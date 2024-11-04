import sys
from PyQt5.QtWidgets import QApplication, QWidget
from ui.main_window import MainWindow

def main():
    app = QApplication(sys.argv)

    window = MainWindow() 
    window.show()
    window.resize(800, 800)
    window.move(300, 300)

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
