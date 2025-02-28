import math
from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6 import uic
from PyQt6.QtGui import QFontDatabase, QFont


class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)

        self.pantalla_label = self.findChild(QLabel, "Pantalla")
        self.log_tableWidget = self.findChild(QTableWidget, "log")

        # Configuramos tabla de historial
        self.log_tableWidget.setColumnCount(2)
        self.log_tableWidget.setHorizontalHeaderLabels(["Operación", "Resultado"])
        self.log_tableWidget.setRowCount(0)

        # Estado de encendido/apagado
        self.encendida = True

        # Cargar fuente personalizada para la pantalla
        font_id = QFontDatabase.addApplicationFont("digital-7 (mono).ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        self.pantalla_label.setFont(QFont(font_family, 24))

        # Conexiones de los botones
        self.findChild(QPushButton, "button0").clicked.connect(lambda: self.add_number("0"))
        self.findChild(QPushButton, "button1").clicked.connect(lambda: self.add_number("1"))
        self.findChild(QPushButton, "button2").clicked.connect(lambda: self.add_number("2"))
        self.findChild(QPushButton, "button3").clicked.connect(lambda: self.add_number("3"))
        self.findChild(QPushButton, "button4").clicked.connect(lambda: self.add_number("4"))
        self.findChild(QPushButton, "button5").clicked.connect(lambda: self.add_number("5"))
        self.findChild(QPushButton, "button6").clicked.connect(lambda: self.add_number("6"))
        self.findChild(QPushButton, "button7").clicked.connect(lambda: self.add_number("7"))
        self.findChild(QPushButton, "button8").clicked.connect(lambda: self.add_number("8"))
        self.findChild(QPushButton, "button9").clicked.connect(lambda: self.add_number("9"))

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
        self.findChild(QPushButton, "buttonON").clicked.connect(self.encendido)

        # Variables para almacenar la operación y el resultado
        self.operation = ""
        self.result = None
        self.operators = "+-*/"

    # Función para el botón de encendido
    def encendido(self):
        self.encendida = not self.encendida
        if not self.encendida:
            self.operation = ""
            self.pantalla_label.setText("")
        else:
            self.pantalla_label.setText("0")
    
    # Función para mostrar la operación en la pantalla
    def print_operation(self):
        if self.encendida:
            self.pantalla_label.setText(self.operation)

    # Función para añadir un número
    def add_number(self, number):
        if self.encendida:
            self.operation += number
            self.print_operation()

    # Función para añadir un punto
    def add_point(self):
        if self.encendida:
            if not self.operation or self.operation[-1] in self.operators:
                self.operation += "0."
            elif "." not in self.operation.split(self.operators[-1])[-1]:
                self.operation += "."
            self.print_operation()

    # Función para añadir operadores
    def add_operator(self, operator):
        if self.encendida:
            if self.operation and self.operation[-1] not in self.operators:
                self.operation += operator
            elif not self.operation:
                self.operation = "0" + operator
            self.print_operation()

    # Función para calcular el resultado de una operación
    def calculate(self):
        if self.encendida:
            try:
                self.result = str(eval(self.operation))
                self.pantalla_label.setText(self.result)
                self.add_to_log(self.operation, self.result)
                self.operation = self.result
            except ZeroDivisionError:
                self.pantalla_label.setText("Error: Div / 0")
            except Exception:
                self.pantalla_label.setText("Error")

    # Función para limpiar la pantalla
    def clear(self):
        if self.encendida:
            self.operation = ""
            self.pantalla_label.setText("0")

    # Función para borrar
    def delete(self):
        if self.encendida:
            self.operation = self.operation[:-1]
            self.print_operation()

    # Función para calcular la raíz cuadrada
    def square(self):
        if self.encendida:
            try:
                result = str(float(self.operation) ** 2)
                self.pantalla_label.setText(result)
                self.add_to_log(f"{self.operation}²", result)
                self.operation = result
            except ValueError:
                self.pantalla_label.setText("Error")

    # Función para calcular el porcentaje
    def percentage(self):
        if self.encendida:
            try:
                result = str(float(self.operation) / 100)
                self.pantalla_label.setText(result)
                self.add_to_log(f"{self.operation}%", result)
                self.operation = result
            except ValueError:
                self.pantalla_label.setText("Error")

    # Función para calcular el seno.
    def sine(self):
        if self.encendida:
            try:
                result = str(math.sin(math.radians(float(self.operation))))
                self.pantalla_label.setText(result)
                self.add_to_log(f"sin({self.operation})", result)
                self.operation = result
            except ValueError:
                self.pantalla_label.setText("Error")
    # Función para calcular el coseno
    def cosine(self):
        if self.encendida:
            try:
                result = str(math.cos(math.radians(float(self.operation))))
                self.pantalla_label.setText(result)
                self.add_to_log(f"cos({self.operation})", result)
                self.operation = result
            except ValueError:
                self.pantalla_label.setText("Error")

    # Función para añadir las operaciones al log
    def add_to_log(self, operation, result):
        """Añade la operación y su resultado a la tabla de historial."""
        if self.encendida:
            row_count = self.log_tableWidget.rowCount()
            self.log_tableWidget.insertRow(row_count)
            self.log_tableWidget.setItem(row_count, 0, QTableWidgetItem(operation))
            self.log_tableWidget.setItem(row_count, 1, QTableWidgetItem(result))


if __name__ == "__main__":
    app = QApplication([])
    calculadora = Calculadora()
    calculadora.show()
    app.exec()