import sys
import sqlite3

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from PyQt5 import uic


class CoffeeProgram(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setup_database()
        self.createButton.clicked.connect(self.show_add_widget)
        self.updateButton.clicked.connect(self.update_button)

    def setup_database(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('coffee.sqlite')
        self.db.open()
        self.model = QSqlTableModel(self, self.db)
        self.model.setTable('items')
        self.model.select()
        self.items.setModel(self.model)

    def show_add_widget(self):
        print("test")
        self.widget = AddCoffeeForm()

    def update_button(self):
        self.setup_database()


class AddCoffeeForm(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.submitButton.clicked.connect(self.create_item)
        self.show()

    def create_item(self):
        con = sqlite3.connect("coffee.sqlite")
        cursor = con.cursor()
        cursor.execute(f"""INSERT INTO items(sort_name,hot,type,description,price,volume) VALUES (
            '{self.sortEdit.text()}','{self.hotEdit.text()}','{self.typeEdit.text()}','{self.descriptionEdit.text()}',
            '{self.priceEdit.text()}','{self.volumeEdit.text()}'
        )""")
        con.commit()
        con.close()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CoffeeProgram()
    widget.show()
    app.exec_()
