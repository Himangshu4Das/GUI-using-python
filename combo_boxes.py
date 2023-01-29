from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Create class and extend from super class QMainWindow to derive functionalities
class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create window and layout for it
        self.setWindowTitle("Combo boxes")
        self.resize(1280, 720)
        layout = QVBoxLayout()

        # Create combo box
        combo = QComboBox()

        # Add options in combo box
        combo.addItems(["Easy", "Intermediate", "Hard"])

        # Add a pushbutton
        btn = QPushButton("Start")

        # Add actions to the pushbutton event
        btn.pressed.connect(lambda: self.show_selected(combo))



        # Default message
        self.label = QLabel("You have not selected anything")

        # List of checked boxes
        self.checked_stuff = []

        # Create comboboxes, attributes and labels as widgets
        layout.addWidget(combo)
        layout.addWidget(btn)
        layout.addWidget(self.label)

        # Initialize the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # Function do something each a time the button is pressed
    def show_selected(self, combo):
        status = combo.currentText()
        self.label.setText(status+' selected!')

app = QApplication([])
window = MainWindow()
window.show()
app.exec()