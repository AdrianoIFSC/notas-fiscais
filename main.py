import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

sg.theme('Dark2')
layout = [
    [sg.Text('CÓDIGO DO SIAFI:    '), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('DIGITE SUA SENHA: '), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Text('NOME DA NOTA FISCAL COM EXTENÇÃO EM .PDF')],
    [sg.InputText(key='arquivo', size=(32,1))],
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
        navegador.get('*') # NO LUGAR DO # INSIRA A URL DO SITE QUE IRA RESUMIR A NOTA FISCAL
        arquivo_input = navegador.find_element(By.XPATH, '*') # NO LUGAR DO * COLOQUE O XPATH DO CAMPO DE INPUT
        arquivo_input.send_keys(r'*\\' + file) #NO LUGAR DO * COLOQUE O LOCAL DA PASTA ONDE ESTA LOCALIZADO AS NOTAS FISCAIS
        navegador.find_element(By.XPATH, '*').click() # NO LUGAR DO * COLOQUE O XPATH DO BOTÃO DE EXTRAIR TEXTO
        navegador.execute_script("window.open('about:blank', '_blank');")
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.get('*') # NO LUGAR DO * INSIRA A URL DO SITE ONDE SERA LIQUIDADO A NOTA FISCAL