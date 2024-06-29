
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(830, 730)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-30, -1, 861, 741))
        self.widget.setStyleSheet(u"background-color: #454d6b")
        self.Tela_3 = QWidget(self.widget)
        self.Tela_3.setObjectName(u"Tela_3")
        self.Tela_3.setGeometry(QRect(220, 150, 461, 341))
        self.Tela_3.setStyleSheet(u"background-color: #373d56")
        self.codigo_de_verificacao = QLineEdit(self.Tela_3)
        self.codigo_de_verificacao.setObjectName(u"codigo_de_verificacao")
        self.codigo_de_verificacao.setGeometry(QRect(90, 80, 281, 51))
        self.codigo_de_verificacao.setPlaceholderText(u"🔐 | Insira o codigo enviado ")
        self.codigo_de_verificacao.setStyleSheet("padding: 17px")
        self.botao_verificar = QPushButton(self.Tela_3)
        self.botao_verificar.setObjectName(u"botao_verificar")
        self.botao_verificar.setGeometry(QRect(260, 170, 141, 31))
        self.botao_verificar.setStyleSheet(u"background-color: #2c3245; color: white; border-radius: 5px; border: none")
        self.Texto_de_login_2 = QLabel(self.Tela_3)
        self.Texto_de_login_2.setObjectName(u"Texto_de_login_2")
        self.Texto_de_login_2.setGeometry(QRect(90, 0, 281, 61))
        font = QFont()
        font.setFamilies([u"Tlwg Typist"])
        font.setPointSize(18)
        font.setItalic(True)
        self.Texto_de_login_2.setFont(font)
        self.Sair_botao = QPushButton(self.Tela_3)
        self.Sair_botao.setObjectName(u"Sair_botao")
        self.Sair_botao.setGeometry(QRect(80, 170, 141, 31))
        self.Sair_botao.setStyleSheet(u"background-color: #2c3245; color: white; border-radius: 5px; border: none")
        self.line_5 = QFrame(self.Tela_3)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setGeometry(QRect(30, 40, 20, 241))
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_7 = QFrame(self.Tela_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setGeometry(QRect(50, 270, 391, 16))
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_8 = QFrame(self.Tela_3)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setGeometry(QRect(40, 20, 51, 20))
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_9 = QFrame(self.Tela_3)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setGeometry(QRect(420, 30, 20, 251))
        self.line_9.setFrameShape(QFrame.Shape.VLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)
        self.line_10 = QFrame(self.Tela_3)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setGeometry(QRect(360, 20, 71, 16))
        self.line_10.setFrameShape(QFrame.Shape.HLine)
        self.line_10.setFrameShadow(QFrame.Shadow.Sunken)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.botao_verificar.setText(QCoreApplication.translate("Form", u"Verificar", None))
        self.Texto_de_login_2.setText(QCoreApplication.translate("Form", u"Verifique seu email", None))
        self.Sair_botao.setText(QCoreApplication.translate("Form", u"Sair", None))
    # retranslateUi
