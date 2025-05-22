import time
import pyautogui
pyautogui.FAILSAFE = True

#posicoes

# nova aba = x=324, y=891
# criar visualizacoes = x=74, y=126
# quantidade de divisao = x=125, y=822
# 16 visualizações = x=169, y=611
# segunda tela = x=-1184, y=239
# nova aba = x=295, y=22
# funcoes
def abrir_sim_next():
    pyautogui.hotkey('f8')
    time.sleep (13)
    pyautogui.hotkey('win', 'up')
    time.sleep (0.5)

def abrir_sandboxie():
    pyautogui.hotkey('f7')
    time.sleep(3)

def criar_visualização_16_next():#Criar 3 visualizações em 3 telas das TVs
    pyautogui.click(x=291, y=21, clicks=1, button='left',duration=0.5) #nova aba
    time.sleep(0.2)
    pyautogui.click(x=74, y=126, clicks=1, button='left',duration=0.2) #visualizacao
    time.sleep(7)
    pyautogui.click(x=125, y=822, clicks=1, button='left', duration=0.5) #quantidade de divisao
    time.sleep(0.8)
    pyautogui.click(x=169, y=611, clicks=1, button='left', duration=0.2) #16visualizacoes
    time.sleep(0.2)

abrir_sim_next()
#criar_visualização_16_next()

#pyautogui.click(x=73, y=129, clicks=1, button='left')sim next
# COLOCAR CLIQUE DA VISUALIZACAO
# REPETIR PROCESSO DO CRIAR VISUALIZACOES_16_NEXT 3 VEZES