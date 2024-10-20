from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from abc import abstractmethod,ABC
import sys
from PySide6.QtCore import  Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QWidget, QLineEdit,QCheckBox
from pagina_de_login import Ui_Form as login
from pagina_de_cadastro import Ui_Form as Tela_de_registro_cadastro
from Verificar_email import Ui_Form as verificar
from pagina_final import Ui_Form as final
from fale_conosco_page import Ui_Form as page_fale_conosco
import pymysql
import smtplib
import threading
import random
import hashlib
class Pagina_de_mudar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tela de Login")
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.setFixedSize(820, 730)
        
        self.pagina_de_login = pagina_de_login()
        self.pagina_de_registro = pagina_de_registro()
        self.pagina_final = pagina_final()
        self.pagina_fale_conosco = Fale_conosco()
        self.verificar_page = Tela_de_verificacao()

        self.definindo_widgets_de_pagina()
        self.stacked_widget.setCurrentWidget(self.pagina_de_login)
        # Chamando funções importantes 
        self.definindo_menu_bar()
        self.definindo_conexoes_dos_Signals()

    def definindo_widgets_de_pagina(self):
        self.stacked_widget.addWidget(self.pagina_de_login)
        self.stacked_widget.addWidget(self.pagina_fale_conosco)
        self.stacked_widget.addWidget(self.pagina_de_registro)
        self.stacked_widget.addWidget(self.verificar_page)
        self.stacked_widget.addWidget(self.pagina_final)


    def conexoes_do_login(self): # realiza mudanças de paginas e outras conexões 
        self.stacked_widget.setCurrentWidget(self.verificar_page)
        self.verificar_page.definir_email_usuario(self.pagina_de_login.email_do_usuario,pagina_de_login)

    def conexoes_da_pagina_de_registro(self): # realiza mudanças de paginas e outras conexões 
        self.stacked_widget.setCurrentWidget(self.verificar_page)
        self.verificar_page.definir_email_usuario(self.pagina_de_registro.texto_do_email,pagina_de_registro)
   
    def definindo_conexoes_dos_Signals(self):
        # Signals pagina de login 
        self.pagina_de_login.usuario_logado.connect(lambda: self.conexoes_do_login())
        self.pagina_de_login.mudar_para_new_accout.connect(lambda: self.stacked_widget.setCurrentWidget(self.pagina_de_registro))

        # Definindo conexões para mudar de pagina 
        self.pagina_final.retornar.connect(lambda: self.stacked_widget.setCurrentWidget(self.pagina_de_login))
        self.pagina_fale_conosco.voltar.connect(lambda: self.stacked_widget.setCurrentWidget(self.pagina_de_login))

        # Signals da pagina de verificação 
        self.verificar_page.criar_conta.connect(lambda: self.finalizar_criacao_de_conta() )
        self.verificar_page.login_executado.connect(lambda: self.stacked_widget.setCurrentWidget(self.pagina_final))

        # Signals da pagina de registro
        self.pagina_de_registro.mudar_para_login.connect(lambda:self.stacked_widget.setCurrentWidget(self.pagina_de_login))
        self.pagina_de_registro.solicitar_verificacao.connect(lambda: self.conexoes_da_pagina_de_registro())
    def finalizar_criacao_de_conta(self):
        self.pagina_de_registro.criar_nova_conta()
        self.stacked_widget.setCurrentWidget(self.pagina_de_login)
    # Definindo o menu bar  
    def definindo_menu_bar(self):
        menu = self.menuBar()
        menu.setStyleSheet("background-color: #373d56")
        menu_ajuda = menu.addMenu("Menu de Ajuda")
        menu_ajuda.setStyleSheet("background-color: #373d56; color: white")
        fale_conosco = menu_ajuda.addAction("Fale conosco")
        sair = menu_ajuda.addAction("Sair")
        sair.triggered.connect(lambda: exit())

        fale_conosco.triggered.connect(lambda: self.stacked_widget.setCurrentWidget(self.pagina_fale_conosco))

    # definindo botões para voltar para a pagina de login 

