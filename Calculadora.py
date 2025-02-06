from PyQt6.QtWidgets import QApplication, QPushButton, QLabel, QMainWindow, QTableWidget
from PyQt6 import uic
from PyQt6.QtCore import Qt

class Calculadora(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('untitled.ui', self)  # Cargar el archivo .ui
        
        # Crear etiquetas para mostrar la operación y el resultado
        self.pantalla_label = self.findChild(QLabel, "Pantalla")
        self.log_label = self.findChild(QTableWidget, "Log")

        # Conectar los botones con las funciones correspondientes
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
        
        self.findChild(QPushButton, "buttonMas").clicked.connect(lambda: self.add_operator("+"))
        self.findChild(QPushButton, "buttonMenos").clicked.connect(lambda: self.add_operator("-"))
        self.findChild(QPushButton, "buttonX").clicked.connect(lambda: self.add_operator("*"))
        self.findChild(QPushButton, "buttonDividir").clicked.connect(lambda: self.add_operator("/"))

        self.findChild(QPushButton, "buttonAC").clicked.connect(self.clear)
        self.findChild(QPushButton, "buttonIgual").clicked.connect(self.calculate)
        self.findChild(QPushButton, "buttonPunto").clicked.connect(self.add_point)
        self.findChild(QPushButton, "buttonDel").clicked.connect(self.delete)
        self.findChild(QPushButton, "buttonEXP").clicked.connect(self.exponential)
        self.findChild(QPushButton, "buttonSQR").clicked.connect(self.square)

        # Inicializar la operación y el resultado
        self.operation = ""
        self.result = None
        self.operators = "+-*/"
    
    def print_operation(self):
        # Mostrar la operación actual en la pantalla y el historial
        self.pantalla_label.setText(self.operation)
        self.log_label.setText(f"{self.operation} = {self.result}" if self.result else self.operation)

    def print_error(self, error="Error"):
        # Mostrar un error en el historial de operaciones
        self.log_label.setStyleSheet("color: #f00")
        self.log_label.setText(error)

    def add_number(self, number):
        # Agregar un número a la operación
        self.operation += number
        self.print_operation()

    def add_point(self):
        # Agregar un punto decimal si es necesario
        if "." not in self.operation.split()[-1]:  # Asegurarse de no agregar puntos múltiples
            self.operation += "."
            self.print_operation()

    def add_operator(self, operator):
        # Agregar un operador a la operación
        if self.operation and self.operation[-1] not in self.operators:
            self.operation += operator
        elif not self.operation:  # Si no hay operación, iniciar con el operador
            self.operation = "0" + operator
        self.print_operation()

    def calculate(self):
        if not self.operation:
            return

        try:
            # Evaluar la operación ingresada
            self.result = str(eval(self.operation))  

            # Mostrar el resultado en la pantalla
            self.pantalla_label.setText(self.result)

            # Agregar la operación y el resultado al historial sin sobrescribirlo
            historial = self.log_label.text()
            nuevo_historial = historial + f"\n{self.operation} = {self.result}" if historial else f"{self.operation} = {self.result}"
            self.log_label.setText(nuevo_historial)

            # Guardar el resultado en self.operation para seguir operando
            self.operation = self.result

        except ZeroDivisionError:
            self.print_error("Error, No se puede dividir por 0")
        except (SyntaxError, ValueError):
            self.print_error("Error de Sintaxis")
        except Exception:
            self.print_error()


    def clear(self):
        # Limpiar la operación y los resultados
        self.operation = ""
        self.pantalla_label.setText("")
        self.log_label.setText("")

    def delete(self):
        # Eliminar el último carácter de la operación
        self.operation = self.operation[:-1]
        self.print_operation()

    def exponential(self):
        try:
            num = float(self.log_label.text()) 
            self.log_label.setText(str(num ** 2)) 
        except ValueError:
            self.log_label.setText("Error")

    def square(self):
        try:
            num = float(self.log_label.text()) 
            self.log_label.setText(str(num ** 2)) 
        except ValueError:
            self.log_label.setText("Error")

if __name__ == "__main__":
    app = QApplication([])
    calculadora = Calculadora()
    calculadora.show()
    app.exec()