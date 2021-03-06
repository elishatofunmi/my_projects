import sys
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from welcome import welcome




class Authenticate_admin(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.title = 'Admin login'
        self.button_status = False
        self.trigger_button = False
        self.setMaximumSize(700,500)
        self.dict_details = {'username': None, 'password': None, 'confirm_password': None}
        self.display_background()
        self.display_login_details()
        
       
    def display_background(self):
       self.setWindowTitle(self.title)
       self.width = 700
       self.height = 500
       self.top = 300
       self.left = 200

       self.label = QLabel(self)
       pixmap = QPixmap("all_background.PNG")
       self.label.setGeometry(0,0,self.width,self.height)
       self.label.setPixmap(pixmap)
       self.label.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
       self.label.setScaledContents(True)
       self.label.show()

       #self.setWindowIcon(QIcon('icon.png'))
       self.setGeometry(self.top, self.left,self.width, self.height)
        #return
        
    def get_admin_details(self):
       
       flie_open = open('admin_details.txt', 'r')
       read_data = flie_open.readlines()[0]
       data = read_data.split(',')
       flie_open.close()
       if data == '':
          sol = False
       else:
          sol = True
        
       return sol
    
   
    def get_my_admin_details(self):
       
       flie_open = open('admin_details.txt', 'r')
       read_data = flie_open.read()
       data = read_data
       flie_open.close()
       if data == '':
          sol = False
       else:
          sol = True
        
       return sol
        
        
        
    def display_login_details(self):
        self.setWindowTitle(self.title)
        
        #layout = QVBoxLayout()

        # display Username
        self.label_name = QLabel('Username:',self)
        self.label_name.move(90,150)
        self.label_name.resize(100,30)
       # layout.addWidget(self.label_name)


        # display entry box for name
        self.lineedit_name = QLineEdit('', self)
        self.lineedit_name.move(180,150)
        self.lineedit_name.resize(400,30)
        self.lineedit_name.setPlaceholderText("Enter your username")
        #layout.addWidget(self.lineedit_name)
        
        # display Rank/title
        self.rank_title = QLabel('Password:',self)
        self.rank_title.move(90,250)
        self.rank_title.resize(100,30)
       # layout.addWidget(self.rank_title)

        # display entry box for rank or title
        self.rank_title_edit = QLineEdit('', self)
        self.rank_title_edit.setEchoMode(PyQt5.QtWidgets.QLineEdit.Password)
        self.rank_title_edit.move(180,250)
        self.rank_title_edit.resize(400,30)
       # layout.addWidget(self.rank_title_edit)
        self.rank_title_edit.setPlaceholderText("Enter your password")
        
        try:
           
           if (self.get_my_admin_details() == False):
              # confirm password
              self.password_confirm = QLabel(' Confirm password:',self)
              self.password_confirm.move(70,350)
              self.password_confirm.resize(150,30)
              #layout.addWidget(self.password_confirm)


              #dispaly entrybox for confirming password
              self.password_conf = QLineEdit('',self)
              self.password_conf.setEchoMode(PyQt5.QtWidgets.QLineEdit.Password)
              self.password_conf.move(180,350)
              self.password_conf.resize(400,30)
              #layout.addWidget(self.password_conf)
              self.password_conf.setPlaceholderText("Enter to confirm password")
              
              
              self.click_to_login = QPushButton('login', self)
             # layout.addWidget(self.click_to_login)
              self.click_to_login.resize(200,30)
              self.click_to_login.move(150,410)
              self.click_to_login.setToolTip("save details")
              self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
              self.click_to_login.clicked.connect(self.log_details)
              
              self.click_to_cancel = QPushButton('close', self)
             # layout.addWidget(self.click_to_cancel)
              self.click_to_cancel.resize(200,30)
              self.click_to_cancel.move(400,410)
              self.click_to_cancel.setToolTip("close window")
              self.click_to_cancel.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
              self.click_to_cancel.clicked.connect(self.cancel_details)
              
              
              
              self.display_label = QLabel('',self)
             # layout.addWidget(self.display_label)
              self.display_label.resize(300,30)
              self.display_label.move(100,450)
           else:
              self.click_to_login = QPushButton('login', self)
             # layout.addWidget(self.click_to_login)
              self.click_to_login.resize(200,30)
              self.click_to_login.move(150,300)
              self.click_to_login.setToolTip("save details")
              self.click_to_login.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
              self.click_to_login.clicked.connect(self.log_details)
              
              self.click_to_cancel = QPushButton('close', self)
             # layout.addWidget(self.click_to_cancel)
              self.click_to_cancel.resize(200,30)
              self.click_to_cancel.move(400,300)
              self.click_to_cancel.setToolTip("close window")
              self.click_to_cancel.setStyleSheet('background-color:#4e4e4e;color:#f7f7f7;')
              self.click_to_cancel.clicked.connect(self.cancel_details)
              
              
              
              self.display_label = QLabel('',self)
             # layout.addWidget(self.display_label)
              self.display_label.resize(200,30)
              self.display_label.move(100,400)
              
         
        except IndexError:
           pass
        finally:
           pass
        
        
        

        #self.setLayout(layout)
        self.show()
        return
     
       
     
    def log_details(self):
       try:
          if self.get_admin_details() == True:
             if self.compare_details() == True:
                self.welcome_page = welcome()
                self.hide()
                self.welcome_page.show()
             else:
                pass
          else:
             self.save_details()
             self.welcome_page = welcome()
             self.hide()
             self.welcome_page.show()
       except IndexError:
          if self.get_my_admin_details() == True:
             if self.compare_details() == True:
                self.welcome_page = welcome()
                self.hide()
                self.welcome_page.show()
             else:
                pass
          else:
             self.save_details()
             self.welcome_page = welcome()
             self.hide()
             self.welcome_page.show()
                
       
       return 
       
       
       
   
    def read_admin_details(self):
        flie_open = open('admin_details.txt', 'r')
        read_data = flie_open.readlines()[0]
        data = read_data.split(',')
        flie_open.close()
        
        return data[0],data[1]
          
          
    def compare_details(self):
        name = self.lineedit_name.text()
        rank = self.rank_title_edit.text()
        
        
        user_name, password = self.read_admin_details()
        
        
        if (name == user_name) and (rank == password):
            solu = True
            self.display_label.setText('your details is confirmed')
        else:
            solu = False
            self.display_label.setText('confirm your details')
        
        return solu
    
    
    def save_details(self):
        self.dict_details['username'] = self.lineedit_name.text()
        self.dict_details['password'] = self.rank_title_edit.text()
        self.dict_details['confirm_password'] = self.password_conf.text()
        

        if self.confirm_details() == True:
            self.display_label.setText('your details have been saved successfully')
            
            file_open = open('admin_details.txt', 'w')
            list_both = [self.lineedit_name.text(),',', self.rank_title_edit.text(),
                         ',',self.password_conf.text()]
            file_open.writelines(list_both)
            file_open.close()
           
        return
        
    def confirm_details(self):
        solution = False
        if self.verify_details() == False:
            if self.dict_details['password'] != self.dict_details['confirm_password']:
                self.display_label.setText('your password does not match')
                solution = False
                
            else:
                solution = True
        else:
            self.display_label.setText('Invalid entry, please enter your details')
        return solution
    
    
    
    def verify_details(self):
        return ('' in self.dict_details.values())
    
    
    
    
    def cancel_details(self):
        return self.close()
    
    
#if __name__ == '__main__':
#    App = QApplication(sys.argv)
#    App.setStyle('Fusion')
#    
#    window = Authenticate_admin()
#    window.show()
#    p = window.palette()
#    p.setColor(window.backgroundRole(), Qt.gray)
#    window.setPalette(p)
# 
#        
#    sys.exit(App.exec())