
##                                                                               Painel de Acesso
![Captura de tela_2024-08-01_19-16-45](https://github.com/user-attachments/assets/d4f4468d-a97c-4d0e-b421-85136c2e9c82)


## Descrição

Este é um sistema de Login desenvolvido em Python com a biblioteca PySide6. Utilizei MySQL para manipulação dos dados e PyQt Designer para criar o layout da aplicação.

## Proteções

- **Tratamento de todos os inputs de dados do usuário para prevenir vulnerabilidades comuns de injeção de código.**
- **Utilização de Placeholders nos inputs destinados ao MySQL para prevenir SQL Injection.**
- **Armazenamento de todas as senhas criptografadas com SHA-512 no MySQL.**
- **Verificação por código enviado via email para login e criação de conta, adicionando uma camada extra de segurança.**
- **Tratamento de erros e logs com mensagens de erro exibidas na tela.**
- **Conexão para enviar o Email criptografada com TLS .**

## Funcionalidades da Tela de Login

- **Login seguro com verificação de Email obrigatória.**
- **Exibição de logs e telas de erro caso algo dê errado.**
- **Limitação de caracteres para cada input.**
- **Verificação da existência do login no banco de dados.**
- **Função para visualizar a senha digitada.**

## Tecnologias Usadas

- **PySide6**: Biblioteca oficial da Qt para Python, que permite a criação de interfaces gráficas de usuário (GUIs) robustas e modernas.
- **MySQL**: PyMySQL é um módulo que permite a conexão e a manipulação de bancos de dados MySQL a partir do Python.
- **SMTP**: smtplib é um módulo que define uma interface para enviar emails através do protocolo SMTP (Simple Mail Transfer Protocol).
- **Threading**: threading é um módulo que permite a execução de operações em segundo plano, utilizando threads.
- **Random**: random é um módulo que implementa geradores de números pseudo-aleatórios para várias distribuições.
- **Hashlib**: hashlib é um módulo que fornece uma interface para algoritmos de hash seguros, como SHA-256.

## Tela de registro de conta 
** ![Captura de tela_2024-08-01_19-14-35](https://github.com/user-attachments/assets/f533be81-51fc-4378-a634-8b7d974d5720)**

## Funcionalidades da Tela de Registro de Conta

- **Limitação e tratamento para todos os inputs.**
- **Exibição de telas e logs de erro.**
- **Verificação de email e username já cadastrados para impedir duplicidade de conta.**
- **Verificação de email através de código enviado para criar uma conta.**
- **Função para visualizar a senha digitada.**

## Como ficam armazenados os login ( Tela DBeaver )
**![Captura de tela_2024-06-29_13-30-34](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/56aa51b2-7db3-4f13-af0d-819ed8dcb2af)**
  
## Tela de verificação 
**![Captura de tela_2024-06-29_12-24-16](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/3424caed-831a-41f9-8ddc-55ee832e44ea)**

## Email enviado 
**![Captura de tela_2024-06-29_12-25-46](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/375276e3-841e-442e-8fd7-bf22906a2b80)**

## Tela final Após o Login 
**![Captura de tela_2024-06-29_12-27-23](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/a0b26ac1-1319-470c-a8a9-f136f031d024)**

## Pagina "Fale Conosco" do Menu de Ajuda
**![Captura de tela_2024-06-29_12-30-29](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/b722df86-d9eb-430a-94d2-7083fb209770)**

## Tela com Erros da Pagina de Login 
- **Foram colocadas apenas 4 telas para não comprometer a visibilidade, devido ao grande número de telas de erro.**
**![Captura de tela_2024-06-29_12-32-25](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/0aa72b7d-595f-42df-a0e8-46410b1b982b)**
**![Captura de tela_2024-06-29_12-32-57](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/79aabbc4-abbe-47ce-9195-db2a58d4e9da)**
**![Captura de tela_2024-06-29_12-33-23](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/f81db7d7-b60d-4c39-b628-243ef4566abc)**
**![Captura de tela_2024-06-29_12-35-30](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/eece4de7-f6a1-4f58-9158-b78655d8801e)**

## Telas com Erros da Pagina de Cadastro
- **Foram colocadas apenas 4 telas para não comprometer a visibilidade, devido ao grande número de telas de erro.**
  
**![Captura de tela_2024-06-29_12-45-40](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/03f422d2-ebce-45fc-8813-dff96d4c32ae)**
**![Captura de tela_2024-06-29_12-46-09](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/02941ecc-eb02-4453-94d5-3b9bcd4e3cee)**
**![Captura de tela_2024-06-29_12-46-34](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/0fbf1123-2549-44f5-a4f0-93d5c7d29269)**
**![Captura de tela_2024-06-29_12-47-01](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/b842d742-62d3-4f1c-87ba-180bb061a6c1)**
