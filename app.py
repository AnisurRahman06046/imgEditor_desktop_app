# from PyQt6.QtWidgets import QApplication,QWidget,QVBoxLayout,QHBoxLayout,QPushButton,QLabel,QStackedWidget,QMainWindow
# from PyQt6.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("NavBar")
        
#         main_layout = QVBoxLayout()
#         navb = QHBoxLayout()
#         navb.setSpacing(20)
        
#         # add btns to navbar
#         self.homeBtn = QPushButton("Home")
#         self.aboutBtn = QPushButton("About")
#         self.contactBtn = QPushButton("Contact")
        
        
#         # style navbar
#         self.homeBtn.setStyleSheet("QPushButton {padding:10px;font-size:16px}")
#         self.contactBtn.setStyleSheet("QPushButton {padding:10px;font-size:16px}")
#         self.aboutBtn.setStyleSheet("QPushButton {padding:10px;font-size:16px}")
        
#         # navbar container
#         nav_container = QWidget()
#         nav_container.setLayout(navb)
#         nav_container.setStyleSheet("background-color: #007BFF; color: white; padding: 10px;")
        
        
#         self.pages = QStackedWidget()
#         self.pages.addWidget(self.create_page("Home"))
#         self.pages.addWidget(self.create_page("About"))
#         self.pages.addWidget(self.create_page("Contact"))
        
#         # connect the btn
#         self.homeBtn.clicked.connect(lambda:self.pages.setCurrentIndex(0))
#         self.aboutBtn.clicked.connect(lambda:self.pages.setCurrentIndex(1))
#         self.contactBtn.clicked.connect(lambda:self.pages.setCurrentIndex(2))
        
#         # add widget to main layout
#         main_layout.addWidget(nav_container)
#         main_layout.addWidget(self.pages)
        
#         # main widget
#         main_widget = QWidget()
#         main_widget.setLayout(main_layout)
#         self.setCentralWidget(main_widget)
    
#     def create_page(self,text):
#         page = QWidget()
#         layout = QVBoxLayout()
#         label = QLabel(text)
#         label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(label)
#         page.setLayout(layout)
#         return page 
    
    
# if __name__ in "__main__":
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec()
        
        
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QStackedWidget
)
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop App with Navbar")

        # Main layout
        main_layout = QVBoxLayout()
        
        # Navbar
        navbar = QHBoxLayout()
        navbar.setSpacing(20)

        # Add buttons to navbar
        self.home_btn = QPushButton("Home")
        self.profile_btn = QPushButton("Profile")
        self.settings_btn = QPushButton("Settings")

        # Style the navbar
        self.home_btn.setStyleSheet("padding: 10px; font-size: 16px;")
        self.profile_btn.setStyleSheet("padding: 10px; font-size: 16px;")
        self.settings_btn.setStyleSheet("padding: 10px; font-size: 16px;")

        navbar.addWidget(self.home_btn)
        navbar.addWidget(self.profile_btn)
        navbar.addWidget(self.settings_btn)

        # Navbar container
        navbar_container = QWidget()
        navbar_container.setLayout(navbar)
        navbar_container.setStyleSheet("background-color: #007BFF; color: white; padding: 10px;")

        # Stacked widget for pages
        self.pages = QStackedWidget()
        self.pages.addWidget(self.create_page("Home Page"))
        self.pages.addWidget(self.create_page("Profile Page"))
        self.pages.addWidget(self.create_page("Settings Page"))

        # Connect buttons to change pages
        self.home_btn.clicked.connect(lambda: self.pages.setCurrentIndex(0))
        self.profile_btn.clicked.connect(lambda: self.pages.setCurrentIndex(1))
        self.settings_btn.clicked.connect(lambda: self.pages.setCurrentIndex(2))

        # Add widgets to main layout
        main_layout.addWidget(navbar_container)
        main_layout.addWidget(self.pages)

        # Main widget
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def create_page(self, text):
        """Create a simple page with a label."""
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        page.setLayout(layout)
        return page

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
