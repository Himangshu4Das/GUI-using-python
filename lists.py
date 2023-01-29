from PyQt5.QtWidgets import *


# Create class and extend from super class QMainWindow to derive functionalities
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create window and layout for it
        self.setWindowTitle("Lists")
        self.resize(1280, 720)
        layout = QVBoxLayout()

        # Create a list
        li = QListWidget()
        li.addItems(["Easy", "Intermediate", "Hard"])

        # Create actions for list
        # li.currentItemChanged.connect(lambda x: print(x.text))
        li.currentItemChanged.connect(
            self.show_selected)  # Alternatively you can use methods instead of lambda function

        # Default message
        self.label = QLabel("You have not selected anything")  # does not work with lists.


        # Create lists and labels as widgets
        layout.addWidget(li)
        layout.addWidget(self.label)

        # Initialize the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    # Function do something each a time the button is pressed
    def show_selected(self, item):
        status = item.text()
        self.label.setText(status + ' selected!')


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
