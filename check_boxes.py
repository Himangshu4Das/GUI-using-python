from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Create class and extend from super class QMainWindow to derive functionalities
class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create window and layout for it
        self.setWindowTitle("Checkboxes")
        self.resize(1280,720)
        layout = QVBoxLayout()

        # Create checkbox
        check1 = QCheckBox("Task 1")
        check2 = QCheckBox("Task 2")

        # Create actions for checkbox events
        check1.toggled.connect(lambda: self.something_checked(check1))
        check2.toggled.connect(lambda: self.something_checked(check2))


        # Default message
        self.label = QLabel("You have not selected anything")

        # List of checked boxes
        self.checked_stuff = []

        # Create checkboxes and labels as widgets
        layout.addWidget(check1)
        layout.addWidget(check2)
        layout.addWidget(self.label)

        # Initialize the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # Function do something each a time a checkbox is checked
    def something_checked(self, check):
        if check.isChecked() == False:
            self.checked_stuff= list(filter(lambda stuff: (stuff!= check.text()) ,self.checked_stuff))

        else:
            self.checked_stuff.append(check.text())

        task_string = ""
        for task in self.checked_stuff:
            task_string += (task+' checked!\n')

        self.label.setText(task_string)

app = QApplication([])
window = MainWindow()
window.show()
app.exec()