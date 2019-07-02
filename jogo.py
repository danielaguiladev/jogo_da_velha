from time import sleep
from random import randint
import sys
import os

pts_jogador = 0
pts_pc = 0

def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clearConsole()
    j = ''
    primeiro = ''
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    lv = 'livre'
    pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = lv, lv, lv, lv, lv, lv, lv, lv, lv
    jogada = 0
    jog_adv = 0
    jogada_aleatoria = 0
    turnos = 1
    vencedor = ''

    tabuleiro_inicial = '''

Tabuleiro:

     |     |     
  1  |  2  |  3  
_____|_____|_____
     |     |     
  4  |  5  |  6  
_____|_____|_____
     |     |     
  7  |  8  |  9  
     |     |     
    '''

    print(tabuleiro_inicial)
    j = 'O'
    adv = 'X'
    primeiro = 'EU'

    def atualizar_tabuleiro():
        clearConsole()
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        tabuleiro = '''
     |     |   
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
_____|_____|_____
     |     |
  {}  |  {}  |  {}
     |     |
        '''.format(p1, p2, p3, p4, p5, p6, p7, p8, p9)
        print(tabuleiro)

    def jogada_j1():
        global jogada

        while True:
            try:
                jogada = int(input('Digite a posicao da sua jogada (1 a 9) e pressione Enter: '))
                break
            except ValueError:
                print('\nValor digitado invalido. Digite um número inteiro de 1 a 9!\n')

    def rotina_j1():
        global jogada
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        msg_ocupado = '\nEste espaço ja esta ocupado!\n'

        jogada_j1()

        while jogada not in range(1, (9 + 1)):
            jogada_j1()

            if jogada not in range(1, (9 + 1)):
                print('\nNumero invalido!\n')

        while jogada == 1 and pos1 == 'ocupada' or \
            jogada == 2 and pos2 == 'ocupada' or \
            jogada == 3 and pos3 == 'ocupada' or \
            jogada == 4 and pos4 == 'ocupada' or \
            jogada == 5 and pos5 == 'ocupada' or \
            jogada == 6 and pos6 == 'ocupada' or \
            jogada == 7 and pos7 == 'ocupada' or \
            jogada == 8 and pos8 == 'ocupada' or \
                jogada == 9 and pos9 == 'ocupada':
            print(msg_ocupado)
            rotina_j1()

    def atualizar_jogadas_j1():
        global jogada
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        if jogada == 1:
            p1 = j
            pos1 = 'ocupada'
        elif jogada == 2:
            p2 = j
            pos2 = 'ocupada'
        elif jogada == 3:
            p3 = j
            pos3 = 'ocupada'
        elif jogada == 4:
            p4 = j
            pos4 = 'ocupada'
        elif jogada == 5:
            p5 = j
            pos5 = 'ocupada'
        elif jogada == 6:
            p6 = j
            pos6 = 'ocupada'
        elif jogada == 7:
            p7 = j
            pos7 = 'ocupada'
        elif jogada == 8:
            p8 = j
            pos8 = 'ocupada'
        elif jogada == 9:
            p9 = j
            pos9 = 'ocupada'

    def atualizar_jogadas_j2():
        global jogada, jogada_aleatoria, adv
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9
        jogada_aleatoria = randint(1, 9)

        while jogada_aleatoria == 1 and pos1 == 'ocupada' or \
            jogada_aleatoria == 2 and pos2 == 'ocupada' or \
            jogada_aleatoria == 3 and pos3 == 'ocupada' or \
            jogada_aleatoria == 4 and pos4 == 'ocupada' or \
            jogada_aleatoria == 5 and pos5 == 'ocupada' or \
            jogada_aleatoria == 6 and pos6 == 'ocupada' or \
            jogada_aleatoria == 7 and pos7 == 'ocupada' or \
            jogada_aleatoria == 8 and pos8 == 'ocupada' or \
                jogada_aleatoria == 9 and pos9 == 'ocupada':
            jogada_aleatoria = randint(1, 9)

        if jogada_aleatoria == 1:
            p1 = adv
            pos1 = 'ocupada'
        elif jogada_aleatoria == 2:
            p2 = adv
            pos2 = 'ocupada'
        elif jogada_aleatoria == 3:
            p3 = adv
            pos3 = 'ocupada'
        elif jogada_aleatoria == 4:
            p4 = adv
            pos4 = 'ocupada'
        elif jogada_aleatoria == 5:
            p5 = adv
            pos5 = 'ocupada'
        elif jogada_aleatoria == 6:
            p6 = adv
            pos6 = 'ocupada'
        elif jogada_aleatoria == 7:
            p7 = adv
            pos7 = 'ocupada'
        elif jogada_aleatoria == 8:
            p8 = adv
            pos8 = 'ocupada'
        elif jogada_aleatoria == 9:
            p9 = adv
            pos9 = 'ocupada'

    def checar_vencedor():
        global j, adv, turnos, vencedor, pts_jogador, pts_pc
        global p1, p2, p3, p4, p5, p6, p7, p8, p9

        if p1 == j and p2 == j and p3 == j or \
           p1 == j and p4 == j and p7 == j or \
           p1 == j and p5 == j and p9 == j or \
           p2 == j and p5 == j and p8 == j or \
           p3 == j and p5 == j and p7 == j or \
           p3 == j and p6 == j and p9 == j or \
           p4 == j and p5 == j and p6 == j or \
           p7 == j and p8 == j and p9 == j:
            print('VOCE GANHOU!\n')
            pts_jogador += 1
            vencedor = 'EU'
            turnos = 10

        if p1 == adv and p2 == adv and p3 == adv or \
           p1 == adv and p4 == adv and p7 == adv or \
           p1 == adv and p5 == adv and p9 == adv or \
           p2 == adv and p5 == adv and p8 == adv or \
           p3 == adv and p5 == adv and p7 == adv or \
           p3 == adv and p6 == adv and p9 == adv or \
           p4 == adv and p5 == adv and p6 == adv or \
           p7 == adv and p8 == adv and p9 == adv:
            print('EU GANHEI!\n')
            pts_pc += 1
            vencedor = 'PC'
            turnos = 10

    def atualizar_tudo():
        global jogada
        global turnos
        global vencedor

        rotina_j1()
        atualizar_jogadas_j1()
        atualizar_tabuleiro()
        checar_vencedor()

        if turnos == 5:
            print('NOS EMPATAMOS!\n')
            turnos = 10
            vencedor = 'EMPATE'

        if vencedor == '':
            atualizar_jogadas_j2()
            atualizar_tabuleiro()
            checar_vencedor()
        jogada = 0
        turnos += 1

    while turnos <= 5:
        atualizar_tudo()

    print('-------- PLACAR --------')
    print('Voce: {} | Computador: {}'.format(pts_jogador, pts_pc))
    print('------------------------')

    while True:
        reiniciar = input('\nQuer jogar de novo? Digite S para sim ou N para nao: ').lower()
        if reiniciar in ('s', 'n', '"s"', '"n"'):
            clearConsole()
            break
        print('\nResposta invalida!')
    if reiniciar == 's' or reiniciar == '"s"':
        continue
    else:
        sys.exit(0)
