from PyQt5.QtWidgets import *


# Create class and extend from super class QMainWindow to derive functionalities
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create window and layout for it
        self.setWindowTitle("Line edits")
        self.resize(1280, 720)
        layout = QVBoxLayout()

        # Create a line for line edit
        input_field = QLineEdit()

        # add line edit widgets to layout
        layout.addWidget(input_field)

        # add actions to line edit ( on pressing enter )
        input_field.returnPressed.connect(lambda: print(input_field.text()))

        # Initialize the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
