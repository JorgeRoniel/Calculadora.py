import PySimpleGUI as sg

sg.theme('Black')

#Layout da janela.
layout = [
    [sg.Input(0, size=(29, 5), key='BOX')],
    [sg.Button('+', size=(5, 2), key='soma'), sg.Button('<-', size=(5, 2), key='bapagar'), sg.Button('Apagar', size=(5, 2), key='delete')],
    [sg.Button('-', size=(5, 2), key='sub'), sg.Button('7', size=(5, 2), key='sete'), sg.Button('8', size=(5, 2), key='oito'), sg.Button('9', size=(5, 2), key='nove')],
    [sg.Button('X', size=(5, 2), key='multi'), sg.Button('4', size=(5, 2), key='quatro'), sg.Button('5', size=(5, 2), key='cinco'), sg.Button('6', size=(5, 2), key='seis')],
    [sg.Button('/', size=(5, 2), key='divi'), sg.Button('1', size=(5, 2), key='um'), sg.Button('2', size=(5, 2), key='dois'), sg.Button('3', size=(5, 2), key='tres')],
    [sg.Button('=', size=(5, 2), key='res'), sg.Button('00', size=(5, 2), key='dzero'), sg.Button('0', size=(5, 2), key='zero'), sg.Button('.', size=(5, 2), key='ponto')]
]

#Criando a janela.
window = sg.Window('Calculator', layout)
result = 0
operacao = ''

#Função que realiza as operações matemáticas.
def resulter():
    if operacao == '+':
        return float(result) + float(values['BOX'])
    elif operacao == '-':
        return float(result) - float(values['BOX'])
    elif operacao == '*':
        return float(result) * float(values['BOX'])
    elif operacao == '/':
        return float(result) / float(values['BOX'])

#Loop de funcionamento.
while True:
    event, values = window.read()

#Fechando o app.
    if event == sg.WIN_CLOSED:
        break

#Quando clicar no numero, ele é impresso na tela.
    if event in 'um':
        if values['BOX'] == '0':
            window['BOX'].update(value='1')
        else:
            window['BOX'].update(value=values['BOX'] + '1')

    if event in 'dois':
        if values['BOX'] == '0':
            window['BOX'].update(value='2')
        else:
            window['BOX'].update(value=values['BOX'] + '2')

    if event in 'tres':
        if values['BOX'] == '0':
            window['BOX'].update(value='3')
        else:
            window['BOX'].update(value=values['BOX'] + '3')

    if event in 'quatro':
        if values['BOX'] == '0':
            window['BOX'].update(value='4')
        else:
            window['BOX'].update(value=values['BOX'] + '4')

    if event in 'cinco':
        if values['BOX'] == '0':
            window['BOX'].update(value='5')
        else:
            window['BOX'].update(value=values['BOX'] + '5')

    if event in 'seis':
        if values['BOX'] == '0':
            window['BOX'].update(value='6')
        else:
            window['BOX'].update(value=values['BOX'] + '6')

    if event in 'sete':
        if values['BOX'] == '0':
            window['BOX'].update(value='7')
        else:
            window['BOX'].update(value=values['BOX'] + '7')

    if event in 'oito':
        if values['BOX'] == '0':
            window['BOX'].update(value='8')
        else:
            window['BOX'].update(value=values['BOX'] + '8')

    if event in 'nove':
        if values['BOX'] == '0':
            window['BOX'].update(value='9')
        else:
            window['BOX'].update(value=values['BOX'] + '9')

    if event in 'zero':
        if values['BOX'] != '0':
            window['BOX'].update(value=values['BOX'] + '0')
    elif event in 'dzero':
        if values['BOX'] != '0':
            window['BOX'].update(value=values['BOX'] + '00')

    if event in 'ponto':
        if values['BOX'] == '':
            window['BOX'].update(value='.')
        else:
            window['BOX'].update(value=values['BOX'] + '.')

#Funções para apagar os valores na tela.
    if event in 'delete':
        #result = 0
        window['BOX'].update(value=result)

    if event in 'bapagar':
        window['BOX'].update(value=values['BOX'][:-1])

#Definindo as operações matematicas.
    if event in 'soma':
        if operacao != '':
            result = resulter()
        else:
            operacao = '+'
            result = values['BOX']
        window['BOX'].update(value='')

    if event in 'sub':
        if operacao != '':
            result = resulter()
        else:
            operacao = '-'
            result = values['BOX']
        window['BOX'].update(value='')

    if event in 'multi':
        if operacao != '':
            result = resulter()
        else:
            operacao = '*'
            result = values['BOX']
        window['BOX'].update(value='')
        
    if event in 'divi':
        if operacao != '':
            result = resulter()
        else:
            operacao = '/'
            result = values['BOX']
        window['BOX'].update(value='')

    if event in 'res':
        result = resulter()
        window['BOX'].update(value=result)
        result = 0
        operacao = ''

window.close()
