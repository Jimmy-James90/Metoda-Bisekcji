import PySimpleGUI as sg
import numpy as num

ZP = -2  # początek przedzialu
ZK = 2  # koniec przedziału
Dyskretyzacja = 0.50000
Bi_Blad = 0.50000
#Funkcja obliczajaca miejsca zerowe
def bisekcja(a, b, Fx,max_krokow):
    max_error = Bi_Blad
    if Fx(a) == 0:
        return a
    if Fx(b) == 0:
        return b
    for j in range(max_krokow):

        x_bisek = (a + b) / 2
        bisek = Fx(x_bisek)
        if bisek == 0:
            return x_bisek
        if abs(bisek) < max_error:
            return x_bisek

        if Fx(a) * bisek < 0:
            b = x_bisek
        else:
            a = x_bisek

# Layout SimpleGUI
layout = [
    [sg.Text('Poziom Dyskretyzacji ', key='-TEXT1-')],
    [sg.Spin(['1.0000','0.50000', '0.20000', '0.10000', '0.01000', '0.00100', '0.00010', '0.00001'], key='INPUT1'), sg.Button('Wprowadź', key='-GUZIK1')],
    [sg.Text('Dokładność wyznaczonego pierwiastka ', key='-TEXT2-')],
    [sg.Spin(['1.0000','0.500000', '0.200000', '0.100000', '0.010000', '0.001000', '0.000100', '0.000010', '0.000001'], key='INPUT2'), sg.Button('Wprowadź', key='-GUZIK2')],
    [sg.Text('Max iteracji petli'),sg.Slider(orientation ='horizontal',default_value=3, key='Slider', range=(1,10))],
    [sg.Text('======OBECNE USTAWIENIA=======')],
    [sg.Text('DYSKRETYZACJA = 0.50000', key='-TEXT3-')],
    [sg.Text('DOKLADNOSC = 0.500000', key='-TEXT4-')],
    [sg.Button('OBLICZ PIERWIASTEK', key='-BUTTON1')],
    [sg.Text('____________________WYNIK____________________')],
    [sg.Text('X1 = ', key='-WYNIK1-')],
    [sg.Text('X2 = ', key='-WYNIK2-')],
    [sg.Text('X3 = ', key='-WYNIK3-')],
    [sg.Text('_______________Powered by MJ_________________')]
]
window = sg.Window('Bisekcji', layout)
# pętla obsługująca zmiane stanów przycisków i okienek
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-GUZIK1':
        window['-TEXT3-'].update('DYSKRETYZACJA = ' + values[ 'INPUT1'])
        a = values['INPUT1']
        Dyskretyzacja = float((a))  # dokladnosc podzialki


    if event == '-GUZIK2':
        window['-TEXT4-'].update('DOKLADNOSC = ' +values['INPUT2'])
        b = values['INPUT2']
        Bi_Blad = float((b))


    if event == '-BUTTON1':
        ######################################################
        Fx = lambda x: x * x * x - 0.165 * x * x + 3.993 * 0.0001
        window['-WYNIK1-'].update('X1 = ')
        window['-WYNIK2-'].update('X2 = ')
        window['-WYNIK3-'].update('X3 = ')
        x = num.arange(ZP, ZK, Dyskretyzacja)
        y = num.vectorize(Fx)(x)
        pierwiastkow = 0
        set_num = y[0]
        roots = []
        max_krokow = int(values['Slider'])

        for i in range(len(y) - 1):
            if y[i] * set_num < 0:
                set_num = y[i]
                pierwiastkow += 1
                root = bisekcja(x[i - 1], x[i], Fx, max_krokow)
                roots.append(root)
                roots = [i for i in roots if i]  # remove None

        if len(roots) > 0:
            window['-WYNIK1-'].update('X1 = ' + str(roots[0]))
        if len(roots) > 1:
            window['-WYNIK2-'].update('X2 = ' + str(roots[1]))
        if len(roots) > 2:
            window['-WYNIK3-'].update('X3 = ' + str(roots[2]))
     
window.close()



