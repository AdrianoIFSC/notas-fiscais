import PySimpleGUI as sg
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
sg.theme('Dark2')
layout = [
    [sg.Text('CÓDIGO DO SIAFI:    '), sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('DIGITE SUA SENHA: '), sg.Input(key='senha', password_char='*', size=(20, 1))],
    [sg.Text('NOME DA NOTA FISCAL COM EXTENÇÃO EM .PDF')],
    [sg.Input(key='arquivo', size=(20,1))],
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
        navegador.get('http://localhost/php_project/menu.php')
        arquivo_input = navegador.find_element('xpath', '/html/body/div/div[1]/div/form/div/input')
        arquivo_input.send_keys(r'C:\Users\DAM\Documents\\' + file)
        navegador.find_element('xpath', '/html/body/div/div[1]/div/form/input').click()
        navegador.find_element('xpath', '//*[@id="resultado"]/div[1]/div[1]/button[1]').click()
        navegador.execute_script("window.open('about:blank', '_blank');")
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.get('http://localhost/adriano.html')
        navegador.find_element('xpath', '/html/body/form/div[1]/input').send_keys(valores['usuario'])
        navegador.find_element('xpath', '/html/body/form/div[2]/input').send_keys(valores['senha'])
        navegador.find_element('xpath', '/html/body/form/button/a').click()

        #CAMPO 0
        navegador.find_element('xpath', '/html/body/form/div[1]/label[1]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 1
        navegador.find_element('xpath', '//*[@id="resultado"]/div[1]/div[2]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/div[1]/label[2]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 2
        navegador.find_element('xpath', '//*[@id="resultado"]/div[1]/div[3]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/div[2]/label[1]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 3
        navegador.find_element('xpath', '//*[@id="resultado"]/div[2]/div[1]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/div[2]/label[2]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 4
        navegador.find_element('xpath', '//*[@id="resultado"]/div[2]/div[1]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/div[2]/label[2]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 5
        navegador.find_element('xpath', '/html/body/div/div[2]/div/section/div[2]/div[2]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/div[3]/label[1]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 6
        navegador.find_element('xpath', '//*[@id="resultado"]/div[2]/div[3]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/div[3]/label[2]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 7
        navegador.find_element('xpath', '//*[@id="resultado"]/div[3]/div[2]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/div[4]/label[1]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 8
        navegador.find_element('xpath', '//*[@id="resultado"]/div[3]/div[3]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/div[4]/label[2]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 9
        navegador.find_element('xpath', '//*[@id="resultado"]/div[4]/div[2]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/div[5]/label[1]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 10
        navegador.find_element('xpath', '//*[@id="resultado"]/div[4]/div[2]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/div[5]/label[2]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 11
        navegador.find_element('xpath', '//*[@id="resultado"]/div[4]/div[3]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/label[1]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 12
        navegador.find_element('xpath', '//*[@id="resultado"]/div[4]/div[4]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/label[2]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])

        #CAMPO 13
        navegador.find_element('xpath', '//*[@id="resultado"]/div[4]/div[5]/button').click()
        navegador.switch_to.window(navegador.window_handles[1])
        navegador.find_element('xpath', '/html/body/form/label[3]/input').send_keys(Keys.CONTROL, 'v')
        navegador.switch_to.window(navegador.window_handles[0])