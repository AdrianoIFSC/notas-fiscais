from openpyxl import Workbook
import PySimpleGUI as sg

wb = Workbook()
ws = wb.active
current_row = 2

sg.theme('Dark2')
layout = [
    [sg.Text('Sequencia'), sg.Text('Item'), sg.Text('                                                                        Marca'), sg.Text('                   Quantidade')],
    [sg.Input(key='sequencia', size=(8, 1)), sg.Input(key='item'), sg.Input(key='marca', size=(16, 1)), sg.Input(key='quantidade', size=(8, 1))],
    [sg.Button('Gerar Planilha'), sg.Button('Adicionar Item')]
]

janela = sg.Window('Gerador de Planilha', layout)

while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Adicionar Item':
        data = [valores['sequencia'], valores['item'], valores['marca'], valores['quantidade']]
        ws.append(data)
        current_row += 1
    if eventos == 'Gerar Planilha':
        wb.save(r'C:\Users\DAM\Downloads\Almoxarifado.xlsx')

janela.close()