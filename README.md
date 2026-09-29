# Cadastro de Produtos

Automação desenvolvida em Python para realizar o cadastro automático de produtos em um sistema web a partir de uma base de dados em CSV.

Este projeto foi desenvolvido como um exercício prático de aprendizado, com foco em automação de tarefas, manipulação de dados e interação com interfaces gráficas.

# Sobre o projeto

O programa utiliza PyAutoGUI para automatizar o preenchimento de um sistema web.

Os dados dos produtos são armazenados em um arquivo produtos.csv e processados utilizando Pandas.

A automação percorre cada produto da base de dados e realiza seu cadastro automaticamente no sistema.

# Funcionamento

Base de dados (CSV)
        ↓
     Pandas
        ↓
Leitura dos produtos
        ↓
      Loop
        ↓
    PyAutoGUI
        ↓
Preenchimento do formulário
        ↓
Cadastro do produto

# Tecnologias utilizadas

Python

PyAutoGUI — automação de teclado e mouse

Pandas — leitura e manipulação dos dados

CSV — armazenamento dos dados dos produtos

# Estrutura do projeto 📂

CadastroDeProdutos/

├── codigo.py
├── auxiliar.py
├── produtos.csv
├── .vscode/
└── README.md

# Como executar

1. Clone o repositório
git clone https://github.com/MiguelFerreira-CMD/Cadastro-de-Produtos.git

2. Entre na pasta
cd Cadastro-de-Produtos

3. Instale as bibliotecas necessárias
pip install pyautogui pandas

4. Execute o programa
python codigo.py

# Base de dados

Os produtos utilizados na automação estão armazenados no arquivo:

produtos.csv

O programa utiliza o Pandas para ler a tabela e percorre cada linha para realizar o cadastro.

# O que pratiquei neste projeto

Este exercício foi utilizado para praticar conceitos importantes de Python, como:

Importação e utilização de bibliotecas;

Variáveis;

Estruturas de repetição (for);

Estruturas condicionais (if);

Conversão de tipos com str();

Leitura e manipulação de arquivos CSV;

Utilização do Pandas;

Automação de teclado e mouse com PyAutoGUI;

Organização de um projeto no GitHub;

Versionamento utilizando Git.

# Objetivo

O principal objetivo deste projeto foi colocar em prática os conhecimentos adquiridos durante os estudos de Python, transformando conceitos de programação em uma automação capaz de executar uma tarefa repetitiva.

# Autor

Miguel Ferreira
