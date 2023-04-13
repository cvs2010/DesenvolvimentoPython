import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QWidget, QVBoxLayout

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    cw = QWidget()
    vlayout = QVBoxLayout()
    cw.setLayout(vlayout)

    label1 = QLabel('Olá, Mundo!')
    vlayout.addWidget(label1)

    window.setCentralWidget(cw)
    window.show()
    app.exec()