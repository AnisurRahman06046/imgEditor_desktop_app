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
        
        
# import sys
# from PyQt6.QtWidgets import (
#     QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QStackedWidget
# )
# from PyQt6.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Desktop App with Navbar")

#         # Main layout
#         main_layout = QVBoxLayout()
        
#         # Navbar
#         navbar = QHBoxLayout()
#         navbar.setSpacing(20)

#         # Add buttons to navbar
#         self.home_btn = QPushButton("Home")
#         self.profile_btn = QPushButton("Profile")
#         self.settings_btn = QPushButton("Settings")

#         # Style the navbar
#         self.home_btn.setStyleSheet("padding: 10px; font-size: 16px;")
#         self.profile_btn.setStyleSheet("padding: 10px; font-size: 16px;")
#         self.settings_btn.setStyleSheet("padding: 10px; font-size: 16px;")

#         navbar.addWidget(self.home_btn)
#         navbar.addWidget(self.profile_btn)
#         navbar.addWidget(self.settings_btn)

#         # Navbar container
#         navbar_container = QWidget()
#         navbar_container.setLayout(navbar)
#         navbar_container.setStyleSheet("background-color: #007BFF; color: white; padding: 10px;")

#         # Stacked widget for pages
#         self.pages = QStackedWidget()
#         self.pages.addWidget(self.create_page("Home Page"))
#         self.pages.addWidget(self.create_page("Profile Page"))
#         self.pages.addWidget(self.create_page("Settings Page"))

#         # Connect buttons to change pages
#         self.home_btn.clicked.connect(lambda: self.pages.setCurrentIndex(0))
#         self.profile_btn.clicked.connect(lambda: self.pages.setCurrentIndex(1))
#         self.settings_btn.clicked.connect(lambda: self.pages.setCurrentIndex(2))

#         # Add widgets to main layout
#         main_layout.addWidget(navbar_container)
#         main_layout.addWidget(self.pages)

#         # Main widget
#         main_widget = QWidget()
#         main_widget.setLayout(main_layout)
#         self.setCentralWidget(main_widget)

#     def create_page(self, text):
#         """Create a simple page with a label."""
#         page = QWidget()
#         layout = QVBoxLayout()
#         label = QLabel(text)
#         label.setAlignment(Qt.AlignmentFlag.AlignCenter)
#         layout.addWidget(label)
#         page.setLayout(layout)
#         return page

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.resize(800, 600)
#     window.show()
#     sys.exit(app.exec())




import sys 
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QWidget, QStackedWidget, QSpacerItem, QSizePolicy
from PyQt6.QtGui import QIcon ,QPixmap # Correct import for QIcon
from PyQt6.QtCore import Qt 

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Base App")
        # self.resize(800,600)
        self.resize(1480,680)

        # navbar layout
        navBar = QHBoxLayout()  # QHBoxLayout to arrange the buttons horizontally

        # Left side: Logo + Navigation buttons
        left_nav = QHBoxLayout()
        # logo_label = QLabel("LOGO")  # Placeholder for your logo
        logo_label= QLabel()
        pixmp_logo = QPixmap("assets/logo.jpg")
        logo_label.setStyleSheet("font-size: 20px; font-weight: bold; padding-right: 20px")
        logo_label.setPixmap(pixmp_logo.scaled(100,100,Qt.AspectRatioMode.KeepAspectRatio,Qt.TransformationMode.SmoothTransformation))
        logo_label.setStyleSheet("padding-right:20px")
        left_nav.addWidget(logo_label)

        # creating the navigation buttons
        self.homeBtn = QPushButton("Home")
        self.ordersBtn = QPushButton("Orders")
        self.postBtn = QPushButton("POS Terminal")
        self.productsBtn = QPushButton("Products")
        self.customerBtn = QPushButton("Customers")
        self.staffBtn = QPushButton("Staff")
        self.settingBtn = QPushButton("Settings")

        # design buttons
        btn_style = "padding:10px;font-size:25px;border:none;color:black"
        self.homeBtn.setStyleSheet(btn_style)
        self.ordersBtn.setStyleSheet(btn_style)
        self.postBtn.setStyleSheet(btn_style)
        self.productsBtn.setStyleSheet(btn_style)
        self.customerBtn.setStyleSheet(btn_style)
        self.staffBtn.setStyleSheet(btn_style)
        self.settingBtn.setStyleSheet(btn_style)

        # adding the buttons to the left navigation
        left_nav.addWidget(self.homeBtn)
        left_nav.addWidget(self.ordersBtn)
        left_nav.addWidget(self.postBtn)
        left_nav.addWidget(self.productsBtn)
        left_nav.addWidget(self.customerBtn)
        left_nav.addWidget(self.staffBtn)
        left_nav.addWidget(self.settingBtn)

        # Add spacer to push items to the right
        left_nav.addSpacerItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        # Right side: Profile logo + Settings button
        right_nav = QHBoxLayout()
        
        # Profile logo (as an icon or text placeholder)
        profile_logo = QLabel("UserName")  
        profile_logo.setStyleSheet("font-size: 20px; padding-right: 10px")
        right_nav.addWidget(profile_logo)
        
        # Settings button
        self.prflBtn = QPushButton()
        profilePix = QPixmap("assets/profile.png")
        profilePix = profilePix.scaled(40, 40, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.prflBtn.setIcon(QIcon(profilePix))
        self.prflBtn.setIconSize(profilePix.size())
        
        self.prflBtn.setStyleSheet(btn_style)  # Apply the same button style as others
        right_nav.addWidget(self.prflBtn)

        # Add the left and right sections to the navbar
        navBar.addLayout(left_nav)
        navBar.addLayout(right_nav)

        # wrapping the navbar in a container
        nav_container = QWidget()
        nav_container.setLayout(navBar)
        nav_container.setStyleSheet("background-color:#FFFFFF; padding:10px")

        # creating pages
        # QStackedWidget : to manage multiple pages, switching between them
        self.pages = QStackedWidget()  # initialized the StackWidget
        pagesTextList = ["Home Page", "PosTerminal page", "Orders Page", "Products page", "Customer page", "Staff Page","Setting page","Profile"]

        for c in pagesTextList:
            self.pages.addWidget(self.create_page(c))

        self.homeBtn.clicked.connect(lambda: self.pages.setCurrentIndex(0))
        self.ordersBtn.clicked.connect(lambda: self.pages.setCurrentIndex(1))
        self.postBtn.clicked.connect(lambda: self.pages.setCurrentIndex(2))
        self.productsBtn.clicked.connect(lambda: self.pages.setCurrentIndex(3))
        self.customerBtn.clicked.connect(lambda: self.pages.setCurrentIndex(4))
        self.staffBtn.clicked.connect(lambda: self.pages.setCurrentIndex(5))
        self.settingBtn.clicked.connect(lambda: self.pages.setCurrentIndex(6))
        self.prflBtn.clicked.connect(lambda:self.pages.setCurrentIndex(7))

        # combine navbar and pages into a single layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(nav_container)
        main_layout.addWidget(self.pages)

        # final layout
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        self.setStyleSheet("background-color:#e6e7e7")

    # method to generate pages dynamically
    def create_page(self, text):
        page = QWidget()
        layout = QVBoxLayout()
        label = QLabel(text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)
        page.setLayout(layout)
        return page

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
