from PyQt5.QtWidgets import QMainWindow, QApplication , QLabel, QLineEdit,QPushButton,QMessageBox,QProgressBar,QFrame,QRadioButton
import sys
import random
import re

class fenetre(QMainWindow):
    def __init__(self):
        super().__init__()
        #_____________window________________
        self.setWindowTitle("Password Generator")
        self.setGeometry(0,0,700,950)
        self.setFixedSize(700,950)
        self.setStyleSheet("background-color:#bebacf;")
        
        #---------------------home page----------------
        self.home=QFrame(self)
        self.home.setGeometry(0,0,700,950)
        self.home.setStyleSheet("background-color:#EDE7F6;")
        self.title=QLabel("Password Generator",self.home)
        self.title.setGeometry(100,-80,500,400)
        self.title.setStyleSheet("""
                                QLabel{
                                    font-family:Poppins;
                                    font-size: 46px;
                                    font-weight:900;
                                    color:#EDE9FE;
                                    text-align:center;
                                }
                                QLabel:hover {
                                    color:#A855F7;
                                }
                                """)
        self.label1=QLabel("Choose what you want to do.",self.home)
        self.label1.setGeometry(190,210,300,100)
        self.label1.setStyleSheet("color:#EDE9FE;font-family:Roboto;font-size:20px;font-weight:500;")
        self.generate_btn1=QPushButton("Generate Password",self.home)
        self.generate_btn1.setGeometry(100,310,500,80)
        self.generate_btn1.setStyleSheet("""
                                        QPushButton{
                                            color:black;
                                            font-family:Poppins;
                                            font-size:20px;
                                            font-weight:800;
                                            background-color:#EDE7F6;
                                            border:3px solid #A855F7;
                                            border-radius:32px ;
                                        }
                                        QPushButton:hover {
                                            background:#A855F7;
                                            color:#EDE9FE;
                                        }
                                        """)
        self.generate_btn1.clicked.connect(self.generate_1)

        self.test_btn=QPushButton("Test Password",self.home)
        self.test_btn.setGeometry(100,440,500,80)
        self.test_btn.setStyleSheet("""
                                        QPushButton{
                                            color:black;
                                            font-family:Poppins;
                                            font-size:20px;
                                            font-weight:800;
                                            background-color:#EDE7F6;
                                            border:3px solid #A855F7;
                                            border-radius:32px ;
                                        }
                                        QPushButton:hover {
                                            background:#A855F7;
                                            color:#EDE9FE;
                                        }
                                        """)
        self.test_btn.clicked.connect(self.show_test_page)
        #self.home.hide()
        #-----------------generate password page-----------------
        self.generate_page=QFrame(self)
        self.generate_page.setGeometry(0,0,700,950)
        self.generate_page.setStyleSheet("background-color:#EDE7F6;")
        self.label2=QLabel("Enter Password length",self.generate_page)
        self.label2.setGeometry(100,210,300,100)
        self.label2.setStyleSheet("color:#EDE9FE;font-family:Roboto;font-size:20px;font-weight:500;")
        self.input1=QLineEdit(self.generate_page)
        self.input1.setGeometry(100,310,500,80)
        self.input1.setPlaceholderText("10,12,14,16,18,20,22")
        self.input1.setStyleSheet("""
                                    QLineEdit{
                                        background-color:#EDE7F6;
                                        color:black;
                                        font-family:Inter;
                                        font-size: 15px;
                                        padding: 12px 16px;
                                        border:3px solid #2D2744;
                                        border-radius: 10px;
                                        selection-background-color:#A855F7;
                                        selection-color:#EDE9FE;
                                    }
                                    QLineEdit:hover {
                                        border:3px solid #A855F7;
                                    }
                                    QLineEdit:focus {
                                        border:3px solid #A855F7;
                                        background-color:#33294D;
                                    }
                                    QLineEdit:disabled {
                                        background-color:#221B35;
                                        color:#8B7FA3;
                                        border:3px solid #221B35;
                                    }
                                """)
        self.generate_btn2=QPushButton("Generate Password",self.generate_page)
        self.generate_btn2.setGeometry(100,440,500,80)
        self.generate_btn2.setStyleSheet("""
                                        QPushButton{
                                            color:black;
                                            font-family:Poppins;
                                            font-size:20px;
                                            font-weight:800;
                                            background-color:#EDE7F6;
                                            border:3px solid #A855F7;
                                            border-radius:32px ;
                                        }
                                        QPushButton:hover {
                                            background:#A855F7;
                                            color:#EDE9FE;
                                        }
                                        """)
        self.generate_btn2.clicked.connect(self.generate_function)
        self.result=QFrame(self.generate_page)
        self.result.setGeometry(100,600,500,300)
        self.result.setStyleSheet("background-color:#2D2744;")
        self.label3=QLabel("Result:",self.result)
        self.label3.setGeometry(20,-20,100,100)
        self.label3.setStyleSheet("color:#EDE9FE;font-family:Roboto;font-size:20px;font-weight:500;")
        self.input_result=QLineEdit(self.result)
        self.input_result.setGeometry(30,90,400,70)
        self.input_result.setStyleSheet("""
                                        QLineEdit{
                                        background-color:#2D2744;
                                        color:#EDE9FE;
                                        font-family:Inter;
                                        font-size: 25px;
                                        font-weight:600;
                                        padding: 12px 16px;
                                        border:3px solid #A855F7;
                                        border-radius: 10px;
                                        selection-background-color:#A855F7;
                                        selection-color:#EDE9FE;
                                    }
                                    QPushButton:hover {
                                            background:#A855F7;
                                            color:#EDE9FE;
                                        }
                                        """)
        self.home_btn1=QPushButton("Home",self.result)
        self.home_btn1.setGeometry(30,190,80,60)
        self.home_btn1.setStyleSheet("""
                            QPushButton{
                                        color:#C4B5FD;
                                        font-family:Poppins;
                                        font-size:20px;
                                        font-weight:800;
                                        background-color: #2D2744;
                                        border:3px solid #A855F7;
                                        border-radius:23px ;
                                        }
                        QPushButton:hover {
                                            background:#A855F7;
                                            color:#EDE9FE;
                                        }
                                    """)
        self.home_btn1.clicked.connect(self.home_function)
        self.copy_btn=QPushButton("Copy",self.result)
        self.copy_btn.setGeometry(195,190,80,60)
        self.copy_btn.setStyleSheet("""
                            QPushButton{
                                        color:#C4B5FD;
                                        font-family:Poppins;
                                        font-size:20px;
                                        font-weight:800;
                                        background-color: #2D2744;
                                        border:3px solid #A855F7;
                                        border-radius:23px ;
                                        }
                        QPushButton:hover {
                                            background:#A855F7;
                                            color:#EDE9FE;
                                        }
                                    """)
        self.copy_btn.clicked.connect(self.copy_password)
        self.exit_btn1=QPushButton("Exit",self.result)
        self.exit_btn1.setGeometry(350,190,80,60)
        self.exit_btn1.setStyleSheet("""
                            QPushButton{
                                        color:#C4B5FD;
                                        font-family:Poppins;
                                        font-size:20px;
                                        font-weight:800;
                                        background-color: #2D2744;
                                        border:3px solid #A855F7;
                                        border-radius:23px ;
                                        
                                        }
                        QPushButton:hover {
                                            background:#A855F7;
                                            color:#EDE9FE;
                                        }
                                    """)
        self.exit_btn1.clicked.connect(self.close)
        self.result.hide()
        self.generate_page.hide()
        
        
        
