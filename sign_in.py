
# Interfejs do logowania na stronie + panel sterujący zalogowanego użytkownika

# Importy

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QLineEdit, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtCore import Qt
import sys
import sign_in_selenium
import sign_out_selenium
from user_panel_window import UserPanel

class SuccessfullSignOut(QDialog):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Komunikat ze strony wszystkozkotami.pl")
        self.setFixedSize(500, 500)
        self.setWindowIcon(QIcon("logo.png"))
        layout = QVBoxLayout()

        message = QLabel(
            '<div style="text-align:center">'
            '<span style="font-size:16pt;">Do zobaczenia!<br>'
            '<span style="font-size:14pt;color:#e91e63;">Nastąpiło poprawne wylogowanie<br>'
            '</span>'
            '</div>'
        )
        font = QFont()
        font.setPointSize(14)
        message.setFont(font)
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message.setContentsMargins(0, 20, 0, 20)
        layout.addWidget(message)

        logo = QLabel()
        pixmap = QPixmap("logo.png")
        logo.setPixmap(pixmap.scaledToWidth(200, Qt.TransformationMode.SmoothTransformation))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setContentsMargins(0, -10, 0, 65)
        layout.addWidget(logo)

        button_layout = QHBoxLayout()
        self.sign_in_again_button = QPushButton("Zaloguj ponownie")
        self.sign_in_again_button.setStyleSheet("""
                                   QPushButton {
                                       background-color: #e91e63;
                                       color: white;
                                       border-radius: 8px;
                                       padding: 8px;
                                       font-weight: bold;
                                   }
                                   QPushButton:hover {
                                       background-color: #d81b60;
                                   }
                               """)
        self.exit_button = QPushButton("Zakończ")
        self.exit_button.setStyleSheet("""
                                    QPushButton {
                                        background-color: #D3D3D3;
                                        color: black;
                                        border-radius: 8px;
                                        padding: 8px;
                                    }
                                    QPushButton:hover {
                                        background-color: #C0C0C0;
                                    }
                                """)
        font = QFont()
        font.setPointSize(13)
        self.sign_in_again_button.setFont(font)
        self.exit_button.setFont(font)
        self.sign_in_again_button.clicked.connect(self.retry_sign_in)
        self.exit_button.clicked.connect(self.quit_app)
        button_layout.addWidget(self.sign_in_again_button)
        button_layout.addWidget(self.exit_button)
        layout.addLayout(button_layout)
        self.setLayout(layout)

    def retry_sign_in(self):
        self.close()
        app = QApplication.instance()
        app.sign_in_window = SignInWindow()
        app.sign_in_window.show()

    def quit_app(self):
        self.close()
        sys.exit()

