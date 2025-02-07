import math
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6 import uic


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)

        self.pantalla_label = self.findChild(QLabel, "Pantalla")
        self.log_tableWidget = self.findChild(QTableWidget, "log")  # Ahora correctamente identificado como QTableWidget

        # Configurar tabla de historial
        self.log_tableWidget.setColumnCount(2)
        self.log_tableWidget.setHorizontalHeaderLabels(["Operación", "Resultado"])
        self.log_tableWidget.setRowCount(0)

        # Conexiones de los botones
        for i in range(10):
            self.findChild(QPushButton, f"button{i}").clicked.connect(lambda _, n=i: self.add_number(str(n)))

        self.findChild(QPushButton, "buttonP1").clicked.connect(lambda: self.add_number("("))
        self.findChild(QPushButton, "buttonP2").clicked.connect(lambda: self.add_number(")"))
        self.findChild(QPushButton, "buttonMas").clicked.connect(lambda: self.add_operator("+"))
        self.findChild(QPushButton, "buttonMenos").clicked.connect(lambda: self.add_operator("-"))
        self.findChild(QPushButton, "buttonX").clicked.connect(lambda: self.add_operator("*"))
        self.findChild(QPushButton, "buttonDividir").clicked.connect(lambda: self.add_operator("/"))
        self.findChild(QPushButton, "buttonAC").clicked.connect(self.clear)
        self.findChild(QPushButton, "buttonIgual").clicked.connect(self.calculate)
        self.findChild(QPushButton, "buttonPunto").clicked.connect(self.add_point)
        self.findChild(QPushButton, "buttonDel").clicked.connect(self.delete)
        self.findChild(QPushButton, "buttonPorcentaje").clicked.connect(self.percentage)
        self.findChild(QPushButton, "buttonSQR").clicked.connect(self.square)
        self.findChild(QPushButton, "buttonSEN").clicked.connect(self.sine)
        self.findChild(QPushButton, "buttonCOS").clicked.connect(self.cosine)

        self.operation = ""
        self.result = None
        self.operators = "+-*/"

    def print_operation(self):
        self.pantalla_label.setText(self.operation)

    def add_number(self, number):
        self.operation += number
        self.print_operation()

    def add_point(self):
        if not self.operation or self.operation[-1] in self.operators:
            self.operation += "0."
        elif "." not in self.operation.split(self.operators[-1])[-1]:
            self.operation += "."
        self.print_operation()

    def add_operator(self, operator):
        if self.operation and self.operation[-1] not in self.operators:
            self.operation += operator
        elif not self.operation:
            self.operation = "0" + operator
        self.print_operation()

    def calculate(self):
        try:
            self.result = str(eval(self.operation))
            self.pantalla_label.setText(self.result)
            self.add_to_log(self.operation, self.result)
            self.operation = self.result
        except ZeroDivisionError:
            self.pantalla_label.setText("Error: Div / 0")
        except Exception:
            self.pantalla_label.setText("Error")

    def clear(self):
        self.operation = ""
        self.pantalla_label.setText("")

    def delete(self):
        self.operation = self.operation[:-1]
        self.print_operation()

    def square(self):
        try:
            self.operation = str(float(self.operation) ** 2)
            self.print_operation()
        except ValueError:
            self.pantalla_label.setText("Error")

    def percentage(self):
        try:
            self.operation = str(float(self.operation) / 100)
            self.print_operation()
        except ValueError:
            self.pantalla_label.setText("Error")

    def sine(self):
        try:
            self.operation = str(math.sin(math.radians(float(self.operation))))
            self.print_operation()
        except ValueError:
            self.pantalla_label.setText("Error")

    def cosine(self):
        try:
            self.operation = str(math.cos(math.radians(float(self.operation))))
            self.print_operation()
        except ValueError:
            self.pantalla_label.setText("Error")

    def add_to_log(self, operation, result):
        """ Agrega la operación y su resultado al log (QTableWidget). """
        row_count = self.log_tableWidget.rowCount()
        self.log_tableWidget.insertRow(row_count)
        self.log_tableWidget.setItem(row_count, 0, QTableWidgetItem(operation))
        self.log_tableWidget.setItem(row_count, 1, QTableWidgetItem(result))


if __name__ == "__main__":
    app = QApplication([])
    calculadora = Calculadora()
    calculadora.show()
    app.exec()