class pagina_de_login(QWidget):
    mudar_para_new_accout = Signal()
    usuario_logado = Signal()
    def __init__(self) :
        super().__init__(parent=None)
        self.logs_de_erro : Tela_de_mensagens = Tela_de_Erros().tela_de_mensagem
        self.mensagem_sucesso : Tela_de_mensagens = Tela_de_sucesso().tela_de_mensagem
        self.login = login()
        self.consult : conection_service = coneccao_mysql().consult
        self.encript: encrypter_  = criptografador_sha512().encrypt_text
        self.login.setupUi(self)

        self.login.input_senha.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.login.Botao_login.clicked.connect(lambda: self.realizar_login())
        self.login.ver_senha.toggled.connect(lambda: self.ver_senha())
        self.login.criar_nova_conta_botao.clicked.connect(lambda: self.mudar_para_new_accout.emit())
    # Função limpar inputs do usuario
    def limpar_campos(self):
        self.login.input_senha.setText('')
        self.login.Usuario_input.setText('')
    # Função ver senha 
    def ver_senha(self):
            if QCheckBox.isChecked(self.login.ver_senha):
                self.login.input_senha.setEchoMode(QLineEdit.EchoMode.Normal)     
            else:
                self.login.input_senha.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

    def verificar_senhas(self):
        texto_da_senha = self.login.input_senha.text()
        if not texto_da_senha:
            self.logs_de_erro("O campo da senha está vazio")
            return False
        elif len(texto_da_senha) < 4 :
            self.logs_de_erro("Sua Senha tem menos de 4 caractes, Senha invalida")
            return  False
        elif len(texto_da_senha) >= 50:
            self.logs_de_erro("Sua senha não pode ter mais de 50 caracteres ")
            self.login.input_senha.setText("")
            return False
        return True
    # Testa o nome de usuario inserido 
    def verificar_usuario(self):
        texto_usuario = self.login.Usuario_input.text()
        if len(texto_usuario) >= 40 :
            self.logs_de_erro("Erro, não são permitidos mais de 40 caracteres \n para o Username ")
            return False
        if not texto_usuario :
            self.logs_de_erro("Você Não Inseriu um Nome de Usúario")
            return False
        elif " " in texto_usuario:
            self.logs_de_erro("Não é permitido espaços no Nome de Usuario")
            return False
        elif len(texto_usuario) < 3:
            self.logs_de_erro("Seu nome de Usúario deve ter no mínimo 4 caracteres ")
            return False
        data = self.consult('SELECT * FROM Usuarios WHERE Senha = %s and Username = %s ',(self.encript(self.login.input_senha.text()),self.login.Usuario_input.text() ))
        if not data or data == 0:
            self.logs_de_erro("Usuario ou Senha incorreta")
            return False
        self._id_do_usuario = data[0][0]
        self.email_do_usuario = data[0][2]
        return True

    def realizar_login(self):
        if self.verificar_senhas() and self.verificar_usuario():
            self.usuario_logado.emit()
            self.limpar_campos()

