
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Form(QWidget):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(820, 730)
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-30, 0, 881, 741))
        self.widget_2.setMinimumSize(QSize(600, 600))
        self.widget_2.setMaximumSize(QSize(900, 900))
        self.widget_2.setLayoutDirection(Qt.LeftToRight) # type: ignore
        self.widget_2.setAutoFillBackground(False)
        self.widget_2.setStyleSheet(u"background-color: #454d6b")
        self.Tela = QWidget(self.widget_2)
        self.Tela.setObjectName(u"Tela")
        self.Tela.setGeometry(QRect(200, 60, 511, 481))
        self.Tela.setStyleSheet(u"background-color: #373d56")
        self.Usuario_input = QLineEdit(self.Tela)
        self.Usuario_input.setObjectName(u"Usuario_input")
        self.Usuario_input.setGeometry(QRect(120, 100, 281, 51))
        self.Usuario_input.setStyleSheet(u"padding-left: 17px;")
        self.Input_senha = QLineEdit(self.Tela)
        self.Input_senha.setObjectName(u"Input_senha")
        self.Input_senha.setGeometry(QRect(120, 160, 281, 51))
        self.Input_senha.setStyleSheet(u"padding-left: 17px;")
        self.Texto_de_login = QLabel(self.Tela)
        self.Texto_de_login.setObjectName(u"Texto_de_login")
        self.Texto_de_login.setGeometry(QRect(40, 10, 451, 61))
        font = QFont()
        font.setFamilies([u"Tlwg Typist"])
        font.setPointSize(18)
        font.setItalic(True)
        self.Texto_de_login.setFont(font)
        self.continuar_botao = QPushButton(self.Tela)
        self.continuar_botao.setObjectName(u"continuar_botao")
        self.continuar_botao.setGeometry(QRect(280, 400, 141, 31))
        self.continuar_botao.setStyleSheet(u"background-color: #2c3245; color: white; border-radius: 5px; border: none")
        self.verificar_senha = QLineEdit(self.Tela)
        self.verificar_senha.setObjectName(u"verificar_senha")
        self.verificar_senha.setGeometry(QRect(120, 220, 281, 51))
        self.verificar_senha.setStyleSheet(u"padding-left: 17px;")
        self.verificar_email = QLineEdit(self.Tela)
        self.verificar_email.setObjectName(u"verificar_email")
        self.verificar_email.setGeometry(QRect(120, 280, 281, 51))
        self.verificar_email.setStyleSheet(u"padding-left: 17px;")
        self.line = QFrame(self.Tela)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(30, 60, 451, 16))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.voltar_botao = QPushButton(self.Tela)
        self.voltar_botao.setObjectName(u"voltar_botao")
        self.voltar_botao.setGeometry(QRect(80, 400, 141, 31))
        self.voltar_botao.setStyleSheet(u"background-color: #2c3245; color: white; border-radius: 5px; border: none")
        self.Ver_senha_ = QCheckBox(self.Tela)
        self.Ver_senha_.setObjectName(u"Ver_senha_")
        self.Ver_senha_.setGeometry(QRect(100, 350, 101, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Usuario_input.setText("")
        self.Usuario_input.setPlaceholderText(QCoreApplication.translate("Form", u"          👤 | Insira seu novo nome de Usuarío  ", None))
        self.Input_senha.setText("")
        self.Input_senha.setPlaceholderText(QCoreApplication.translate("Form", u"          🔒 | Insira sua senha", None))
        self.Texto_de_login.setText(QCoreApplication.translate("Form", u"Bem vindo a pagina de cadastro", None))

        self.continuar_botao.setText(QCoreApplication.translate("Form", u"Continuar", None))
        self.verificar_senha.setText("")
        self.verificar_senha.setPlaceholderText(QCoreApplication.translate("Form", u"         🔒 | Confirme sua senha", None))
        self.verificar_email.setText("")
        self.verificar_email.setPlaceholderText(QCoreApplication.translate("Form", u"          @ | Insira um email de recuperação ", None))
        self.voltar_botao.setText(QCoreApplication.translate("Form", u"Voltar ", None))
        self.Ver_senha_.setText(QCoreApplication.translate("Form", u"Ver senhas", None))
    # retranslateUi

