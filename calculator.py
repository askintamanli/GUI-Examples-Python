import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Main(QWidget):

    def __init__(self):
        super(Main, self).__init__()

        self.setWindowTitle("CALCULATOR")
        

        self.interface1()
        
        self.show()

    def interface1(self):

        # BUTTONS
        self.space_LineEdit = QLineEdit()

        self.ButtonEmpty1 = QPushButton()
        self.ButtonDel = QPushButton("Del")
        self.ButtonClear = QPushButton("Clear")
        self.ButtonDivide = QPushButton("/")   

        
        self.Button7 = QPushButton("7")
        self.Button8 = QPushButton("8")
        self.Button9 = QPushButton("9")
        self.ButtonMultiply = QPushButton("X")

        self.Button4 = QPushButton("4")
        self.Button5 = QPushButton("5")
        self.Button6 = QPushButton("6")
        self.ButtonMinus = QPushButton("-")

        self.Button1 = QPushButton("1")
        
        self.Button2 = QPushButton("2")
        self.Button3 = QPushButton("3")
        self.ButtonPlus = QPushButton("+")
        
        self.ButtonEmpty2 = QPushButton()
        self.Button0 = QPushButton("0")
        self.ButtonPoint = QPushButton(",")
        self.ButtonEqual = QPushButton("=")
        self.ButtonEqual.setStyleSheet("background-color : orange")
        

        #ALIGN
        HBox0 = QHBoxLayout()
        HBox0.addWidget(self.space_LineEdit)
        

        HBox1 = QHBoxLayout()
        HBox1.addWidget(self.ButtonEmpty1)
        HBox1.addWidget(self.ButtonDel)
        HBox1.addWidget(self.ButtonClear)
        HBox1.addWidget(self.ButtonDivide)
        

        HBox2 = QHBoxLayout()
        HBox2.addWidget(self.Button7)
        HBox2.addWidget(self.Button8)
        HBox2.addWidget(self.Button9)
        HBox2.addWidget(self.ButtonMultiply)
        

        HBox3 = QHBoxLayout()
        HBox3.addWidget(self.Button4)
        HBox3.addWidget(self.Button5)
        HBox3.addWidget(self.Button6)
        HBox3.addWidget(self.ButtonMinus)
        

        HBox4 = QHBoxLayout()
        HBox4.addWidget(self.Button1)
        HBox4.addWidget(self.Button2)
        HBox4.addWidget(self.Button3)
        HBox4.addWidget(self.ButtonPlus)

        HBox5 = QHBoxLayout()
        HBox5.addWidget(self.ButtonEmpty2)
        HBox5.addWidget(self.Button0)
        HBox5.addWidget(self.ButtonPoint)
        HBox5.addWidget(self.ButtonEqual)
        
        #Birleştirme
        VBox = QVBoxLayout()
        VBox.addLayout(HBox0)
        VBox.addLayout(HBox1)
        VBox.addLayout(HBox2)
        VBox.addLayout(HBox3)
        VBox.addLayout(HBox4)
        VBox.addLayout(HBox5)

        self.setLayout(VBox)
        
        #Connect
        self.Button1.clicked.connect(self.opeariton_1)
        self.Button2.clicked.connect(self.opeariton_2)
        self.Button3.clicked.connect(self.opeariton_3)
        self.Button4.clicked.connect(self.opeariton_4)
        self.Button5.clicked.connect(self.opeariton_5)
        self.Button6.clicked.connect(self.opeariton_6)
        self.Button7.clicked.connect(self.opeariton_7)
        self.Button8.clicked.connect(self.opeariton_8)
        self.Button9.clicked.connect(self.opeariton_9)
        self.Button0.clicked.connect(self.opeariton_0)
        self.ButtonPoint.clicked.connect(self.opeariton_Point)
        self.ButtonDivide.clicked.connect(self.opeariton_Divide)
        self.ButtonMultiply.clicked.connect(self.opeariton_Multiply)
        self.ButtonMinus.clicked.connect(self.opeariton_Minus)
        self.ButtonPlus.clicked.connect(self.opeariton_Plus)
        self.ButtonClear.clicked.connect(self.operation_Clear)
        self.ButtonDel.clicked.connect(self.operation_Del)
        self.ButtonEqual.clicked.connect(self.operation_Equal)



    def opeariton_1(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "1")

    def opeariton_2(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "2")
    
    def opeariton_3(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "3")
    
    def opeariton_4(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "4")

    def opeariton_5(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "5")
    
    def opeariton_6(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "6")
    def opeariton_7(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "7")

    def opeariton_8(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "8")
    
    def opeariton_9(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "9")
    
    def opeariton_0(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "0")

    def opeariton_Point(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + ".")
    
    def opeariton_Divide(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "/")

    def opeariton_Multiply(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "*")
    
    def opeariton_Minus(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "-")

    def opeariton_Plus(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text + "+")
    
    def operation_Clear(self):
        self.space_LineEdit.setText("")

    def operation_Del(self):
        text = self.space_LineEdit.text()
        self.space_LineEdit.setText(text[:len(text)-1])

    def operation_Equal(self):
        text = self.space_LineEdit.text()
        result = eval(text)
        self.space_LineEdit.setText(str(result))
        



if __name__ == '__main__':
    app = QApplication(sys.argv)
    MAIN = Main()
    sys.exit(app.exec_())