from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from ui.order import Order
from helper.crud import CRUD

class HomeU(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.crud = CRUD()
        self.crud.create_price_table()
        self.crud.create_customer_table()

        self.count = 0
        self.count2 = 0
        self.count3 = 0

        self.setWindowTitle("Home")
        self.setFixedSize(1300, 800)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.center_window()

        # Background Image
        self.background_label = QtWidgets.QLabel(self)
        self.background_pixmap = QtGui.QPixmap("res/Water.jpg")
        self.background_pixmap = self.background_pixmap.scaled(
            1300, 800, QtCore.Qt.KeepAspectRatioByExpanding, QtCore.Qt.SmoothTransformation
        )
        self.background_label.setPixmap(self.background_pixmap)

        # Apply Blur Effect to Background
        blur_effect = QtWidgets.QGraphicsBlurEffect(self)
        blur_effect.setBlurRadius(10)
        self.background_label.setGraphicsEffect(blur_effect)

        # Left Sidebar
        self.panel1 = QtWidgets.QWidget(self)
        self.panel1.setGeometry(0, 0, 300, 800)
        self.panel1.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.9);
            border: 2px solid #000;
            background-image: url('res/Water.jpg');
            background-repeat: no-repeat;
            background-position: center;
        """)

        # Logo
        logo_label = QtWidgets.QLabel(self)
        logo_pixmap = QtGui.QPixmap("res/logo.jpg").scaled(200, 200, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        
        # Create a rounded mask
        mask = QtGui.QBitmap(logo_pixmap.size())
        mask.fill(QtCore.Qt.color0)
        painter = QtGui.QPainter(mask)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtCore.Qt.color1)
        painter.drawRoundedRect(mask.rect(), 15, 15)
        painter.end()

        logo_pixmap.setMask(mask)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setGeometry(50, 50, 200, 200)

        # Dashboard Button
        self.dashboard_button = QtWidgets.QPushButton("Dashboard", self)
        self.dashboard_button.setFont(QtGui.QFont("Poppins", 12))
        self.dashboard_button.setGeometry(49, 400, 200, 70)
        self.dashboard_button.setStyleSheet("""
            QPushButton {
                background-color: #0077be;
                color: white;
                border: 2px solid #005f8a;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #0093d0;
            }
            QPushButton:pressed {
                background-color: #005f8a;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)

        # Order Button
        self.order_button = QtWidgets.QPushButton("Order", self)
        self.order_button.setFont(QtGui.QFont("Poppins", 12))
        self.order_button.setGeometry(49, 500, 200, 70)
        self.order_button.setStyleSheet("""
            QPushButton {
                background-color: #0077be;
                color: white;
                border: 2px solid #005f8a;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #0093d0;
            }
            QPushButton:pressed {
                background-color: #005f8a;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        self.order_button.clicked.connect(self.open_order)

        # Panel 1
        self.panel1 = QtWidgets.QWidget(self)
        self.panel1.setGeometry(375, 180, 250, 550)  # Position and size of the panel
        self.panel1.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.9);  /* White with transparency */
            border: 2px solid #000;                      /* Black border */
            border-radius: 15px;                         /* Rounded corners */
        """)

        # Panel 2
        self.panel2 = QtWidgets.QWidget(self)
        self.panel2.setGeometry(645, 180, 250, 550)  # Position and size of the panel
        self.panel2.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.9);  /* White with transparency */
            border: 2px solid #000;                      /* Black border */
            border-radius: 15px;                         /* Rounded corners */
        """)

        # Panel 3
        self.panel3 = QtWidgets.QWidget(self)
        self.panel3.setGeometry(925, 180, 250, 550)  # Position and size of the panel
        self.panel3.setStyleSheet("""
            background-color: rgba(255, 255, 255, 0.9);  /* White with transparency */
            border: 2px solid #000;                      /* Black border */
            border-radius: 15px;                         /* Rounded corners */
        """)

        self.items()
        self.field_text()
        self.buttons()

    def center_window(self):
        # Get screen geometry
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def open_order(self):
        self.order_window = Order(self)  # Instantiate the Home window
        self.order_window.show()  # Show the Home window
        self.close()

    def items(self):
        # Logo Item 1 ##################################################
        logo_label = QtWidgets.QLabel(self)
        logo_pixmap = QtGui.QPixmap("res/bottle.png").scaled(200, 200, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        
        # Create a rounded mask
        mask = QtGui.QBitmap(logo_pixmap.size())
        mask.fill(QtCore.Qt.color0)
        painter = QtGui.QPainter(mask)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtCore.Qt.color1)
        painter.drawRoundedRect(mask.rect(), 15, 15)
        painter.end()

        logo_pixmap.setMask(mask)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setGeometry(400, 200, 200, 200)

        # Logo Item 2 ##################################################
        logo_label = QtWidgets.QLabel(self)
        logo_pixmap = QtGui.QPixmap("res/Water_containe.png").scaled(200, 200, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        
        # Create a rounded mask 
        mask = QtGui.QBitmap(logo_pixmap.size())
        mask.fill(QtCore.Qt.color0)
        painter = QtGui.QPainter(mask)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtCore.Qt.color1)
        painter.drawRoundedRect(mask.rect(), 15, 15)
        painter.end()

        logo_pixmap.setMask(mask)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setGeometry(665, 200, 200, 200)

        # Logo Item 3 ##################################################
        logo_label = QtWidgets.QLabel(self)
        logo_pixmap = QtGui.QPixmap("res/5_Gallon.png").scaled(200, 200, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        
        # Create a rounded mask
        mask = QtGui.QBitmap(logo_pixmap.size())
        mask.fill(QtCore.Qt.color0)
        painter = QtGui.QPainter(mask)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtCore.Qt.color1)
        painter.drawRoundedRect(mask.rect(), 15, 15)
        painter.end()

        logo_pixmap.setMask(mask)
        logo_label.setPixmap(logo_pixmap)
        logo_label.setGeometry(1000, 200, 200, 200)

    def field_text(self):
        prices = self.crud.read_price()

        self.item1_price = prices[0]['price']
        self.item2_price = prices[1]['price']
        self.item3_price = prices[2]['price']

        self.item1_stock = prices[0]['quantity']
        self.item2_stock = prices[1]['quantity']
        self.item3_stock = prices[2]['quantity']

        self.item1_field = QtWidgets.QLabel(self)
        self.item1_field.setText(f"Price: {self.item1_price}")
        font = QtGui.QFont("Poppins", 10)
        font.setBold(True)  # Set the font to bold
        self.item1_field.setFont(font)
        self.item1_field.setGeometry(400, 450, 100, 30)
        self.item1_field.setStyleSheet("padding-left: 10px; background: transparent; color: black;")

        self.item1_field2 = QtWidgets.QLabel(self)
        self.item1_field2.setText(f"Stock: {self.item1_stock}")
        font = QtGui.QFont("Poppins", 10)
        font.setBold(True)  # Set the font to bold
        self.item1_field2.setFont(font)
        self.item1_field2.setGeometry(500, 450, 100, 30)
        self.item1_field2.setStyleSheet("padding-left: 10px; background: transparent; color: black;")

        self.item1_field3 = QtWidgets.QLabel(self)
        self.item1_field3.setText("Price: 0 Total: 0")
        font = QtGui.QFont("Poppins", 10)
        font.setBold(True)  # Set the font to bold
        self.item1_field3.setFont(font)
        self.item1_field3.setGeometry(400, 580, 200, 30)
        self.item1_field3.setStyleSheet("background: transparent; color: black;")
        self.item1_field3.setAlignment(QtCore.Qt.AlignCenter)

        self.item2_field = QtWidgets.QLabel(self)
        self.item2_field.setText(f"Price: {self.item2_price}")
        font = QtGui.QFont("Poppins", 10)
        font.setBold(True)  # Set the font to bold
        self.item2_field.setFont(font)
        self.item2_field.setGeometry(670, 450, 100, 30)
        self.item2_field.setStyleSheet("padding-left: 10px; background: transparent; color: black;")

        self.item2_field2 = QtWidgets.QLabel(self)
        self.item2_field2.setText(f"Stock: {self.item2_stock}")
        font = QtGui.QFont("Poppins", 10)
        font.setBold(True)  # Set the font to bold
        self.item2_field2.setFont(font)
        self.item2_field2.setGeometry(770, 450, 100, 30)
        self.item2_field2.setStyleSheet("padding-left: 10px; background: transparent; color: black;")

        self.item2_field3 = QtWidgets.QLabel(self)
        self.item2_field3.setText("Price: 0 Total: 0")
        font = QtGui.QFont("Poppins", 10)
        font.setBold(True)  # Set the font to bold
        self.item2_field3.setFont(font)
        self.item2_field3.setGeometry(670, 580, 200, 30)
        self.item2_field3.setStyleSheet("background: transparent; color: black;")
        self.item2_field3.setAlignment(QtCore.Qt.AlignCenter)

        self.item3_field = QtWidgets.QLabel(self)
        self.item3_field.setText(f"Price: {self.item3_price}")
        font = QtGui.QFont("Poppins", 10)
        font.setBold(True)  # Set the font to bold
        self.item3_field.setFont(font)
        self.item3_field.setGeometry(950, 450, 100, 30)
        self.item3_field.setStyleSheet("padding-left: 10px; background: transparent; color: black;")

        self.item3_field2 = QtWidgets.QLabel(self)
        self.item3_field2.setText(f"Stock: {self.item3_stock}")
        font = QtGui.QFont("Poppins", 10)
        font.setBold(True)  # Set the font to bold
        self.item3_field2.setFont(font)
        self.item3_field2.setGeometry(1050, 450, 100, 30)
        self.item3_field2.setStyleSheet("padding-left: 10px; background: transparent; color: black;")

        self.item3_field3 = QtWidgets.QLabel(self)
        self.item3_field3.setText("Price: 0 Total: 0")
        font = QtGui.QFont("Poppins", 10)
        font.setBold(True)  # Set the font to bold
        self.item3_field3.setFont(font)
        self.item3_field3.setGeometry(950, 580, 200, 30)
        self.item3_field3.setStyleSheet("background: transparent; color: black;")
        self.item3_field3.setAlignment(QtCore.Qt.AlignCenter)

    def buttons(self):
        self.item1_button = QtWidgets.QPushButton("Add", self)
        self.item1_button.setFont(QtGui.QFont("Poppins", 12))
        self.item1_button.setGeometry(400, 500, 100, 70)
        self.item1_button.setStyleSheet("""
            QPushButton {
                background-color: #0077be;
                color: white;
                border: 2px solid #005f8a;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #0093d0;
            }
            QPushButton:pressed {
                background-color: #005f8a;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        self.item1_button.clicked.connect(self.add_item)

        self.item1_button2 = QtWidgets.QPushButton("Remove", self)
        self.item1_button2.setFont(QtGui.QFont("Poppins", 12))
        self.item1_button2.setGeometry(500, 500, 100, 70)
        self.item1_button2.setStyleSheet("""
            QPushButton {
                background-color: #0077be;
                color: white;
                border: 2px solid #005f8a;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #0093d0;
            }
            QPushButton:pressed {
                background-color: #005f8a;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        self.item1_button2.clicked.connect(self.remove_item)

        self.item1_button3 = QtWidgets.QPushButton("Checkout", self)
        self.item1_button3.setFont(QtGui.QFont("Poppins", 12))
        self.item1_button3.setGeometry(400, 620, 200, 70)
        self.item1_button3.setStyleSheet("""
            QPushButton {
                background-color: #0077be;
                color: white;
                border: 2px solid #005f8a;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #0093d0;
            }
            QPushButton:pressed {
                background-color: #005f8a;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        # self.item1_button.clicked.connect(self.update_item)

        self.item2_button = QtWidgets.QPushButton("Add", self)
        self.item2_button.setFont(QtGui.QFont("Poppins", 12))
        self.item2_button.setGeometry(670, 500, 100, 70)
        self.item2_button.setStyleSheet("""
            QPushButton {
                background-color: #0077be;
                color: white;
                border: 2px solid #005f8a;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #0093d0;
            }
            QPushButton:pressed {
                background-color: #005f8a;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        self.item2_button.clicked.connect(self.add_item2)

        self.item2_button2 = QtWidgets.QPushButton("Remove", self)
        self.item2_button2.setFont(QtGui.QFont("Poppins", 12))
        self.item2_button2.setGeometry(770, 500, 100, 70)
        self.item2_button2.setStyleSheet("""
            QPushButton {
                background-color: #0077be;
                color: white;
                border: 2px solid #005f8a;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #0093d0;
            }
            QPushButton:pressed {
                background-color: #005f8a;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        self.item2_button2.clicked.connect(self.remove_item2)

        self.item2_button3 = QtWidgets.QPushButton("Checkout", self)
        self.item2_button3.setFont(QtGui.QFont("Poppins", 12))
        self.item2_button3.setGeometry(670, 620, 200, 70)
        self.item2_button3.setStyleSheet("""
            QPushButton {
                background-color: #0077be;
                color: white;
                border: 2px solid #005f8a;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #0093d0;
            }
            QPushButton:pressed {
                background-color: #005f8a;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        # self.item1_button.clicked.connect(self.update_item)

        self.item3_button = QtWidgets.QPushButton("Add", self)
        self.item3_button.setFont(QtGui.QFont("Poppins", 12))
        self.item3_button.setGeometry(950, 500, 100, 70)
        self.item3_button.setStyleSheet("""
            QPushButton {
                background-color: #0077be;
                color: white;
                border: 2px solid #005f8a;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #0093d0;
            }
            QPushButton:pressed {
                background-color: #005f8a;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        self.item3_button.clicked.connect(self.add_item3)

        self.item3_button2 = QtWidgets.QPushButton("Remove", self)
        self.item3_button2.setFont(QtGui.QFont("Poppins", 12))
        self.item3_button2.setGeometry(1050, 500, 100, 70)
        self.item3_button2.setStyleSheet("""
            QPushButton {
                background-color: #0077be;
                color: white;
                border: 2px solid #005f8a;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #0093d0;
            }
            QPushButton:pressed {
                background-color: #005f8a;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        self.item3_button2.clicked.connect(self.remove_item3)

        self.item3_button3 = QtWidgets.QPushButton("Checkout", self)
        self.item3_button3.setFont(QtGui.QFont("Poppins", 12))
        self.item3_button3.setGeometry(950, 620, 200, 70)
        self.item3_button3.setStyleSheet("""
            QPushButton {
                background-color: #0077be;
                color: white;
                border: 2px solid #005f8a;
                border-radius: 15px;
                font-weight: bold;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #0093d0;
            }
            QPushButton:pressed {
                background-color: #005f8a;
                padding-left: 5px;
                padding-top: 5px;
            }
        """)
        # self.item1_button.clicked.connect(self.update_item)

    def add_item(self):
        price = self.item1_price
        stock = self.item1_stock

        if stock > self.count:
            self.count += 1
            self.item1_field3.setText(f"Price: {price * self.count} Total: {self.count}")

    def remove_item(self):
        price = self.item1_price

        if 0 < self.count:
            self.count -= 1
            self.item1_field3.setText(f"Price: {price * self.count} Total: {self.count}")

    def add_item2(self):
        price = self.item2_price
        stock = self.item2_stock

        if stock > self.count2:
            self.count2 += 1
            self.item2_field3.setText(f"Price: {price * self.count2} Total: {self.count2}")

    def remove_item2(self):
        price = self.item2_price
        
        if 0 < self.count2:
            self.count2 -= 1
            self.item2_field3.setText(f"Price: {price * self.count2} Total: {self.count2}")

    def add_item3(self):
        price = self.item3_price
        stock = self.item3_stock

        if stock > self.count3:
            self.count3 += 1
            self.item3_field3.setText(f"Price: {price * self.count3} Total: {self.count3}")

    def remove_item3(self):
        price = self.item3_price
        
        if 0 < self.count3:
            self.count3 -= 1
            self.item3_field3.setText(f"Price: {price * self.count3} Total: {self.count3}")