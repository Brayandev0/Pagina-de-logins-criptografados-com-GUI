
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QStackedWidget, QWidget, QLineEdit
from pagina_de_login import Ui_Form as login
from pagina_de_cadastro import Ui_Form
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
        self.resize(820, 730)

        self.pagina_de_login = pagina_de_login()
        self.pagina_de_registro = pagina_de_registro()
        self.pagina_final = pagina_final()
        self.pagina_fale_conosco = Fale_conosco()
        self.registro_verificar = pagina_de_verificacao_registro()
        self.pagina_verificar_login = pagina_de_verificacao_login()
        self.definindo_widgets_de_pagina()
        self.stacked_widget.setCurrentWidget(self.pagina_de_login)
        # Chamando funções importantes 
        self.mudar_de_pagina()
        self.definindo_menu_bar()
        self.conexoes_da_pagina_de_registro()
        self.conexoes_pagina_verificar_rg()

        # Definindo conexões para mudar de pagina 
        self.pagina_de_login.usuario_logado.connect(lambda: self.continuar_login())
        self.pagina_verificar_login.sair.connect(lambda: self.voltar())
        self.pagina_final.retornar.connect(lambda: self.voltar())
        self.pagina_verificar_login.usuario_logado.connect(lambda: self.stacked_widget.setCurrentWidget(self.pagina_final))
        self.pagina_fale_conosco.voltar.connect(lambda: self.voltar())
    def definindo_widgets_de_pagina(self):
        self.stacked_widget.addWidget(self.pagina_de_login)
        self.stacked_widget.addWidget(self.pagina_fale_conosco)
        self.stacked_widget.addWidget(self.pagina_de_registro)
        self.stacked_widget.addWidget(self.registro_verificar)
        self.stacked_widget.addWidget(self.pagina_verificar_login)
        self.stacked_widget.addWidget(self.pagina_final)
    # define as conexoes da pagina verificar rg
    def conexoes_pagina_verificar_rg(self):
        self.registro_verificar.sair.connect(lambda: self.stacked_widget.setCurrentWidget(self.pagina_de_login))
        self.registro_verificar.sair.connect(lambda: self.voltar())

    # define conexoes da pagina de registro 
    def conexoes_da_pagina_de_registro(self):
        self.pagina_de_registro.mudar_para_login.connect(lambda: self.voltar())
        self.pagina_de_registro.solicitar_verificacao.connect(lambda: self.continuar_registro())
    # Função para encaminhar dados para verificação 
    def continuar_registro(self):
        codigo = self.pagina_de_registro.codigo_de_verificacao
        username = self.pagina_de_registro.username
        senha = self.pagina_de_registro.senha
        email = self.pagina_de_registro.email
        self.stacked_widget.setCurrentWidget(self.registro_verificar)
        self.registro_verificar.definir_dados(codigo,username,senha,email)
    # Função para encaminhar dados para o login  

    def continuar_login(self):
         codigo = self.pagina_de_login.codigo_de_verificacao
         self.stacked_widget.setCurrentWidget(self.pagina_verificar_login)
         self.pagina_verificar_login.definindo_codigo(codigo)
    # função para voltar para a pagina de login 
    def voltar(self):
        self.pagina_de_registro.limpar_campos()
        self.pagina_de_login.limpar_campos()
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
    def mudar_de_pagina(self):
        self.pagina_de_login.login.criar_nova_conta_botao.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.pagina_de_registro))
        self.pagina_de_registro.tela_de_cadastro.voltar_botao.clicked.connect(lambda: self.stacked_widget.setCurrentWidget(self.pagina_de_login))

