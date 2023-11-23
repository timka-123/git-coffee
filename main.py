import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class CoffeeProgram(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setup_database()

    def setup_database(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('coffee.sqlite')
        self.db.open()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('items')
        self.model.select()
        self.items.setModel(self.model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CoffeeProgram()
    widget.show()
    app.exec_()
