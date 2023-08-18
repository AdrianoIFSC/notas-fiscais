import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

sg.theme('Dark2')
layout = [
    [sg.Text('CÓDIGO DO SIAFI:    '), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('DIGITE SUA SENHA: '), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Text('NOME DA NOTA FISCAL COM EXTENÇÃO EM .PDF')],
    [sg.InputText(key='arquivo', size=(32, 1)), sg.FileBrowse()],
    [sg.Button('Começar')]
]
janela = sg.Window('Automatização de Liquidação', layout)
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Começar':
        navegador = webdriver.Firefox()
        file = valores['arquivo']
        
        # Change the URL to the appropriate one
        navegador.get('http://26.68.23.218/php_project/update.php')
        
        # Locate the input element for file upload by its name attribute
        arquivo_input = navegador.find_element(By.NAME, 'nome_do_input')  # Replace 'nome_do_input' with the actual name
        
        # Send the full file path to the input element
        arquivo_input.send_keys(file)
        
        # Perform the click action, replace 'xpath_do_botao' with the actual XPath of the button
        navegador.find_element(By.XPATH, 'Upload PDF').click()
        
        # Continue with the rest of your automation steps
        
        # Close the second window and the browser when done
        janela2.close()
        navegador.quit()