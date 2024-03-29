import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from loginUi4 import Ui_Form as Login # Assuming your UI code is in a file named loginUi4.py
from register import Ui_Form as Register # Assuming your UI code is in a file named loginUi4.py
from staff import Ui_MainWindow as Staff
from admin import Ui_MainWindow as Admin


class RegisterForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Register()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.goToLogin)
        self.ui.label_5.mousePressEvent = self.goToLogin

    def goToLogin(self, event):  # No need for event parameter
        self.hide()  # Hide current window
        login_window = MainForm()  # Assuming LoginForm is the login window class
        login_window.show()


class MainForm(QMainWindow):  # Change QWidget to QMainWindow
    def __init__(self):
        super().__init__()
        self.ui = Login()
        self.ui.setupUi(self)

        # Connect the clicked signal of self.pushButton to the login method
        self.ui.pushButton.clicked.connect(self.login)
        self.ui.label_5.mousePressEvent = self.goToRegister

    def goToStaff(self):
        self.hide()  # Hide current window
        staff_window = StaffWindow()  # Assuming RegisterForm is the registration window class
        staff_window.show()

    def goToAdmin(self):
        self.hide()  # Hide current window
        admin_window = AdminWindow()  # Assuming RegisterForm is the registration window class
        admin_window.show()

    def goToRegister(self, event):  
        self.hide()  # Hide current window
        register_window = RegisterForm()  # Assuming RegisterForm is the registration window class
        register_window.show()


    def login(self):
        username = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        # Here you can implement your login logic
        # For example, if username and password are correct, switch to Staff interface
        if username == "admin" and password == "admin":
            self.goToAdmin()
        elif username == "staff" and password == "staff":
            self.goToStaff()
        else:
            pass


class StaffWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Staff()
        self.ui.setupUi(self)
        self.ui.pushButton.mousePressEvent = self.goToLogin

    def goToLogin(self, event):  # No need for event parameter
        self.hide()  # Hide current window
        login_window = MainForm()  # Assuming LoginForm is the login window class
        login_window.show()


class AdminWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Admin()
        self.ui.setupUi(self)
        self.ui.pushButton.mousePressEvent = self.goToLogin

    def goToLogin(self, event):  # No need for event parameter
        self.hide()  # Hide current window
        login_window = MainForm()  # Assuming LoginForm is the login window class
        login_window.show()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainForm()
    mainWindow.show()
    sys.exit(app.exec_())