class pagina_de_login(QWidget):
    usuario_logado = Signal()
    def __init__(self) :
        super().__init__(parent=None)
        self.codigo_de_verificacao = ""
        self.login = login()
        self.login.setupUi(self)
        self.conectar_a_db()
        self.login.input_senha.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.login.Botao_login.clicked.connect(lambda: self.realizar_login())
        self.login.ver_senha.toggled.connect(lambda: self.ver_senha())
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
    # função testar os dados e logar 
    def realizar_login(self):
        if self.login.Texto_de_login.text() and self.login.input_senha.text():
            if self.verificar_senhas() and self.verificar_usuario():
                if self.verificar_usuario_e_senha():
                    self.mensagem_sucesso(f"Foi enviado um código de verificação para o email cadastrado na conta com o username {self.login.Usuario_input.text()}. \n \n Por favor, digite o código enviado.")
                    self.juntando_email()
                    self.usuario_logado.emit()
        else:
            self.logs_de_erro("Os campos estão vazio ")

    # verifica na db se os dados existem 
    def verificar_usuario_e_senha(self):
        self.cursor_mysql.execute(f'SELECT * FROM Usuarios WHERE Username = %s AND Senha = %s',(self.login.Usuario_input.text(),self.gerar_senha_criptografada(self.login.input_senha.text())))
        self.conectar.commit()
        self.dados = self.cursor_mysql.fetchone()
        print(self.dados)
        if not self.dados:
            self.logs_de_erro("Nome de Usuario ou Senha incorreta")
            return False
        else:
            return True
    # gera uma vaor criptografado
    def gerar_senha_criptografada(self,valor):
            hash = hashlib.sha512()
            hash.update(valor.encode())
            senha_final = hash.hexdigest()
            return senha_final   
    # Função que mosra telas de erro 
    def logs_de_erro(self,texto : str):
        Tela_de_erro = QMessageBox()
        Tela_de_erro.setWindowTitle("Tela de Erro")
        Tela_de_erro.setText(texto)
        Tela_de_erro.setIcon(QMessageBox.Icon.Critical)
        return Tela_de_erro.exec()
    # Função que mosra telas de Sucesso 
    def mensagem_sucesso(self,texto : str):
        sucesso = QMessageBox()
        sucesso.setWindowTitle("Sucesso")
        sucesso.setText(texto)
        sucesso.setIcon(QMessageBox.Icon.Information)
        return sucesso.exec()
    # Conectar na db 
    def conectar_a_db(self):
            try:
                self.conectar = pymysql.Connect(
                            host="localhost",
                            user="root",
                            password="admin",
                            database="Banco_de_Dados",
                            )
                self.cursor_mysql = self.conectar.cursor()
            except pymysql.err.OperationalError:
                self.logs_de_erro("Tivemos um erro em nosso servidor \n tente novamente mais tarde")
                exit()
#       verificando valor do email 
    def definindo_variaveis(self):
        print("Iniciando envio de email...")
        if self.dados != None:
            __id,_username,_senha,email = self.dados    
            self.mensagem = MIMEMultipart('alternative')
            self.mensagem['From'] = 'verificar254@gmail.com'
            self.mensagem['To'] = email
            self.mensagem['Subject'] = "Código de verificação"
            self.mensagem.attach(MIMEText(self.corpo_do_email, 'html'))
    # Junta dados e inicia o email 
    def juntando_email(self):
        self.definindo_corpo_do_email()
        self.definindo_variaveis()
        thread = threading.Thread(target=self.enviando_email)
        thread.start()
  
    #Inicia a conexão e envia o email 
    def enviando_email(self):
                if self.dados != None:
                    __id,_username,_senha,email = self.dados
                    print("Iniciando envio de email...")
                    mensagem = MIMEMultipart('alternative')
                    mensagem['From'] = 'verificar254@gmail.com'
                    mensagem['To'] = email
                    mensagem['Subject'] = "Código de verificação"
                    mensagem.attach(MIMEText(self.corpo_do_email, 'html'))
                    print("Criando conexão SMTP...")
                    with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as server:
                        server.starttls()
                        server.login('verificar254@gmail.com', "pztuufbqhkeyqvki")
                        server.sendmail(mensagem['From'], mensagem['To'], mensagem.as_string())
                        print("Logando no servidor SMTP...")

    # Gera o codigo que vai ser enviado        
    def gerar_codigo(self):
        self.codigo_de_verificacao = ""
        for i in range(3):
            self.codigo_de_verificacao += str(random.randint(1,40))
    # Testa as senhas enviadas pelo usuario
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

        return True
    # Define o nosso email 
    def definindo_corpo_do_email(self):
        self.gerar_codigo()
        self.corpo_do_email = f"""
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
                <div class="code">{self.codigo_de_verificacao}</div>
                <p>Se você não solicitou este código, ignore este email.</p>
            </div>
            <div class="footer">
                &copy; 2024 Brayan Dev . Todos os direitos reservados.
            </div>
        </div>
    </body>
    </html>
    """
