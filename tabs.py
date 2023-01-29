from PyQt5.QtWidgets import *

# Create class and extend from super class QMainWindow to derive functionalities
class MainWindow (QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create window and layout for it
        self.setWindowTitle("Tabs")
        self.resize(1280,720)
        layout = QVBoxLayout()

        # Create tabs
        tabs = QTabWidget()
        tabs.setMovable(True)   # adds movable tabs property to the tab object

        # Add tabs
        tabs.addTab(QLabel("This is tab 1\n"), "TAB 1")
        tabs.addTab(QLabel("This is tab 2\n"), "TAB 2")
        tabs.addTab(QLabel("This is tab 3\n"), "TAB 3")

        # Add tabs to the layout as widgets
        layout.addWidget(tabs)

        # Initialize the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()