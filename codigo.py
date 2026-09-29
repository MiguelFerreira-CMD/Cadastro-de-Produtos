# BIBLIOTECAS = Packs de Códigos
# pip  install pyautogui -> instala uuma biblioteca

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

import pyautogui
import time

# Passo a Passo ddo PROGRAMA!:

#  Passo 1:  abrir o navegador e entrar no sistema da empresa:

pyautogui.PAUSE  = 1 # espera 1 seg entre os pyautoguis

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press("win")
pyautogui.write("Brave") # seu navegador!
pyautogui.press("enter")

pyautogui.write(link)
pyautogui.press("enter")

time.sleep(2) # esperar 2 seg

# Passo 2: login no sistema:
pyautogui.click(693, 367)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab")
pyautogui.write("Python")
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2) # esperar 2 seg

# Passo 3: abrir a  base de dados:
# pip install pandas openpyxl -> Base de Dados -> o pandas e o openpyxl trabalham com eles!
import pandas

tabela = pandas.read_csv("produtos.csv")
print(tabela)

for linha in  tabela.index:
    # Passo 4 e 5: Cadastrar os produtos
    # O for repete o processo até cadastrar todos os produtos.

    # codigo
    pyautogui.click(745, 254)

    codigo  = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    #categoria
    categoria  = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    #preço
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    #custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])
    # Se houver observação, preenche o campo.
    # Se estiver vazio (nan), não escreve nada.
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")

    pyautogui.press("enter")
    pyautogui.scroll(5000) # voltar pro inicio da tela!