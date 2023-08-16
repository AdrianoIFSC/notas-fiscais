import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

layout = [
    [sg.Text('CÓDIGO DO SIAFI:    '), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('DIGITE SUA SENHA: '), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Text('NOME DA NOTA FISCAL COM EXTENÇÃO EM .PDF')],
    [sg.Input(key='arquivo')],
    [sg.Button('Começar')]
]

janela = sg.Window('Automatização de Liquidação', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Começar':
        usuario = valores['usuario']
        senha = valores['senha']
        navegador = webdriver.Firefox()
        file = valores['arquivo']

        # Navigate to the desired URL
        navegador.get('http://localhost/php_project/menu.php')

        # Locate and interact with elements using XPath
        arquivo_input = navegador.find_element('xpath', '/html/body/div/div[1]/div/form/div/input')
        arquivo_input.send_keys(r'C:\Users\DAM\Documents\\' + file)  # Corrected the file path
        navegador.find_element('xpath', '/html/body/div/div[1]/div/form/input').click()

        # ... Continue with your remaining automation steps ...

        # Close the browser when done
        navegador.quit()

janela.close()