import sys
import os
from dotenv import load_dotenv
from PyQt5.QtWidgets import (
    QWidget, QApplication, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QListWidget
)
from db import Database


load_dotenv()


class WishList(QWidget):
    db = Database(
        os.getenv('USER'),
        os.getenv('PASSWORD'),
        'wishlist',
        'wishes'
    )

    def __init__(self):
        super().__init__()

        self.wishes = self.db.read()

        self.name_expl = QLabel()
        self.name_expl.setText('Name:')
        self.price_expl = QLabel()
        self.price_expl.setText('Price:')
        self.link_expl = QLabel()
        self.link_expl.setText('Link:')
        self.note_expl = QLabel()
        self.note_expl.setText('Note:')
        self.message_label = QLabel()

        self.name_entry = QLineEdit()
        self.price_entry = QLineEdit()
        self.link_entry = QLineEdit()
        self.note_entry = QLineEdit()

        entries = QVBoxLayout()
        entries.addWidget(self.name_expl)
        entries.addWidget(self.name_entry)

        entries.addWidget(self.price_expl)
        entries.addWidget(self.price_entry)

        entries.addWidget(self.link_expl)
        entries.addWidget(self.link_entry)

        entries.addWidget(self.note_expl)
        entries.addWidget(self.note_entry)

        entries.addWidget(self.message_label)

        container = QHBoxLayout()
        container.addLayout(entries)

        common_container = QVBoxLayout()
        common_container.addLayout(container)

        self.wish_list = QListWidget()

        self.wish_list.itemClicked.connect(self.selection_changed)

        wishes = QVBoxLayout()
        wishes.addWidget(self.wish_list)
        container.addLayout(wishes)

        self.setLayout(common_container)

    def selection_changed(self, item):
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wl = WishList()
    wl.setWindowTitle('WishList')
    wl.show()
    sys.exit(app.exec_())