#-----------------test password page-----------------
        self.test_page=QFrame(self)
        self.test_page.setGeometry(0,0,700,950)
        self.test_page.setStyleSheet("background-color:#EDE7F6;")
        self.label_test1=QLabel("Enter Your Password",self.test_page)
        self.label_test1.setGeometry(100,210,300,100)
        self.label_test1.setStyleSheet("color:#EDE9FE;font-family:Roboto;font-size:20px;font-weight:500;")
        self.input_test=QLineEdit(self.test_page)
        self.input_test.setGeometry(100,310,500,80)
        self.input_test.setPlaceholderText("********************")
        self.input_test.setStyleSheet("""
                                    QLineEdit{
                                        background-color:#2D2744;
                                        color:#EDE9FE;
                                        font-family:Inter;
                                        font-size: 15px;
                                        padding: 12px 16px;
                                        border:3px solid #2D2744;
                                        border-radius: 10px;
                                        selection-background-color:#A855F7;
                                        selection-color:#EDE9FE;
                                    }
                                    QLineEdit:hover {
                                        border:3px solid #A855F7;
                                    }
                                    QLineEdit:focus {
                                        border:3px solid #A855F7;
                                        background-color:#33294D;
                                    }
                                    QLineEdit:disabled {
                                        background-color:#221B35;
                                        color:#8B7FA3;
                                        border:3px solid #221B35;
                                    }
                                """)
        self.test_btn=QPushButton("Test Password",self.test_page)
        self.test_btn.setGeometry(100,440,500,80)
        self.test_btn.setStyleSheet("""
                                        QPushButton{
                                            color:#C4B5FD;
                                            font-family:Poppins;
                                            font-size:20px;
                                            font-weight:800;
                                            background-color:#2D2744;
                                            border:3px solid #A855F7;
                                            border-radius:32px ;
                                        }
                                        QPushButton:hover {
                                            background:#A855F7;
                                            color:#EDE9FE;
                                        }
                                        """)
        self.test_btn.clicked.connect(self.test_function)
        self.result_test=QFrame(self.test_page)
        self.result_test.setGeometry(100,600,500,300)
        self.result_test.setStyleSheet("background-color:#2D2744;")
        self.label_test2=QLabel("Result:",self.result_test)
        self.label_test2.setGeometry(20,-20,100,100)
        self.label_test2.setStyleSheet("color:#EDE9FE;font-family:Roboto;font-size:20px;font-weight:500;")
        self.input_result_test=QLineEdit(self.result_test)
        self.input_result_test.setGeometry(30,90,400,70)
        self.input_result_test.setReadOnly(True)
        self.input_result_test.setStyleSheet("""
                                        QLineEdit{
                                        background-color:#2D2744;
                                        color:#EDE9FE;
                                        font-family:Inter;
                                        font-size: 25px;
                                        font-weight:600;
                                        padding: 12px 16px;
                                        border:3px solid #A855F7;
                                        border-radius: 10px;
                                        selection-background-color:#A855F7;
                                        selection-color:#EDE9FE;
                                    }
                                    QPushButton:hover {
                                            background:#A855F7;
                                            color:#EDE9FE;
                                        }
                                        """)
        self.home_btn_test=QPushButton("Home",self.result_test)
        self.home_btn_test.setGeometry(30,190,80,60)
        self.home_btn_test.setStyleSheet("""
                            QPushButton{
                                        color:#C4B5FD;
                                        font-family:Poppins;
                                        font-size:20px;
                                        font-weight:800;
                                        background-color: #2D2744;
                                        border:3px solid #A855F7;
                                        border-radius:23px ;
                                        }
                        QPushButton:hover {
                                            background:#A855F7;
                                            color:#EDE9FE;
                                        }
                                    """)
        self.home_btn_test.clicked.connect(self.home_function)
        self.generate_btn_test = QPushButton("Generate 🔒", self.result_test)
        self.generate_btn_test.setGeometry(155,190,150,60)
        self.generate_btn_test.setStyleSheet("""
                            QPushButton{
                                        color:#C4B5FD;
                                        font-family:Poppins;
                                        font-size:20px;
                                        font-weight:800;
                                        background-color: #2D2744;
                                        border:3px solid #A855F7;
                                        border-radius:23px ;
                                        }
                        QPushButton:hover {
                                            background:#A855F7;
                                            color:#EDE9FE;
                                        }
                                    """)
        self.generate_btn_test.clicked.connect(self.show_generate_page)
        self.exit_btn_test=QPushButton("Exit",self.result_test)
        self.exit_btn_test.setGeometry(350,190,80,60)
        self.exit_btn_test.setStyleSheet("""
                            QPushButton{
                                        color:#C4B5FD;
                                        font-family:Poppins;
                                        font-size:20px;
                                        font-weight:800;
                                        background-color: #2D2744;
                                        border:3px solid #A855F7;
                                        border-radius:23px ;
                                        
                                        }
                        QPushButton:hover {
                                            background:#A855F7;
                                            color:#EDE9FE;
                                        }
                                    """)
        self.exit_btn_test.clicked.connect(self.close)
        self.result_test.hide()
        
        self.test_page.hide()
        
        
    def test_function(self):
        a=self.input_test.text()
        
        if a =="":
            QMessageBox.warning(self,"warning","Enter Your password ")
            return 
        
        j=0
        if re.search(r'[a-z]', a):
            j+=1
        if re.search(r'[A-Z]', a):
            j+=1
        if re.search(r'[0-9]', a):
            j+=1
        if len(a)>8:
            j+=1
        if re.search(r"[!@#$%^&*_\(\)\-=\[\]{}|;:,\?<>]", a):
            j += 1
        
        self.result_test.show()
        if  j<=2:
            self.input_result_test.setText("🔴 Weak password 😟")
        elif  j<=3:
            self.input_result_test.setText("🟡 Normal password 🙂")
        elif  j<=4:
            self.input_result_test.setText("🟢 Strong password 💪🔒")
        elif j == 5:
            self.input_result_test.setText("🛡️ Secure ")
        
    def show_generate_page(self):
        self.home.hide()
        self.test_page.hide()
        self.generate_page.show()
        
    def generate_1(self):
        self.home.hide()
        self.generate_page.show()
    def generate_function(self):
        word=""
        if not (self.input1.text()).isdigit():
            QMessageBox.warning(self,"Error","Enter a valid number")
            return 
        if int(self.input1.text())<10:
            QMessageBox.warning(self,"warning","Enter a valid number greater than 9 ")
            return 
        a=int(self.input1.text())

        while len(word)<int(a):
            #lowercase letters
            letters=['y','x','c','v','b','n','m','a','s','d','f','g','h','j','k','l','ö','ä','q','w','e','r','t','z','u','i','o','p','ü']
            n1=random.randint(0,len(letters)-1)
            word=word+letters[n1]
            #UpperCase letters
            Letters=['Y','X','C','V','B','N','M','A','S','D','F','G','H','J','K','L','Ö','Ä','Ü','P','O','I','U','Z','T','R','E','W','Q']
            n2=random.randint(0,len(Letters)-1)
            word=word+Letters[n2]
            #special characters
            schar=['!','@','#','$','%','^','&','*','_','(',')','-','=','[',']','{','}','|',';',':',',','?','<','>']
            n3=random.randint(0,len(schar)-1)
            word=word+schar[n3]
            
            n4=random.randint(0,9)
            word=word+str(n4)
            
        list1=list(word)
        random.shuffle(list1)
        mixed_word=''.join(list1)
        while len(mixed_word)<a:
                mixed_word+="@"
            
        while len(mixed_word)>a:
                mixed_word=mixed_word[:a]
        
        self.input_result.setText(mixed_word)
        self.result.show()
        print(mixed_word)
        print(len(mixed_word))
        
    def copy_password(self):
        clipboard=QApplication.clipboard()
        clipboard.setText(self.input_result.text())
    
    def show_test_page(self):
        self.home.hide()
        self.generate_page.hide()
        self.test_page.show()
        self.result.hide()
        self.result_test.hide()
        
        
    def home_function(self):
        self.home.show()
        self.generate_page.hide()
        self.test_page.hide()
        self.result.hide()
        self.result_test.hide()

        self.input1.clear()
        self.input_result.clear()
        self.input_test.clear()
        self.input_result_test.clear()
        
def main():
    app=QApplication(sys.argv)
    window=fenetre()
    window.show()
    sys.exit(app.exec())

if __name__=='__main__':
    main()
