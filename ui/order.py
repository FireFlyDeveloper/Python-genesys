from PyQt5 import QtCore, QtGui, QtWidgets

class Order(QtWidgets.QWidget):
    def __init__(self, home):
        super().__init__()

        self.home = home

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
        self.dashboard_button.clicked.connect(self.open_home)

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

    def center_window(self):
        # Get screen geometry
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def open_home(self):
        self.home.show()  # Show the Home window
        self.close()