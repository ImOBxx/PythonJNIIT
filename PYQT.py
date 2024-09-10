import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget

def main():
    # Create a PyQt application
    app = QApplication(sys.argv)

    # Create a QMainWindow (main window)
    main_window = QMainWindow()
    # Set the window properties (title and initial size)
    main_window.setWindowTitle("Basic PyQt Application")
    main_window.setGeometry(100, 100, 400, 300)  # (x, y, width, height)
    # Create a central widget for the main window
    central_widget = QWidget()
    main_window.setCentralWidget(central_widget)
    # Create widgets (QLabel and QPushButton)
    label = QLabel("Example of PyQt label!")
    button = QPushButton("Example of PyQt pushbutton!")
    # Create a layout to arrange the widgets vertically
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(button)
    # Set the layout for the central widget
    central_widget.setLayout(layout)
    # Show the window
    main_window.show()
    # Run the application's event loop
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
