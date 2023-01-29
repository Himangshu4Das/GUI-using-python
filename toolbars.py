from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


# Create class and extend from super class QMainWindow to derive functionalities
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create window and layout for it
        self.setWindowTitle("Line edits")
        self.resize(1280, 720)

        layout = QVBoxLayout()

        # Create a toolbar
        toolbar = QToolBar("My toolbar")

        # Add actions to toolbar
        # btn1 = QAction("Action 1", self)
        btn1 = QAction(QIcon("icon_sample.png"),"Action 1", self)   # Alternatively you can add icon
        btn1.setCheckable(True)
        toolbar.addAction(btn1)
        toolbar.addSeparator()     # add a separation line among the options

        # Add toolbar to layout
        self.addToolBar(toolbar)

        # Initialize the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
