
# Panel użytkownika dostępny po zalogowaniu (umożliwia nawigację po stronie sklepu internetowego)

# Importy

from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout,
    QWidget, QMenu, QPushButton, QToolButton, QSizePolicy
)
from PyQt6.QtGui import QFont, QPixmap, QIcon
from PyQt6.QtCore import Qt
import sys
from user_panel_selenium import handle_navigation
from sign_out_selenium import run_sign_out

class UserPanel(QMainWindow):
    def __init__(self, user_email, driver, sign_in_window=None):
        super().__init__()
        self.user_email = user_email
        self.driver = driver
        self.sign_in_window = sign_in_window
        self.setWindowTitle("Panel użytkownika")
        self.setFixedSize(500, 500)
        self.setWindowIcon(QIcon("logo.png"))

        central_widget = QWidget()
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)

        # Powitanie
        welcome_label = QLabel(
            f'<div style="text-align:center">'
            f'<span style="font-size:16pt;">Witaj, {user_email}!<br>'
            f'<span style="font-size:16pt;color:#e91e63;">Miło Cię widzieć!</span>'
            f'</span>'
            f'</div>'
        )
        font = QFont()
        font.setPointSize(14)
        welcome_label.setFont(font)
        welcome_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        welcome_label.setContentsMargins(0, 20, 0, 20)
        main_layout.addWidget(welcome_label)

        # Logo
        logo = QLabel()
        pixmap = QPixmap("logo.png")
        logo.setPixmap(pixmap.scaledToWidth(190, Qt.TransformationMode.SmoothTransformation))
        logo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        logo.setContentsMargins(0, 0, 0, 40)
        main_layout.addWidget(logo)

        # Etykiety/menu
        menu_layout = QVBoxLayout()

        row1 = QHBoxLayout()
        row2 = QHBoxLayout()

        row1.addWidget(self.create_menu_button("Strona główna"))
        row1.addWidget(self.create_menu_button("Kategorie", ["Dom", "Dziecko", "Moda", "Nowości"]))
        row1.addWidget(self.create_menu_button("Twoje konto", ["Ulubione", "Twoje zamówienia", "Ustawienia konta", "Wyloguj"]))

        row2.addWidget(self.create_menu_button("Obsługa klienta", ["Płatności", "Dostawa", "Zwroty i reklamacje"]))
        row2.addWidget(self.create_menu_button("Pomoc", ["Pytania i odpowiedzi", "Regulamin", "Polityka prywatności"]))
        row2.addWidget(self.create_menu_button("Więcej", ["Blog", "Kontakt", "O nas", "Jak pomagamy kotom?"]))

        menu_layout.addLayout(row1)
        menu_layout.addLayout(row2)
        main_layout.addLayout(menu_layout)

    def create_menu_button(self, label, submenu_items=None):
        button = QToolButton()
        button.setText(label)
        button.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        button.setFont(QFont("Arial", 12))
        button.setStyleSheet("""
            QToolButton {
                background-color: #e91e63;
                color: white;
                border-radius: 6px;
                padding: 10px;
            }
            QToolButton:hover {
                background-color: #d81b60;
            }
        """)
        button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)

        if not submenu_items:
            button.clicked.connect(lambda: self.handle_navigation(label))
        else:
            menu = QMenu()
            for item in submenu_items:
                action = menu.addAction(item)
                action.triggered.connect(lambda checked=False, item=item: self.handle_navigation(item))
            button.setMenu(menu)
            return button

    def handle_logout(self):
        from sign_in import SuccessfullSignOut
        self.close()
        if self.driver:
            success = run_sign_out(self.driver)
            self.driver.quit()

        dialog = SuccessfullSignOut()
        dialog.exec()

    def handle_navigation(self, label):
        if label == "Wyloguj":
            self.handle_logout()
            return
        result = handle_navigation(self.driver, label)
        if result == "exit":
            self.handle_logout()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserPanel(user_email)
    window.show()
    sys.exit(app.exec())