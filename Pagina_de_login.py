# Criador         : Brayan vieira 
# função          : Uma simples de login com cryptografia 
# versão          : 1.0
# data da criação : 24/2/2024
import platform
import os
import hashlib
#-----------------------------------------------------------------------------------
#                       definindo variaveis Padrão 
entrada = "\n Insira qualquer tecla para continuar : "
barras = 30 * "-"
MENU = '''     
| Menu de acesso | \n \n [V] Verificar os Logins  \n [D] Deletar todo o banco de dados \n \n Pressione Enter para sair \n \n Insira : '''
#-----------------------------------------------------------------------------------
#                                           Definindo a função ver os registros de usuarios 
def ver_os_registros():
    limpador()
    with open("DB.txt", "r", encoding="utf-8") as Banco_de_dados:
#-----------------------------------------------------------------------------------
#                           lendo e mostrando o arquivo 
        print(Banco_de_dados.read())
        input(entrada)
        return continuacao()
#-----------------------------------------------------------------------------------
#                           função apagar todo o banco de dados
def Deletar_db():
    limpador()
    continuar = input(" \n \n Você têm certeza que quer apagar todo o banco de dados ? \n \n [S] sim | [N] não \n \n Insira : ").startswith("s")
#-----------------------------------------------------------------------------------
#                           Lendo e apagando o arquivo    
    if continuar:
        with open("DB.txt", "w") as arquivo:
            print("\n \n apagada com sucesso....")
            input(entrada)
            return continuacao()
    input(entrada)
#----------------------------------------------------------------------------------
#                               Realizando o Login 
def login():
    limpador()
#-----------------------------------------------------------------------------------
#                           Mensagem de boas vindas e input de usuario
    entrada_de_usuario1 = input(f" \n \n Bem vindo ao Portal de acesso \n \n Insira seu nome de Usuario para continuar \n \n Insira : ")
    if verificar_usuario(entrada_de_usuario1):
        limpador()
#-----------------------------------------------------------------------------------
#                           solicitando a senha para login 
        entrada_de_usuario = input(f"\n Bem vindo {entrada_de_usuario1} \n \n Insira sua senha para continuar \n \n Insira : ")
        Verificar_senha(entrada_de_usuario)
#-----------------------------------------------------------------------------------
#                       Menu principal do programa
banner = '''
                    ╔═════════════════════════════════════════════════════╗
                    ║                                                     ║
                    ║            BEM-VINDO AO PORTAL DE ACESSO            ║
                    ║                                                     ║
                    ╚═════════════════════════════════════════════════════╝

            Menu : 
                    Faça Login ou crie uma conta para continuar 

                    [C] Criar uma conta
                    
                    [L] Fazer Login

                    Insira Alguma opção do menu : '''
#-----------------------------------------------------------------------------------
#                           Continuação do programa apos o login 
def continuacao():
    limpador()
    escolha_menu = input(MENU)
    match escolha_menu:
        case "v":
            ver_os_registros()
        case "d":
            Deletar_db()
        case _:
            sair = input(" Deseja sair? [S] sim | [N] não \n \n Insira : ").lower().startswith("s")
            if sair:
                return exit()
            continuacao()      
#-----------------------------------------------------------------------------------
#                        Verificar usuario ja criado  
def verificar_usuario_repetido(usuario):
    with open("DB.txt", "r") as Arquivo:
        for linhas in Arquivo:
            if "nome de usuario" in linhas:
#-----------------------------------------------------------------------------------
#                           separando o texto do usuario
                texto, nome_de_usuario = linhas.split(":")
                if usuario == nome_de_usuario.strip():
                    input(f" \n \n Erro esse nome de Usuario já está cadastrado \n \n {entrada} ")
                    return exit()
    return False
#-----------------------------------------------------------------------------------
#                       criptografando A senha 
def criptografar_dados(senha):
    tipo_de_criptografia = hashlib.sha512()
    tipo_de_criptografia.update(senha.encode("utf-8"))
    senha_criptografada = tipo_de_criptografia.hexdigest()
    return senha_criptografada
#-----------------------------------------------------------------------------------
#                       Definindo a função limpar a tela 
def limpador():
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        limpador = "cls"
    elif sistema_operacional == "Linux" or sistema_operacional == "Mac":
        limpador = "clear"
    return os.system(limpador)
#-----------------------------------------------------------------------------------
#                           Definindo a função criar conta 
def Criar_conta():
    limpador()
    nome_usuario = input(" \n Insira seu Nome de usuario : ")
#-----------------------------------------------------------------------------------
#                       verificando usuario repetido 
    if verificar_usuario_repetido(nome_usuario):
        return False
    limpador()
#-----------------------------------------------------------------------------------
#                       Verificando a senha e cryptografando
    senha = input(f"Bem vindo {nome_usuario} \n \n Insira sua senha para continuar \n \n Insira : ")
    senha_codificada = criptografar_dados(senha)
#-----------------------------------------------------------------------------------
#                           Escrvendo os logins no arquivo 
    Usuarios = {"tabela_de_usuarios": {"nome de usuario": nome_usuario, "Senha": senha_codificada}}
    with open("DB.txt", "a", encoding="utf-8") as Banco_de_dados:
        Banco_de_dados.write("\n")
        Banco_de_dados.write(barras)
#-----------------------------------------------------------------------------------
#                       percorrendo os valores e escrevendo no arquivo
        for tabela, users in Usuarios.items():
            for chaves, valores in users.items():
                Banco_de_dados.write(f"\n {chaves} : {valores} ")
    return True
#-----------------------------------------------------------------------------------
#                                   Verificando usuario existente [login]
def verificar_usuario(usuario):
    with open("DB.txt", "r") as Arquivo:
#-----------------------------------------------------------------------------------
#                       Percorrendo e verificando o usuario 
        for linhas in Arquivo:
            if "nome de usuario" in linhas:
                texto, nome_de_usuario = linhas.split(":")
                if usuario == nome_de_usuario.strip():
                    return True
    limpador()
    print("\n Erro \n \n Nome de usuario Inexistente : ")
    input(entrada)
    return False
#-----------------------------------------------------------------------------------
#                           Verificando senha para o login 
def Verificar_senha(senha):
    with open("DB.txt", "r") as Arquivo:
        linhasenha = Arquivo.readlines()
        for linha in linhasenha:
            if "Senha" in linha:
                texto, password = linha.split(":")
                senha_criptografada = criptografar_dados(senha)
                if senha_criptografada == password.strip():
                    continuacao()
                    return True  # Senha correta, retorna True
        limpador()
        print("\n Senha incorreta. Tente novamente.")
        input(f"\n \n {entrada}")
    return False  # Senha incorreta ou não encontrada, retorna False

#-----------------------------------------------------------------------------------
#                       Verificando se o arquivo existe / criando 
try:
    with open("DB.txt", "r") as Arquivo:
        testando_erros = Arquivo
except FileNotFoundError:
    with open("DB.txt", "w") as Arquivo:
        Arquivo.write("\n")
#-----------------------------------------------------------------------------------
#                       Iniciando o looping do menu 
while True:
    limpador()
    entrada_do_menu = input(banner).lower()
    match entrada_do_menu:
            case "c":
                Criar_conta()
            case "l":
                login()
        
