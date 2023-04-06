import PySimpleGUI as sg
sg.theme('DarkAmber')
c1 = [
    [sg.T('Nome completo:')],
    [sg.T('Série')],
    [sg.T('Estado')],
    [sg.T('Cidade')],
    [sg.T('Escola')]
]
c2 = [
    [sg.I(key='-nome-')],
    [sg.I(key='-ano-', size=1), sg.T('º'), sg.I(key='-sala-', size=3)],
    [sg.I(key='-estado-', size=20)],
    [sg.I(key='-cidade-', size=20)],
    [sg.I(key='-escola-')]
]
layout_main = [
    [sg.Titlebar('Sistema')],
    [sg.Col(c1), sg.VerticalSeparator(), sg.Col(c2)],
    [sg.HorizontalSeparator()],
    [sg.T('*Escreva corretamente, cuidado com erros de escrita')],
    [sg.HorizontalSeparator()],
    [sg.B('Continuar')]
]
janela_main = sg.Window('main', layout_main)
while True:
    eventos, valores = janela_main.read()
    if eventos == sg.WIN_CLOSED:
        break
    if eventos == 'Continuar':
        nome = valores['-nome-']
        ano = valores['-ano-']
        sala = valores['-sala-']
        serie = f'{ano}º{sala}'
        estado = valores['-estado-']
        cidade = valores['-cidade-']
        escola = valores['-escola-']
        local = f'{estado}, {cidade}'
        if len(valores['-ano-']) > 1:
            valores['-ano-'] = ano[len(ano) - 1:len(ano)]
            ano = valores['-ano-']
        print(nome, serie, local, escola)
        