class SuccessfulSignIn(QDialog):

    def __init__(self, driver, user_email, sign_in_window=None):
        super().__init__()
        self.driver = driver
        self.user_email = user_email
        self.sign_in_window = sign_in_window
        self.setWindowTitle("Poprawne logowanie użytkownika")
        self.setFixedSize(500, 500)
        self.setWindowIcon(QIcon("logo.png"))
        layout = QVBoxLayout()

        message = QLabel(
            '<div style="text-align:center">'
            '<span style="font-size:16pt;">Jesteś zalogowany<br>'
            '<span style="font-size:14pt;color:#e91e63;">Rozpocznij korzystanie z serwisu<br>'
            '</span>'
            '</div>'
        )
        font = QFont()
        font.setPointSize(14)
        message.setFont(font)
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message.setContentsMargins(0, 20, 0, 20)
        layout.addWidget(message)

        logo = QLabel()
        pixmap = QPixmap("logo.png")
        logo.setPixmap(pixmap.scaledToWidth(200, Qt.TransformationMode.SmoothTransformation))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setContentsMargins(0, -10, 0, 65)
        layout.addWidget(logo)

        button_layout = QHBoxLayout()
        self.user_panel_button = QPushButton("Panel użytkownika")
        self.user_panel_button.setStyleSheet("""
                                   QPushButton {
                                       background-color: #e91e63;
                                       color: white;
                                       border-radius: 8px;
                                       padding: 8px;
                                       font-weight: bold;
                                   }
                                   QPushButton:hover {
                                       background-color: #d81b60;
                                   }
                               """)
        self.sign_out_button = QPushButton("Wyloguj")
        self.sign_out_button.setStyleSheet("""
                                    QPushButton {
                                        background-color: #D3D3D3;
                                        color: black;
                                        border-radius: 8px;
                                        padding: 8px;
                                    }
                                    QPushButton:hover {
                                        background-color: #C0C0C0;
                                    }
                                """)
        font = QFont()
        font.setPointSize(13)
        self.user_panel_button.setFont(font)
        self.sign_out_button.setFont(font)
        self.user_panel_button.clicked.connect(self.user_panel_open)
        self.sign_out_button.clicked.connect(self.sign_out)
        button_layout.addWidget(self.user_panel_button)
        button_layout.addWidget(self.sign_out_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def user_panel_open(self):
        self.hide()
        #app = QApplication.instance()
        self.user_panel = UserPanel(self.user_email, self.driver, sign_in_window=self.sign_in_window)
        self.user_panel.show()

    def sign_out(self):
        self.close()
        success = sign_out_selenium.run_sign_out(self.driver)
        if success and self.sign_in_window:
            self.sign_in_window.show()
        else:
            dialog = SignOutFailed()
            dialog.exec()

class SignInFailed(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Logowanie nie powiodło się")
        self.setFixedSize(500, 500)
        self.setWindowIcon(QIcon("logo.png"))
        layout = QVBoxLayout()

        message = QLabel(
            '<div style="text-align:center">'
            '<span style="font-size:16pt;">Logowanie nie powiodło się<br>'
            '<span style="font-size:13pt;color:#e91e63;">Sprawdź poprawność wprowadzonych<br>'
            'danych i spróbuj ponownie.</span>'
            '</span>'
            '</div>'
        )
        font = QFont()
        font.setPointSize(14)
        message.setFont(font)
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message.setContentsMargins(0, 20, 0, 20)
        layout.addWidget(message)

        logo = QLabel()
        pixmap = QPixmap("logo.png")
        logo.setPixmap(pixmap.scaledToWidth(200, Qt.TransformationMode.SmoothTransformation))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setContentsMargins(0, -10, 0, 65)
        layout.addWidget(logo)

        button_layout = QHBoxLayout()
        self.try_again_button = QPushButton("Spróbuj ponownie")
        self.try_again_button.setStyleSheet("""
                                   QPushButton {
                                       background-color: #e91e63;
                                       color: white;
                                       border-radius: 8px;
                                       padding: 8px;
                                       font-weight: bold;
                                   }
                                   QPushButton:hover {
                                       background-color: #d81b60;
                                   }
                               """)
        self.later_button = QPushButton("Nie teraz")
        self.later_button.setStyleSheet("""
                                    QPushButton {
                                        background-color: #D3D3D3;
                                        color: black;
                                        border-radius: 8px;
                                        padding: 8px;
                                    }
                                    QPushButton:hover {
                                        background-color: #C0C0C0;
                                    }
                                """)
        font = QFont()
        font.setPointSize(13)
        self.try_again_button.setFont(font)
        self.later_button.setFont(font)
        self.try_again_button.clicked.connect(self.retry_sign_in)
        self.later_button.clicked.connect(self.quit_app)
        button_layout.addWidget(self.try_again_button)
        button_layout.addWidget(self.later_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def retry_sign_in(self):
        self.close()
        app = QApplication.instance()
        app.sign_in_window = SignInWindow()
        app.sign_in_window.show()

    def quit_app(self):
        self.close()
        sys.exit()
class SignInWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Zaloguj się na stronie wszystkozkotami.pl")
        self.setFixedSize(500, 500)
        self.setWindowIcon(QIcon("logo.png"))
        self.user_data = {
            "user_email": "",
            "user_password": ""
        }

        central_widget = QWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        message = QLabel(
            '<div style="text-align:center">'
            '<span style="font-size:16pt;">Witaj miłośniku kotów!<br>'
            '<span style="font-size:13pt;color:#e91e63;">Wprowadź dane poniżej, aby zalogować się na swoje konto.'
            '</span>'
            '</div>'
        )
        font = QFont()
        font.setPointSize(14)
        message.setFont(font)
        message.setAlignment(Qt.AlignmentFlag.AlignCenter)
        message.setContentsMargins(0, 20, 0, 20)
        main_layout.addWidget(message)

        logo = QLabel()
        pixmap = QPixmap("logo.png")
        logo.setPixmap(pixmap.scaledToWidth(190, Qt.TransformationMode.SmoothTransformation))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setContentsMargins(0, 0, 0, 28)
        main_layout.addWidget(logo)

        # Pole: Email
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Podaj adres e-mail")
        self.email_input.setFixedSize(300, 30)
        email_row = QHBoxLayout()
        email_row.addStretch()
        email_row.addWidget(self.email_input)
        email_row.addStretch()
        main_layout.addLayout(email_row)
        main_layout.addSpacing(10)

        # Pole: Hasło
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Podaj hasło")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedSize(300, 30)
        password_row = QHBoxLayout()
        password_row.addStretch()
        password_row.addWidget(self.password_input)
        password_row.addStretch()
        main_layout.addLayout(password_row)

        main_layout.addStretch()

        # Przycisk logowania

        button_layout = QHBoxLayout()
        self.sign_in_button = QPushButton("Zaloguj się")
        self.sign_in_button.setStyleSheet("""
                            QPushButton {
                                background-color: #e91e63;
                                color: white;
                                border-radius: 8px;
                                padding: 8px;
                                font-weight: bold;
                            }
                            QPushButton:hover {
                                background-color: #d81b60;
                            }
                        """)
        self.exit_button = QPushButton("Wyjdź")
        self.exit_button.setStyleSheet("""
                                    QPushButton {
                                        background-color: #D3D3D3;
                                        color: black;
                                        border-radius: 8px;
                                        padding: 8px;
                                    }
                                    QPushButton:hover {
                                        background-color: #C0C0C0;
                                    }
                                """)
        font = QFont()
        font.setPointSize(13)
        self.sign_in_button.setFont(font)
        self.exit_button.setFont(font)
        self.sign_in_button.clicked.connect(self.sign_in)
        self.exit_button.clicked.connect(self.close)
        button_layout.addWidget(self.sign_in_button)
        button_layout.addWidget(self.exit_button)

        self.sign_in_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.exit_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def sign_in(self):
        user_email = self.email_input.text()
        user_password = self.password_input.text()
        driver = sign_in_selenium.run_sign_in(user_email, user_password)
        if driver:
            self.close()
            dialog = SuccessfulSignIn(driver, user_email, sign_in_window=self)
            dialog.exec()

        else:
            dialog = SignInFailed()
            dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignInWindow()
    window.show()
    sys.exit(app.exec())