class pagina_de_registro(QWidget):
    mudar_para_login = Signal()
    solicitar_verificacao = Signal()
    def __init__(self) :
        super().__init__()

        self.tela_de_cadastro = Tela_de_registro_cadastro()
        self.tela_de_cadastro.setupUi(self)
        self.pagina_De_verificar = verificar()
        self.logs_de_erro : Tela_de_mensagens = Tela_de_Erros().tela_de_mensagem
        self.consulta_db : conection_service = coneccao_mysql().consult
        self.encryptar_dados : encrypter_ = criptografador_sha512().encrypt_text
        self.tela_de_cadastro.Ver_senha.toggled.connect(lambda: self.ativar_echo_mode())
        self.tela_de_cadastro.continuar_botao.clicked.connect(lambda: self.continuar())
        self.tela_de_cadastro.voltar_botao.clicked.connect(lambda: self.mudar_para_login.emit())

    # Testa os dados e inicia a verificação 
    def ativar_echo_mode(self):
        if QCheckBox.isChecked(self.tela_de_cadastro.Ver_senha):
            self.tela_de_cadastro.Input_senha.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.tela_de_cadastro.Input_senha.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
    def continuar(self):
        if self.verificar_usuario() and self.verificar_senhas() and self.verificar_email():
            self.solicitar_verificacao.emit()
    def criar_nova_conta(self):
        self.senha : str = self.encryptar_dados(self.tela_de_cadastro.Input_senha.text())
        self.email: str = self.tela_de_cadastro.verificar_email.text()
        self.username : str = self.tela_de_cadastro.Usuario_input.text()
        self.consulta_db('INSERT INTO Usuarios (Senha,Email,Username) VALUES (%s,%s,%s)',(self.senha,self.email,self.username))
    def limpar_campos(self):
        self.tela_de_cadastro.Input_senha.setText('')
        self.tela_de_cadastro.Usuario_input.setText('')
        self.tela_de_cadastro.verificar_senha.setText('')
        self.tela_de_cadastro.verificar_email.setText('')
    # Define os dados para serem encaminhados para outra classe
   
    def verificar_email(self): # testa os dados do campo do email 
        self.texto_do_email = self.tela_de_cadastro.verificar_email.text()
        if not self.texto_do_email :
            self.logs_de_erro("Você Não Inseriu um Email de recuperação ")
            return False
        elif " " in self.texto_do_email:
            self.logs_de_erro("Espaços Não são permitidos no Email ")
            return False
        elif "@" not in self.texto_do_email:
            self.logs_de_erro("Email inválido")
            return False
        elif "." not in self.texto_do_email:
            self.logs_de_erro("Email inválido")
            return False
        elif len(self.texto_do_email) < 4 :
            self.logs_de_erro("Email inválido")
            return False
        elif len(self.texto_do_email) >= 50:
            self.logs_de_erro("Seu Email não pode ter mais de 50 caracteres")
            return False
        elif self.consulta_db('SELECT * FROM Usuarios WHERE Email = %s',self.texto_do_email):
            self.logs_de_erro("Este Email já esta cadastrado")
            return False
        return True
 
    def verificar_usuario(self):
        texto_usuario = self.tela_de_cadastro.Usuario_input.text()
        if len(texto_usuario) >= 40 :
            self.logs_de_erro("Erro, não são permitidos mais de 40 caracteres \n para o Username ")
            return False
        if not texto_usuario :
            self.logs_de_erro("Você Não Inseriu um Nome de Usúario")
            return False
        elif " " in texto_usuario:
            self.logs_de_erro("Não é permitido espaços no Nome de Usuario")
            return False
        elif len(texto_usuario) < 3:
            self.logs_de_erro("Seu nome de Usúario deve ter no mínimo 4 caracteres ")
            return False
        if self.consulta_db('SELECT * FROM Usuarios WHERE Username = %s',texto_usuario):
            self.logs_de_erro("Este nome de usuario já está cadastrado")
            return False
        return True
    # Trata e verifica o valor inserido pelo usuario 
    def verificar_senhas(self):
        texto_da_senha = self.tela_de_cadastro.Input_senha.text()
        if " " in texto_da_senha :
            self.logs_de_erro("Espaços não são permitidos nas senhas ")
            return False
        elif not texto_da_senha :
            self.logs_de_erro("O campo da senha está vazio")
            return False

        elif len(texto_da_senha) < 4 or texto_da_senha == "12345" :
            self.logs_de_erro("Sua Senha é insegura, Ou tem menos de 4 caractes,  utilize outra")
            return  False
        elif len(texto_da_senha) >= 50 :
            self.logs_de_erro("Sua senha não pode ter mais de 50 caracteres ")
            return False
        return True

class Tela_de_verificacao(QWidget):
    login_executado = Signal()
    criar_conta = Signal()
    def __init__(self) :
        super().__init__()
        self.pagina = verificar()
        self.pagina.setupUi(self)
        self.logs_de_Erro : Tela_de_mensagens = Tela_de_Erros().tela_de_mensagem
        self.logs_de_sucesso : Tela_de_mensagens = Tela_de_sucesso().tela_de_mensagem
        self.email_page : Email_SMTP = enviando_email()
        self.pagina.botao_verificar.clicked.connect(lambda: self.verificar_codigo())

    def definir_email_usuario(self,email,tipo):
        self.email_page.juntando_email(email)
        self.codigo_correto = self.email_page()
        self.tipo = tipo

    # Testa o codigo de verificação recebido  
    def verificar_codigo(self):
        codigo : str = self.pagina.codigo_de_verificacao.text()
        if len(codigo) >= 12:
            self.logs_de_Erro("O codigo inserido é inválido")   
            return False
        try:
            int(codigo)
        except ValueError:
            self.logs_de_Erro("Insira Somente numeros")
            return False
        if codigo == self.codigo_correto:
            print("wewdedwdwedw")
            print(self.tipo)
            if self.tipo == pagina_de_login:
                print('logo')
                self.login_executado.emit()
            elif self.tipo == pagina_de_registro:
                self.logs_de_sucesso("Conta criada com sucesso")
                self.criar_conta.emit()
            return True
        elif codigo != self.codigo_correto: 
            self.logs_de_Erro("Codigo incorreto")
            return False
    # define os dados para Registro


class pagina_final(QWidget):
    retornar = Signal()
    def __init__(self) :
        super().__init__()
        self.pagina = final()
        self.pagina.setupUi(self)
        self.pagina.Sair_botao.clicked.connect(lambda: exit())
        self.pagina.voltar_botao.clicked.connect(lambda: self.retornar.emit())
class Fale_conosco(QWidget):
    voltar = Signal()
    def __init__(self) :
        super().__init__()
        self.pagina_fale_conosco = page_fale_conosco()
        self.pagina_fale_conosco.setupUi(self)
        self.pagina_fale_conosco.voltar_botao.clicked.connect(lambda: self.voltar.emit())
        self.pagina_fale_conosco.Sair_botao.clicked.connect(lambda: exit())


