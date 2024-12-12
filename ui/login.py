from PyQt5 import QtWidgets, QtGui, QtCore

class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.is_admin = False

        # Set up the window
        self.setWindowTitle("Genesys")
        self.setFixedSize(400, 500)
        self.setStyleSheet("background-image: url('res/Water.jpg');")

        # Create widgets
        self.title_label = QtWidgets.QLabel("Genesys", self)
        self.title_label.setFont(QtGui.QFont("Poppins", 36))
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setGeometry(50, 50, 300, 60)
        self.title_label.setStyleSheet("color: blue; background: transparent;")

        self.username_field = QtWidgets.QLineEdit(self)
        self.username_field.setPlaceholderText("User Name")
        self.username_field.setFont(QtGui.QFont("Poppins", 12))
        self.username_field.setGeometry(100, 150, 200, 30)
        self.username_field.setStyleSheet("padding-left: 10px;")

        self.password_field = QtWidgets.QLineEdit(self)
        self.password_field.setPlaceholderText("Password")
        self.password_field.setFont(QtGui.QFont("Poppins", 12))
        self.password_field.setGeometry(100, 200, 200, 30)
        self.password_field.setStyleSheet("padding-left: 10px;")
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)

        self.user_button = QtWidgets.QPushButton("Admin", self)
        self.user_button.setFont(QtGui.QFont("Poppins", 12))
        self.user_button.setGeometry(100, 250, 200, 30)
        self.user_button.clicked.connect(self.toggle_interface)

        self.admin_button = QtWidgets.QPushButton("Login", self)
        self.admin_button.setFont(QtGui.QFont("Poppins", 12))
        self.admin_button.setGeometry(100, 300, 200, 30)
        self.admin_button.clicked.connect(self.handle_login)

        self.message_label = QtWidgets.QLabel("", self)
        self.message_label.setFont(QtGui.QFont("Poppins", 12))
        self.message_label.setStyleSheet("color: red; background: transparent;")
        self.message_label.setAlignment(QtCore.Qt.AlignCenter)
        self.message_label.setGeometry(25, 350, 350, 20)

    def toggle_interface(self):
        self.is_admin = not self.is_admin
        if self.is_admin:
            self.user_button.setText("User")
            self.admin_button.setText("Login as Admin")
            self.username_field.setPlaceholderText("Admin Name")
        else:
            self.user_button.setText("Admin")
            self.admin_button.setText("Login")
            self.username_field.setPlaceholderText("User Name")

    def handle_login(self):
        username = self.username_field.text().strip()
        password = self.password_field.text()

        if self.is_admin:
            if username == "admin" and password == "password":
                self.message_label.setText("")
                self.show_message("Admin logged in successfully.")
            else:
                self.message_label.setText("Wrong username or password!")
        else:
            if username == "user" and password == "password":
                self.message_label.setText("")
                self.show_message("User logged in successfully.")
            else:
                self.message_label.setText("Wrong username or password!")

    def show_message(self, message):
        QtWidgets.QMessageBox.information(self, "Login", message)