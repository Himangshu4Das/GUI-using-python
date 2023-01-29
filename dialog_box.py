from PyQt5.QtWidgets import *

# Create a class to open a dialog box. Deriving attributes from QDialog class
class MyDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(MyDialog, self).__init__(*args, **kwargs)
        # initialize layout
        self.setWindowTitle("Dialog box")
        self.resize(1000, 500)
        self.layout = QVBoxLayout()

        # Create a label
        self.label = QLabel("Cool")

        # Add label as widget
        self.layout.addWidget(self.label)

        # connect to the main layout
        self.setLayout(self.layout)

# Create class and extend from super class QMainWindow to derive functionalities
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create window and layout for it
        self.setWindowTitle("Checkboxes")
        self.resize(1280, 720)
        layout = QVBoxLayout()

        # Create a button
        btn = QPushButton("Press this")

        # Action for the button
        # btn.pressed.connect(lambda: MyDialog().exec())
        # Alternatively
        btn.pressed.connect(self.dialog_handler)

        # Add button as widget
        layout.addWidget(btn)


        # Initialize the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def dialog_handler(self):
        dialog = MyDialog()
        dialog.label.setText("Changing dialog label!")
        dialog.exec()

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
