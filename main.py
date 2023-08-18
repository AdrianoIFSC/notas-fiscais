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
    [sg.InputText(key='arquivo', size=(32,1)), sg.FileBrowse()],
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
        navegador.get('*') # NO LUGAR DO * INSIRA A URL DO SITE QUE IRA RESUMIR A NOTA FISCAL
        arquivo_input = navegador.find_element(By.XPATH, '*') # NO LUGAR DO * INSIRA O XPATH DO CAMPO DE INPUT DO SITE
        arquivo_input.send_keys(r'*\\' + file) # NO LUGAR DO * INSIRA O LOCAL DA PASTA ONDE ESTA LOCALIZADO AS NOTAS FISCAIS
        navegador.find_element(By.XPATH, '*').click() # NO LUGAR DO * INSIRA O XPATH DO BOTÃO 'EXTRAIR TEXTO'
        navegador.execute_script("window.open('about:blank', '_blank');")
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.get('*') # NO LUGAR DO * INSIRA A URL DO SITE ONDE SERA LIQUIDADA A NOTA FISCAL
        navegador.find_element(By.XPATH, '*').send_keys(valores['usuario']) # NO LUGAR DO * INSIRA O XPATH DO CAMPO DE USUARIO
        navegador.find_element(By.XPATH, '*').send_keys(valores['senha']) # NO LUGAR DO * INSIRA O XPATH DO CAMPO DA SENHA
        layout2 = [
            [sg.Text('RESOLVA O CAPTCHA!')],
            [sg.Input(key='captcha'), sg.Button('Resolvido')]
        ]
        janela2 = sg.Window('Resolução do CAPTCHA', layout2)
        while True:
            eventos2, valores2 = janela2.read()
            if eventos2 == 'Resolvido':
                navegador.find_element(By.XPATH, '*').send_keys(valores2['captcha']) # NO LUGAR DO * INSIRA O XPATH DO CAMPO DO CAPTCHA
                navegador.find_element(By.XPATH, '*').click() # NO LUGAR DO * INSIRA O XPATH DO BOTÃO 'ACESSAR'

                # ESTE CAMPO DE CÓDIGO PODE SER REPETIDO CONFORME O NÚMERO DE CAMPUS DE PREENCHIMENTO DO SISTEMA DE LIQUIDAÇÃO
                navegador.switch_to.window(navegador.window_handles[0])
                navegador.find_element(By.XPATH, '*').click() # NO LUGAR DO * INSIRA O XPATH DO BOTÃO DE COPIAR INFORMAÇÃO
                navegador.switch_to.window(navegador.window_handles[1])
                navegador.find_element(By.XPATH, '*').send_keys(Keys.CONTROL + 'v') # NO LUGAR DO * INIRA O XPATH DO CAPO DE INPUT QUE DESEJA PREENCHER NO SISTEMA