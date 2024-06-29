
## Tela de login 
![Captura de tela_2024-06-29_12-07-01](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/b97b589b-f468-4a99-98ce-e10d62305e9d)

## Tela de registro de conta 
![Captura de tela_2024-06-29_12-17-14](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/b99236a0-43ae-468b-9650-9686dd059c24)

## Descrição
Este é um sistema de Login desenvolvido em python com a biblioteca pyside6, utilizei o banco de dados mysql para manipular os dados  
E o Pyqt designer para criar os layout da aplicação 

## Proteções

- Adicionei tratamento para todos os inputs de dados do usuario, previnindo assim vulnerabilidades comuns de injeção de código
- Adicionei PlaceHolders nos inputs destinados ao Mysql para previnir sql injection
- Todas as senhas são armazenadas criptografadas com SHA512 no Mysql
- Para Logar ou Criar uma conta devera inserir o código de verificação enviado para o email adicionando assim uma camada extra de segurança
- Adicionei tratamentos para os erros e logs, sera exibido uma mensagem de erro na tela

## Funcionalidades da Tela de Login 
- Login seguro e verificação obrigátoria 
- Logs e Telas de erro caso algo dê errado
- Limitação de caracteres para cada input
- Verificação se o Login existe no banco de dados
- Função para ver a senha digitada
  
## Funcionalidades da Tela de registro de conta 
- Adicionei limitação e tratamento para todos os inputs
- telas e logs de erro
- Caso você insira um Email ou Username já cadastrado não será possivel criar a conta com esses dados
- Para criar uma conta você deve verificar o Email inserido, Inserindo o codigo enviado
- Função para ver a senha digitada
  
## Tecnologias usadas
- PySide6 ( PySide6 é a biblioteca oficial da Qt para Python, que permite a criação de interfaces gráficas de usuário (GUIs) robustas e modernas. )
- MySQL ( pymysql é um módulo que permite a conexão e a manipulação de bancos de dados MySQL a partir do Python. )
- SMTP ( smtplib é um módulo que define uma interface para enviar emails através do protocolo SMTP (Simple Mail Transfer Protocol). )
- Threading ( threading é um módulo que permite a execução de operações em segundo plano, utilizando threads. )
- Random ( random é um módulo que implementa geradores de números pseudo-aleatórios para várias distribuições. )
- Hashlib ( hashlib é um módulo que fornece uma interface para algoritmos de hash seguros, como SHA256. )
  
## Tela de verificação 
![Captura de tela_2024-06-29_12-24-16](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/3424caed-831a-41f9-8ddc-55ee832e44ea)

## Email enviado 
![Captura de tela_2024-06-29_12-25-46](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/375276e3-841e-442e-8fd7-bf22906a2b80)

## Tela final Após o Login 
![Captura de tela_2024-06-29_12-27-23](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/a0b26ac1-1319-470c-a8a9-f136f031d024)

## Pagina fale conosco do Menu de Ajuda
![Captura de tela_2024-06-29_12-30-29](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/b722df86-d9eb-430a-94d2-7083fb209770)

## Tela com 4 erros de da Pagina de Login 
- Eu coloquei somente 4 pois Não ficaria bom colocando todas as Telas de Erro pois são muitas e atrapalharia na visibilidade
![Captura de tela_2024-06-29_12-32-25](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/0aa72b7d-595f-42df-a0e8-46410b1b982b)
![Captura de tela_2024-06-29_12-32-57](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/79aabbc4-abbe-47ce-9195-db2a58d4e9da)
![Captura de tela_2024-06-29_12-33-23](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/f81db7d7-b60d-4c39-b628-243ef4566abc)
![Captura de tela_2024-06-29_12-35-30](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/eece4de7-f6a1-4f58-9158-b78655d8801e)

## Telas com 4 erros da Pagina de Cadastro
- Eu coloquei somente 4 pois Não ficaria bom colocando todas as Telas de Erro pois são muitas e atrapalharia na visibilidade
![Captura de tela_2024-06-29_12-45-40](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/03f422d2-ebce-45fc-8813-dff96d4c32ae)
![Captura de tela_2024-06-29_12-46-09](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/02941ecc-eb02-4453-94d5-3b9bcd4e3cee)
![Captura de tela_2024-06-29_12-46-34](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/0fbf1123-2549-44f5-a4f0-93d5c7d29269)
![Captura de tela_2024-06-29_12-47-01](https://github.com/Brayandev0/Pagina-de-logins-criptografados/assets/84828739/b842d742-62d3-4f1c-87ba-180bb061a6c1)