class pagina_de_registro(QWidget):
    mudar_para_login = Signal()
    solicitar_verificacao = Signal()
    def __init__(self,parent=None ) :
        super().__init__(parent)
        self.tela_de_cadastro = Ui_Form()
        self.tela_de_cadastro.setupUi(self)
        self.pagina_de_login = pagina_de_login()
        self.pagina_De_verificar = verificar()
        self.conectar_Db()
        self.tela_de_cadastro.Input_senha.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.tela_de_cadastro.verificar_senha.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
        self.tela_de_cadastro.Ver_senha_.toggled.connect(lambda: self.ver_senha())
        self.tela_de_cadastro.continuar_botao.clicked.connect(lambda: self.continuar())
        self.tela_de_cadastro.voltar_botao.clicked.connect(lambda: self.ir_para_login())
    def ir_para_login(self):
        self.limpar_campos()
        self.mudar_para_login.emit()
    # Testa os dados e inicia a verificação 
    def continuar(self):
            if self.verificar_email() and self.verificar_senhas() and self.verificar_usuario() :
                self.juntar_email()
                self.definir_dados()
                self.sucesso_aviso(f"Insira o código de verificação enviado no email {self.email} \n \n Insira o codigo para continuar")
                self.solicitar_verificacao.emit()
                self.limpar_campos()
    # Limpa os campos dos inputs 
    def limpar_campos(self):
        self.tela_de_cadastro.Input_senha.setText('')
        self.tela_de_cadastro.Usuario_input.setText('')
        self.tela_de_cadastro.verificar_senha.setText('')
        self.tela_de_cadastro.verificar_email.setText('')
    # Define os dados para serem encaminhados para outra classe
    def definir_dados(self):
        self.username = self.tela_de_cadastro.Usuario_input.text()
        self.senha = self.gerar_senha_criptografada(self.tela_de_cadastro.Input_senha.text())
        self.email = self.tela_de_cadastro.verificar_email.text()
    # Gera um valor criptografado
    def gerar_senha_criptografada(self,valor):
            hash = hashlib.sha512()
            hash.update(valor.encode())
            senha_final = hash.hexdigest()
            return senha_final 
    # Tela de mensagens de sucesso   
    def sucesso_aviso(self,valor:str):
        aviso = QMessageBox()
        aviso.setText(valor)
        aviso.setIcon(QMessageBox.Icon.Information)
        aviso.setWindowTitle("Sucesso")
        return aviso.exec()
    # Conecta ao banco de dados 
    def conectar_Db(self):
        self.conectar = pymysql.Connect(
            host="localhost",
            user="root",
            password="admin",
            database="Banco_de_Dados",
            )
        self.cursor_mysql = self.conectar.cursor()
