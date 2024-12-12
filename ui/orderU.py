from PyQt5 import QtCore, QtGui, QtWidgets

class OrderU(QtWidgets.QWidget):
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

        # Scrollable Table Widget
        self.table = QtWidgets.QTableWidget(self)
        self.table.setGeometry(350, 140, 900, 500)  # Position and size
        self.table.setColumnCount(9)  # Set number of columns

        # Set column headers
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Number", "Address", "Item", "Price", "Quantity", "Total Price", "Confirmed"])
        self.table.setColumnHidden(0, True)

        self.table.setFont(QtGui.QFont("Poppins", 12))
        self.table.horizontalHeader().setStyleSheet("font: 12pt 'Poppins';")

        # Set appearance
        self.table.setAlternatingRowColors(True)
        self.table.setStyleSheet("""
            alternate-background-color: #f2f2f2; 
            background-color: #ffffff; 
            border: 2px solid #000;
            border-radius: 10px;
        """)
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)  # Stretch columns to fit

        self.apply_button = QtWidgets.QPushButton("Apply", self)
        self.apply_button.setFont(QtGui.QFont("Poppins", 12))
        self.apply_button.setGeometry(1050, 650, 200, 70)
        self.apply_button.setStyleSheet("""
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
        self.apply_button.clicked.connect(self.apply_changes)

        # Populate the table
        customers = self.home.crud.read_customers()
        self.table.setRowCount(len(customers))  # Set the number of rows

        for row_index, user in enumerate(customers):
            # Assuming `user` is a dictionary with keys matching the column headers
            self.table.setItem(row_index, 0, QtWidgets.QTableWidgetItem(str(user["id"])))
            self.table.setItem(row_index, 1, QtWidgets.QTableWidgetItem(user["name"]))
            self.table.setItem(row_index, 2, QtWidgets.QTableWidgetItem(user["number"]))
            self.table.setItem(row_index, 3, QtWidgets.QTableWidgetItem(user["address"]))
            self.table.setItem(row_index, 4, QtWidgets.QTableWidgetItem(user["item_name"]))
            self.table.setItem(row_index, 5, QtWidgets.QTableWidgetItem(str(user["item_price"])))
            self.table.setItem(row_index, 6, QtWidgets.QTableWidgetItem(str(user["item_number"])))
            self.table.setItem(row_index, 7, QtWidgets.QTableWidgetItem(str(user["item_price"] * user["item_number"])))

            for col_index in range(8):  # Iterate through columns 0 to 7
                item = self.table.item(row_index, col_index)
                if item:
                    item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
            
            #  Add a checkbox to the "Confirmed" column
            checkbox = QtWidgets.QCheckBox()
            checkbox.setChecked(user["confirmed"])  # Directly use the boolean value
            checkbox_widget = QtWidgets.QWidget()
            layout = QtWidgets.QHBoxLayout(checkbox_widget)
            layout.addWidget(checkbox)
            layout.setAlignment(QtCore.Qt.AlignCenter)  # Center-align the checkbox
            layout.setContentsMargins(0, 0, 0, 0)
            self.table.setCellWidget(row_index, 8, checkbox_widget)

    def center_window(self):
        # Get screen geometry
        screen = QtWidgets.QApplication.primaryScreen().geometry()
        x = (screen.width() - self.width()) // 2
        y = (screen.height() - self.height()) // 2
        self.move(x, y)

    def open_home(self):
        self.home.show()  # Show the Home window
        self.close()

    def apply_changes(self):
        for row_index in range(self.table.rowCount()):
            customer_id = int(self.table.item(row_index, 0).text())
            name = self.table.item(row_index, 1).text()
            number = self.table.item(row_index, 2).text()
            address = self.table.item(row_index, 3).text()
            item_name = self.table.item(row_index, 4).text()
            item_price = float(self.table.item(row_index, 5).text())
            item_number = int(self.table.item(row_index, 6).text())
            total_price = item_price * item_number
            checkbox_widget = self.table.cellWidget(row_index, 8)
            checkbox = checkbox_widget.layout().itemAt(0).widget()
            confirmed = checkbox.isChecked()

            # Update the customer in the database
            self.home.crud.update_customer(customer_id, name, number, address, item_name, item_price, item_number, confirmed)
