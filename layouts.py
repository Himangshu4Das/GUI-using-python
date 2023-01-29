from PyQt5.QtWidgets import *


# Create class and extend from super class QMainWindow to derive functionalities
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create window and layout for it
        self.setWindowTitle("Line edits")
        self.resize(1280, 720)

        '''Uncomment the bloc of code to apply different types of layouts'''

        # # =====Vertical Layout=====
        # layout = QVBoxLayout()
        # layout.addWidget(QLabel("Stuff 1"))
        # layout.addWidget(QLabel("Stuff 2"))
        # layout.addWidget(QLabel("Stuff 3"))
        # layout.addWidget(QLabel("Stuff 4"))
        # layout.addWidget(QLabel("Stuff 5"))


        # =====Horizontal Layout=====
        layout = QHBoxLayout()
        layout.addWidget(QLabel("Stuff 1"))
        layout.addWidget(QLabel("Stuff 2"))
        layout.addWidget(QLabel("Stuff 3"))
        layout.addWidget(QLabel("Stuff 4"))
        layout.addWidget(QLabel("Stuff 5"))


        # # =====Grid Layout=====
        # layout = QGridLayout()
        #
        # layout.addWidget(QLabel("Stuff 1"),0,0)    # coordinates (r,c)
        # layout.addWidget(QLabel("Stuff 2"),1,1)
        # layout.addWidget(QLabel("Stuff 3"),2,2)
        # layout.addWidget(QLabel("Stuff 4"),3,3)
        # layout.addWidget(QLabel("Stuff 5"),5,5)


        # # =====Stacked Layout=====
        # layout = QStackedLayout()
        #
        # layout.addWidget(QLabel("Stuff 1"))    # Only the first is printed FIFO
        # layout.addWidget(QLabel("Stuff 2"))
        # layout.addWidget(QLabel("Stuff 3"))
        # layout.addWidget(QLabel("Stuff 4"))
        # layout.addWidget(QLabel("Stuff 5"))

        # Initialize the widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