#       verificando valor do email 
    def verificar_email(self):
        texto_do_email = self.tela_de_cadastro.verificar_email.text()
        if not texto_do_email :
            self.logs_de_erro("Você Não Inseriu um Email de recuperação ")
            return False
        elif " " in texto_do_email:
            self.logs_de_erro("Espaços Não são permitidos no Email ")
            return False
        elif "@" not in texto_do_email:
            self.logs_de_erro("Email inválido")
            return False
        elif "." not in texto_do_email:
            self.logs_de_erro("Email inválido")
            return False
        elif len(texto_do_email) < 4 :
            self.logs_de_erro("Email inválido")
            return False
        elif len(texto_do_email) >= 50:
            self.logs_de_erro("Seu Email não pode ter mais de 50 caracteres")
            return False
        elif not self.verificar_valor_na_db("Email",texto_do_email):
            self.logs_de_erro("Este Email já esta cadastrado")
            return False
        return True
    # Define a função ver a senha 
    def ver_senha(self):
         if QCheckBox.isChecked(self.tela_de_cadastro.Ver_senha_):
                self.tela_de_cadastro.Input_senha.setEchoMode(QLineEdit.EchoMode.Normal)
                self.tela_de_cadastro.verificar_senha.setEchoMode(QLineEdit.EchoMode.Normal)     
        else:
            self.tela_de_cadastro.Input_senha.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)
            self.tela_de_cadastro.verificar_senha.setEchoMode(QLineEdit.EchoMode.PasswordEchoOnEdit)

    # Verifica se um valor já existe no banco de dados 
    def verificar_valor_na_db(self, campo: str, valor: str):
        sql = f"SELECT 1 FROM Usuarios WHERE {campo} = %s LIMIT 1"
        print(f"Executando SQL: {sql} com valor: {valor}")
        self.cursor_mysql.execute(sql, (valor,))
        self.conectar.commit()
        valor_recebido = self.cursor_mysql.fetchone()
        print(f"Resultado da consulta: {valor_recebido}")
        if valor_recebido == None:
            return True
        return False
    # Trata o valor inserido pelo Usuario
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
        if not self.verificar_valor_na_db('Username',texto_usuario):
            self.logs_de_erro("Este nome de usuario já está cadastrado")
            return False
        return True
    # Trata e verifica o alor inserido pelo usuario 
    def verificar_senhas(self):
        texto_da_senha = self.tela_de_cadastro.Input_senha.text()
        texto_confirmar_senha = self.tela_de_cadastro.verificar_senha.text()

        if " " in texto_da_senha and " " in texto_confirmar_senha:
            self.logs_de_erro("Espaços não são permitidos nas senhas ")
            return False
        elif not texto_da_senha:
            self.logs_de_erro("O campo da senha está vazio")
            return False
        elif texto_da_senha != texto_confirmar_senha:
            self.logs_de_erro(" As Senhas não coincidem ")
            return False
        elif len(texto_da_senha) < 4 or texto_da_senha == "12345":
            self.logs_de_erro("Sua Senha é insegura, Ou tem menos de 4 caractes,  utilize outra")
            return  False
        elif len(texto_da_senha) >= 50:
            self.logs_de_erro("Sua senha não pode ter mais de 50 caracteres ")
            return False
        return True
    # Define as mensagens de erro 
    def logs_de_erro(self,texto : str):
        Tela_de_erro = QMessageBox()
        Tela_de_erro.setWindowTitle("Tela de Erro")
        Tela_de_erro.setText(texto)
        Tela_de_erro.setIcon(QMessageBox.Icon.Critical)
        Tela_de_erro.exec()
    # Define a mensagem do email 
    def definindo_variaveis(self):
        print("Iniciando envio de email...")
        self.mensagem = MIMEMultipart('alternative')
        self.mensagem['From'] = 'verificar254@gmail.com'
        self.mensagem['To'] = self.tela_de_cadastro.verificar_email.text()
        self.mensagem['Subject'] = "Código de verificação"
        self.mensagem.attach(MIMEText(self.corpo_do_email, 'html'))
    # Junta as funções do email e envia 
    def juntar_email(self):
        self.definindo_corpo_do_email()
        self.definindo_variaveis()
        thread = threading.Thread(target=self.enviar_email)
        thread.start()
    # Inicia a conexão e envia o email 
    def enviar_email(self):
                        print("Criando conexão SMTP...")
                        with smtplib.SMTP("smtp.gmail.com", 587, timeout=30) as server:
                            server.starttls()
                            server.login("verificar254@gmail.com", 'pztuufbqhkeyqvki')
                            server.sendmail(self.mensagem['From'], self.mensagem['To'], self.mensagem.as_string())
                
                        print("Email enviado com sucesso.")
    # Gera um codigo aleatorio para ser enviado para o email 
    def gerar_codigo(self):
            self.codigo_de_verificacao = ""
            for i in range(3):
                self.codigo_de_verificacao += str(random.randint(1,40))
    # Define a mensagem que vai ser enviada 
    def definindo_corpo_do_email(self):
        self.gerar_codigo()
        self.corpo_do_email = f"""
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
                <div class="code">{self.codigo_de_verificacao}</div>
                <p>Se você não solicitou este código, ignore este email.</p>
            </div>
            <div class="footer">
                &copy; 2024 Brayan Dev . Todos os direitos reservados.
            </div>
        </div>
    </body>
    </html>
    """
