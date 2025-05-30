
# Interfejs do rejestrowania nowego użytkownika na stronie

# Importy

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QLineEdit, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtCore import Qt
import sys
import sign_up_selenium
from sign_in import SignInWindow

class AccountCreated(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rejestracja przebiegła pomyślnie")
        self.setFixedSize(500, 500)
        self.setWindowIcon(QIcon("logo.png"))
        layout = QVBoxLayout()

        message = QLabel(
            '<div style="text-align:center">'
            '<span style="font-size:16pt;">Twoje konto zostało utworzone.<br>'
            '<span style="font-size:13pt;color:#e91e63;">W celu ukończenia rejestracji sprawdź pocztę<br>'
            'i kliknij w link potwierdzający.</span>'
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
        self.confirm_button = QPushButton("Rejestracja potwierdzona")
        self.confirm_button.setStyleSheet("""
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
        self.confirm_button.setFont(font)
        self.later_button.setFont(font)
        self.confirm_button.clicked.connect(self.open_sign_in_window)
        self.later_button.clicked.connect(self.quit_app)
        button_layout.addWidget(self.confirm_button)
        button_layout.addWidget(self.later_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def open_sign_in_window(self):
        self.close()
        app = QApplication.instance()
        app.sign_in_window = SignInWindow()
        app.sign_in_window.show()

    def quit_app(self):
        self.close()
        sys.exit()

class AccountCreationFailed(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rejestracja użytkownika nie powiodła się")
        self.setFixedSize(500, 500)
        self.setWindowIcon(QIcon("logo.png"))
        layout = QVBoxLayout()

        message = QLabel(
            '<div style="text-align:center">'
            '<span style="font-size:16pt;">Twoje konto nie zostało utworzone.<br>'
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
        self.try_again_button.clicked.connect(self.retry_registration)
        self.later_button.clicked.connect(self.quit_app)
        button_layout.addWidget(self.try_again_button)
        button_layout.addWidget(self.later_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def retry_registration(self):
        self.close()
        app = QApplication.instance()
        app.registration_window = NewUserData()
        app.registration_window.show()

    def quit_app(self):
        self.close()
        sys.exit()

class NewUserData(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Rejestracja nowego użytkownika')
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
            '<span style="font-size:16pt;">Rejestracja nowego użytkownika<br>'
            '<span style="font-size:13pt;color:#e91e63;">Wprowadż poniżej poprawne dane,<br>'
            'w celu rejestracji konta.</span>'
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
        self.email_input.setPlaceholderText("Wpisz adres e-mail")
        self.email_input.setFixedSize(300, 30)
        email_row = QHBoxLayout()
        email_row.addStretch()
        email_row.addWidget(self.email_input)
        email_row.addStretch()
        main_layout.addLayout(email_row)
        main_layout.addSpacing(10)

        # Pole: Hasło
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Wpisz hasło (minimum 12 znaków)")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.setFixedSize(300, 30)
        password_row = QHBoxLayout()
        password_row.addStretch()
        password_row.addWidget(self.password_input)
        password_row.addStretch()
        main_layout.addLayout(password_row)

        main_layout.addStretch()

        # Przycisk rejestracji
        button_layout = QHBoxLayout()
        self.create_account_button = QPushButton("Utwórz konto")
        self.create_account_button.setStyleSheet("""
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
        self.return_button = QPushButton("Wróć")
        self.return_button.setStyleSheet("""
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
        self.create_account_button.setFont(font)
        self.return_button.setFont(font)
        self.create_account_button.clicked.connect(self.create_account)
        self.return_button.clicked.connect(self.go_back)
        button_layout.addWidget(self.create_account_button)
        button_layout.addWidget(self.return_button)

        self.create_account_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.return_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def create_account(self):
        user_email = self.email_input.text()
        user_password = self.password_input.text()
        self.close()
        success = sign_up_selenium.run(user_email, user_password)
        if success:
            dialog = AccountCreated()
        else:
            dialog = AccountCreationFailed()
        dialog.exec()
    def go_back(self):
        self.invitation_window = Invitation()
        self.invitation_window.show()
        self.close()
class Invitation(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Komunikat ze strony wszystkozkotami.pl')
        self.setFixedSize(500, 500)
        self.setWindowIcon(QIcon("logo.png"))
        layout = QVBoxLayout()

        label = QLabel(
            '<div style="text-align:center">'
            '<span style="font-size:16pt;">Witaj w kocim świecie!<br>'
            '<span style="color:#e91e63;">Zarejestruj się, aby odkryć wszystkie możliwości.'
            '</span>'
            '</div>'
        )
        font = QFont()
        font.setPointSize(13)
        label.setFont(font)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        logo = QLabel()
        pixmap = QPixmap("logo.png")
        logo.setPixmap(pixmap.scaledToWidth(200, Qt.TransformationMode.SmoothTransformation))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setContentsMargins(0, -10, 0, 50)
        layout.addWidget(logo)

        # Przycisk rejestracji
        button_layout = QHBoxLayout()
        self.register_button = QPushButton("Zarejestruj się")
        self.register_button.setStyleSheet("""
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
        self.close_button = QPushButton("Zamknij")
        self.close_button.setStyleSheet("""
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
        self.register_button.setFont(font)
        self.close_button.setFont(font)
        self.close_button.clicked.connect(self.close)
        self.register_button.clicked.connect(self.open_registration_window)
        button_layout.addWidget(self.register_button)
        button_layout.addWidget(self.close_button)


        self.register_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.close_button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def open_registration_window(self):
        self.registration_window = NewUserData()
        self.registration_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Invitation()
    window.show()
    app.exec()