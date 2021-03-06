import sys
import os
from dotenv import load_dotenv
from PyQt5.QtWidgets import QWidget, QApplication
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wl = WishList()
    wl.setWindowTitle('WishList')
    wl.show()
    sys.exit(app.exec_())