class pagina_de_verificacao_registro(QWidget):
    sair = Signal()
    def __init__(self) :
        super().__init__()
        self.pagina_verificar = verificar()
        self.pagina_verificar.setupUi(self)
        self.conectar_Db()
        self.pagina_verificar.Sair_botao.clicked.connect(lambda: self.sair.emit())
        self.pagina_verificar.botao_verificar.clicked.connect(lambda: self.verificar_codigo())
    # Testa o codigo de verificação recebido  
    def verificar_codigo(self):
        codigo = self.pagina_verificar.codigo_de_verificacao.text()
        if len(codigo) >= 12:
            self.logs_de_Erro("O codigo inserido é inválido")
            return False
        try:
            testando = int(codigo)
        except ValueError:
            self.logs_de_Erro("Insira Somente numeros")
            return False
        if codigo == self.codigo_De_verificacao:
            self.sucesso("Sua conta foi criada com sucesso \n Realize seu login")
            self.criar_conta()
            self.sair.emit()
            print("conta_criada")
            return True
        else: 
            self.logs_de_Erro("Codigo incorreto")
            return False
    # define os dados para Registro
    def definir_dados(self,codigo,username,senha,email):
        self.codigo_De_verificacao = codigo
        self.nome_de_usuario = username
        self.senha_criptografada = senha
        self.email_do_usuario = email
    # Realiza a conexão do db
    def conectar_Db(self):
        self.conectar = pymysql.Connect(
            host="localhost",
            user="root",
            password="admin",
            database="Banco_de_Dados",
            )
        self.cursor_mysql = self.conectar.cursor()
    # Insere os dados do usuario no banco de dados 
    def criar_conta(self):
        self.cursor_mysql.execute('INSERT INTO Usuarios (Username,Senha,Email)'
                                  'VALUES'
                                  '(%s,%s,%s)',(self.nome_de_usuario,self.senha_criptografada,self.email_do_usuario))
        self.conectar.commit()
    # Definindo mensagens de erro
    def logs_de_Erro(self,valor: str):
        erro = QMessageBox()
        erro.setText(valor)
        erro.setIcon(QMessageBox.Icon.Critical)
        erro.setWindowTitle("Erro")
        return erro.exec()
    #Definindo mensagens de sucesso 
    def sucesso(self,valor: str):
        erro = QMessageBox()
        erro.setText(valor)
        erro.setIcon(QMessageBox.Icon.Information)
        erro.setWindowTitle("Sucesso")
        return erro.exec()    
    
class pagina_de_verificacao_login(QWidget):
    usuario_logado = Signal()
    sair = Signal()
    def __init__(self):
        super().__init__()
        self.pagina_verificar = verificar()
        self.pagina_verificar.setupUi(self)
        self.pagina_verificar.botao_verificar.clicked.connect(lambda: self.tratamento_codigo())
        self.pagina_verificar.Sair_botao.clicked.connect(lambda: self.sair.emit())
    # Recebe o codigo de verificação e trata 
    def tratamento_codigo(self):
        codigo = self.pagina_verificar.codigo_de_verificacao.text()
        if len(codigo) >= 12:
            self.logs_de_Erro("O codigo inserido é inválido")
            return False
        try:
            testando = int(codigo)
        except ValueError:
            self.logs_de_Erro("Insira Somente numeros")
            return False
        if codigo == self.codigo_De_verificacao:
            self.usuario_logado.emit()
            return True
        else:
            self.logs_de_Erro("Codigo Incorreto")
            return False
    # define o codigo de verificação 
    def definindo_codigo(self,codigo):
         self.codigo_De_verificacao = codigo
    # Define os codigos de erro 
    def logs_de_Erro(self,valor: str):
        erro = QMessageBox()
        erro.setText(valor)
        erro.setIcon(QMessageBox.Icon.Critical)
        erro.setWindowTitle("Erro")
        return erro.exec()
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Pagina_de_mudar()
    window.show()
    sys.exit(app.exec())
