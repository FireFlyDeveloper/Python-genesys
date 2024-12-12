from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from ui.orderU import OrderU
from helper.crud import CRUD

class Home(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.crud = CRUD()
        self.crud.create_price_table()
        self.crud.create_customer_table()

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
        self.order_window = OrderU(self)  # Instantiate the Home window
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

        item1_price = prices[0]['price']
        item2_price = prices[1]['price']
        item3_price = prices[2]['price']

        item1_stock = prices[0]['quantity']
        item2_stock = prices[1]['quantity']
        item3_stock = prices[2]['quantity']

        self.item1_field = QtWidgets.QLineEdit(self)
        self.item1_field.setPlaceholderText(f"Price: {item1_price}")
        self.item1_field.setFont(QtGui.QFont("Poppins", 10))
        self.item1_field.setGeometry(400, 450, 100, 30)
        self.item1_field.setStyleSheet("padding-left: 10px;")

        self.item1_field2 = QtWidgets.QLineEdit(self)
        self.item1_field2.setPlaceholderText(f"Stock: {item1_stock}")
        self.item1_field2.setFont(QtGui.QFont("Poppins", 10))
        self.item1_field2.setGeometry(500, 450, 100, 30)
        self.item1_field2.setStyleSheet("padding-left: 10px;")

        self.item2_field = QtWidgets.QLineEdit(self)
        self.item2_field.setPlaceholderText(f"Price: {item2_price}")
        self.item2_field.setFont(QtGui.QFont("Poppins", 10))
        self.item2_field.setGeometry(670, 450, 100, 30)
        self.item2_field.setStyleSheet("padding-left: 10px;")

        self.item2_field2 = QtWidgets.QLineEdit(self)
        self.item2_field2.setPlaceholderText(f"Stock: {item2_stock}")
        self.item2_field2.setFont(QtGui.QFont("Poppins", 10))
        self.item2_field2.setGeometry(770, 450, 100, 30)
        self.item2_field2.setStyleSheet("padding-left: 10px;")

        self.item3_field = QtWidgets.QLineEdit(self)
        self.item3_field.setPlaceholderText(f"Price: {item3_price}")
        self.item3_field.setFont(QtGui.QFont("Poppins", 10))
        self.item3_field.setGeometry(950, 450, 100, 30)
        self.item3_field.setStyleSheet("padding-left: 10px;")

        self.item3_field2 = QtWidgets.QLineEdit(self)
        self.item3_field2.setPlaceholderText(f"Stock: {item3_stock}")
        self.item3_field2.setFont(QtGui.QFont("Poppins", 10))
        self.item3_field2.setGeometry(1050, 450, 100, 30)
        self.item3_field2.setStyleSheet("padding-left: 10px;")

    def buttons(self):
        self.item1_button = QtWidgets.QPushButton("Apply", self)
        self.item1_button.setFont(QtGui.QFont("Poppins", 12))
        self.item1_button.setGeometry(400, 500, 200, 70)
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
        self.item1_button.clicked.connect(self.update_item)

        self.item2_button = QtWidgets.QPushButton("Apply", self)
        self.item2_button.setFont(QtGui.QFont("Poppins", 12))
        self.item2_button.setGeometry(670, 500, 200, 70)
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
        self.item2_button.clicked.connect(self.update_item2)

        self.item3_button = QtWidgets.QPushButton("Apply", self)
        self.item3_button.setFont(QtGui.QFont("Poppins", 12))
        self.item3_button.setGeometry(950, 500, 200, 70)
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
        self.item3_button.clicked.connect(self.update_item3)

    def show_warning(self):
        message = "Invalid input. Price and stock must be numbers."
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setWindowTitle("Invalid Input")
        msg.setText(message)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def update_item(self):
        price = self.item1_field.text().strip()
        stock = self.item1_field2.text().strip()

        # Check if price and stock are valid numbers
        try:
            price = float(price)  # Convert price to float
            stock = int(stock)    # Convert stock to integer
            self.crud.update_price(1, "bottle", stock, price)
            self.item1_field.setPlaceholderText(f"Price: {price}")
            self.item1_field2.setPlaceholderText(f"Stock: {stock}")
            self.item1_field.setText("")
            self.item1_field2.setText("")
        except ValueError:
            self.show_warning()

    def update_item2(self):
        price = self.item2_field.text().strip()
        stock = self.item2_field2.text().strip()

        # Check if price and stock are valid numbers
        try:
            price = float(price)  # Convert price to float
            stock = int(stock)    # Convert stock to integer
            self.crud.update_price(2, "container", stock, price)
            self.item2_field.setPlaceholderText(f"Price: {price}")
            self.item2_field2.setPlaceholderText(f"Stock: {stock}")
            self.item2_field.setText("")
            self.item2_field2.setText("")
        except ValueError:
            print(ValueError)
            self.show_warning()

    def update_item3(self):
        price = self.item3_field.text().strip()
        stock = self.item3_field2.text().strip()

        # Check if price and stock are valid numbers
        try:
            price = float(price)  # Convert price to float
            stock = int(stock)    # Convert stock to integer
            self.crud.update_price(3, "gallon", stock, price)
            self.item3_field.setPlaceholderText(f"Price: {price}")
            self.item3_field2.setPlaceholderText(f"Stock: {stock}")
            self.item3_field.setText("")
            self.item3_field2.setText("")
        except ValueError:
            self.show_warning()