class conection_service(ABC):
    @abstractmethod
    def consult(self,sql_consult) -> any:pass 

class coneccao_mysql(conection_service):
    def consult(self, sql_consult : str , data : list) -> any:
        coneccao = pymysql.connect(host='localhost',
                                   user='root',
                                   password='admin',
                                   database='Banco_de_Dados',)
        cursor = coneccao.cursor()
        cursor.execute(sql_consult,data)
        coneccao.commit()
        coneccao.close()
        cursor.close()
        return cursor.fetchall()


class Tela_de_mensagens(ABC):
    @abstractmethod
    def tela_de_mensagem(self,text: str) -> str: pass



class Tela_de_Erros(Tela_de_mensagens):
    def tela_de_mensagem(self, text: str) -> str:
        mensagem = QMessageBox()
        mensagem.setWindowTitle("Tela de Erro")
        mensagem.setText(text)
        mensagem.setIcon(QMessageBox.Icon.Critical)
        return mensagem.exec()


class Tela_de_sucesso(Tela_de_mensagens):
    def tela_de_mensagem(self, text: str) -> str:
        mensagem = QMessageBox()
        mensagem.setWindowTitle("Sucesso")
        mensagem.setText(text)
        mensagem.setIcon(QMessageBox.Icon.Information)
        return mensagem.exec()

class generator_int(ABC):
    @abstractmethod
    def generate_int(self) -> str: pass
class gerar_codigo(generator_int):
    def generate_int(self) -> str:
        codigo = ''
        for i in range(3):
            codigo += str(random.randint(0,40))
        return codigo


class encrypter_(ABC):
    @abstractmethod
    def encrypt_text(self,text: str) -> str: pass

class criptografador_sha512(encrypter_):
    def encrypt_text(self, text: str) -> str:
        hash = hashlib.sha512()
        hash.update(text.encode("utf-8"))
        return hash.hexdigest()



class Email_SMTP(ABC):
    @abstractmethod
    def juntando_email(self,destinatario:str) -> None: pass
    @abstractmethod
    def Enviando_email(self) -> generator_int: pass
    @abstractmethod
    def definindo_variaveis(self) -> None: pass
    

class enviando_email(Email_SMTP):
    def juntando_email(self,destinatario: str) -> None:
        self.codigo_correto : generator_int = gerar_codigo().generate_int()

        self.mensagem = MIMEMultipart('alternative')
        self.mensagem['From'] = 'verificar254@gmail.com'
        self.mensagem['To'] = destinatario
        self.mensagem['Subject'] = "Código de verificação"
        self.definindo_variaveis()
        
        self.mensagem.attach(MIMEText(self.corpo_email, 'html'))
        a = threading.Thread(target=self.Enviando_email)
        a.start()
    def definindo_variaveis(self) -> None:
        self.corpo_email = f"""
                <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            .container {{
                width: 100%;
                max-width: 600px;
                margin: auto;
                padding: 20px;
                font-family: Arial, sans-serif;
                background-color: #f9f9f9;
                border: 1px solid #ddd;
            }}
            .header {{
                text-align: center;
                padding: 10px;
                background-color: #454d6b;
                color: white;
            }}
            .content {{
                text-align: center;
                margin: 20px;
            }}
            .code {{
                font-size: 24px;
                font-weight: bold;
                margin: 20px;
                padding: 10px;
                background-color: #f1f1f1;
                border: 1px solid #ccc;
                display: inline-block;
            }}
            .footer {{
                text-align: center;
                margin-top: 20px;
                font-size: 12px;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Verificação de Email</h1>
            </div>
            <div class="content">
                <p>Obrigado por se registrar. Use o código abaixo para verificar seu endereço de email:</p>
                <div class="code">{self.codigo_correto}</div>
                <p>Se você não solicitou este código, ignore este email.</p>
            </div>
            <div class="footer">
                &copy; 2024 Brayan Dev . Todos os direitos reservados.
            </div>
        </div>
    </body>
    </html>
    """
    
    def Enviando_email(self) -> bool:
      with smtplib.SMTP("smtp.gmail.com",587,timeout=30) as servidor:
        servidor.starttls()
        servidor.login('verificar254@gmail.com',SS)
        servidor.sendmail(self.mensagem['from'],self.mensagem['to'],self.mensagem.as_string())
        return True
    def __call__(self, ) -> str:
        return self.codigo_correto
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Pagina_de_mudar()
    window.show()
    sys.exit(app.exec())
