from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Create class and extend from super class QMainWindow to derive functionalities
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # lets build our app
        self.setWindowTitle("Buttons Window")
        self.resize(1280,720)

        # layout
        layout = QVBoxLayout()
        # initialize buttons
        bt1 = QPushButton('Button 1')
        bt2 = QPushButton('Button 2')

        # Create self label to make it an attribute of the class.
        # Then we can access it anywhere in the class
        self.label = QLabel("Click any button")

        # set fonts
        font = self.label.font()
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        # add actions and events
        bt1.clicked.connect(self.bt1_clicked)
        bt2.clicked.connect(self.bt2_clicked)

        # add stuff to a layout
        layout.addWidget(self.label)
        layout.addWidget(bt1)
        layout.addWidget(bt2)

        # initialize a widget and then set the layout
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def bt1_clicked(self):
        self.label.setText("You clicked button 1")
    def bt2_clicked(self):
        self.label.setText("You clicked button 2")

app = QApplication([])
window = MainWindow()
window.show()
app.exec()