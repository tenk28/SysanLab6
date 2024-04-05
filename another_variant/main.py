import sys
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from PyQt6 import QtWidgets, QtGui

from interface import Ui_MainWindow
from cognitive_analysis import Stability
from impulse_modeling import ImpulseProcess


class UI(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.adjacency_matrix = None
        self.stability = None
        self.impulse_process = None
        self.n_model_steps = None
        self.q_impulses = None

        self.output_field.setFont(QtGui.QFont("Consolas", 10))
        self.input_filename.setText('source_cognitive_map.xlsx')
        self.output_filename.setText('result_cognitive_map.xlsx')

        self.load_am.clicked.connect(self.load_adjacency_matrix)
        self.save_am.clicked.connect(self.save_adjacency_matrix)
        self.browse_input.clicked.connect(self.select_input)
        self.browse_output.clicked.connect(self.select_output)
        self.check_stability_button.clicked.connect(self.check_stability)
        self.plot_graph_button.clicked.connect(self.plot_graph)
        self.im.clicked.connect(self.value_impulse_modeling)
        self.im.clicked.connect(self.plot_impulse_modeling)

    def _check_am(self):
        if self.adjacency_matrix is None:
            self.output_field.setText('Can not do this: cognitive map matrix is unfilled.')
            return False
        else:
            return True

    def load_adjacency_matrix(self):
        filename = self.input_filename.text()
        self.adjacency_matrix = pd.read_excel(filename, index_col=0)
        self.output_adjacency_matrix()
        self.set_q_table()

    def save_adjacency_matrix(self):
        if self._check_am():
            filename = self.output_filename.text()
            self.read_adjacency_matrix()
            self.adjacency_matrix.to_excel(filename)

    def select_input(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open data file', '.', 'Data file (*.xlsx)')[0]
        self.input_filename.setText(filename)

    def select_output(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Open data file', '.', 'Data file (*.xlsx)')[0]
        self.output_filename.setText(filename)

    def read_adjacency_matrix(self):
        if self._check_am():
            for i in range(len(self.adjacency_matrix)):
                for j in range(len(self.adjacency_matrix.columns)):
                    self.adjacency_matrix.iloc[i, j] = float(self.adjacency_matrix_out.item(i, j).text())

    def check_stability(self):
        if self._check_am():
            self.read_adjacency_matrix()
            self.stability = Stability(self.adjacency_matrix)

            def bull_converter(bull_term):
                return 'stable.' if bull_term else 'unstable.'

            out_str = 'Results of stability analysis:\n\n'
            out_str += f'Structure stability: {bull_converter(self.stability.structure_stability)}\n'
            out_str += f'Number of pair cycles: {len(self.stability.graph.pair_cycles)}\n'
            if len(self.stability.graph.pair_cycles) != 0:
                out_str += f'List of pair cycles:\n'
                for pc in self.stability.graph.pair_cycles:
                    pc.append(pc[0])
                    pc = '->'.join(e for e in pc) + '\n'
                    out_str += pc
            out_str += f'\nValue stability: {bull_converter(self.stability.value_stability)}\n'
            out_str += f'Perturbation stability: {bull_converter(self.stability.perturbation_stability)}\n'
            out_str += f'Spectral radius: {self.stability.spectral_radius:.3f}\n'
            out_str += f'Cognitive map matrix eigenvalues:\n'
            for ev in self.stability.eigenvalues:
                out_str += '{0:.3f} {1} {2:.3f}j\n'.format(ev.real, '+-'[int(ev.imag < 0)], abs(ev.imag))
            self.output_field.setText(out_str)

    def plot_graph(self):
        if self._check_am():
            self.read_adjacency_matrix()
            self.stability = Stability(self.adjacency_matrix)
            self.stability.graph.plot_graph(True)

    def output_adjacency_matrix(self):
        m, n = self.adjacency_matrix.shape
        self.adjacency_matrix_out.setRowCount(m)
        self.adjacency_matrix_out.setColumnCount(n)
        self.adjacency_matrix_out.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.adjacency_matrix_out.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)

        for idx in range(m):
            horizontal_item = QtWidgets.QTableWidgetItem(self.adjacency_matrix.columns[idx])
            self.adjacency_matrix_out.setHorizontalHeaderItem(idx, horizontal_item)
            vertical_item = QtWidgets.QTableWidgetItem(self.adjacency_matrix.columns[idx])
            self.adjacency_matrix_out.setVerticalHeaderItem(idx, vertical_item)

        for row in range(m):
            for column in range(n):
                item = QtWidgets.QTableWidgetItem(str(self.adjacency_matrix.iloc[row, column]))
                self.adjacency_matrix_out.setItem(row, column, item)

    def execute_set_model_steps(self):
        model_steps = self.impulse_modeling_steps.value()
        self.n_model_steps = model_steps

    def set_q_table(self, q_impulses=None):
        self.q_table.setColumnCount(1)
        self.q_table.setRowCount(len(self.adjacency_matrix.index))
        self.q_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.q_table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        for idx in range(len(self.adjacency_matrix.index)):
            item = QtWidgets.QTableWidgetItem(self.adjacency_matrix.columns[idx])
            self.q_table.setVerticalHeaderItem(idx, item)
        self.q_table.setHorizontalHeaderItem(0, QtWidgets.QTableWidgetItem('Q'))
        if q_impulses is None:
            for i in range(len(self.adjacency_matrix.index)):
                item = QtWidgets.QTableWidgetItem(f'{0.}')
                self.q_table.setItem(i, 0, item)
        else:
            for i in range(len(self.adjacency_matrix.index)):
                item = QtWidgets.QTableWidgetItem(f'{q_impulses.iloc[i, 0]}')
                self.q_table.setItem(i, 0, item)

    def read_q_impulses(self):
        r = len(self.adjacency_matrix.index)
        c = self.n_model_steps+1
        q_impulses = pd.DataFrame(data=np.zeros((r, c)), index=self.adjacency_matrix.index,
                                  columns=list(range(self.n_model_steps + 1)))
        for i in range(len(self.adjacency_matrix.index)):
            q_impulses.iloc[i, 0] = float(self.q_table.item(i, 0).text())

        self.q_impulses = q_impulses

    def value_impulse_modeling(self):
        if self._check_am():
            self.execute_set_model_steps()
            self.read_adjacency_matrix()
            self.read_q_impulses()
            ip = ImpulseProcess(self.adjacency_matrix, self.q_impulses.iloc[:, 0])
            ip.impulse_modeling(self.q_impulses, self.n_model_steps)
            x = ip.x
            out_str = 'Results of impulse modeling:\n'
            out_str += x.to_string()
            self.output_field.setText(out_str)

    def plot_impulse_modeling(self):
        if self._check_am():
            self.execute_set_model_steps()
            self.read_adjacency_matrix()
            self.read_q_impulses()
            ip = ImpulseProcess(self.adjacency_matrix, self.q_impulses.iloc[:, 0])
            ip.impulse_modeling(self.q_impulses, self.n_model_steps)
            ip.x.T.plot()
            plt.show()


def cognitive_analysis_execute():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = UI()
    MainWindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    cognitive_analysis_execute()
