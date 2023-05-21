# AUTOMAÇÃO DE SISTEMAS E PROCESSOS COM PYTHON

import pyautogui
import time

pyautogui.PAUSE = 0.25

# Passo 1: Acessar o sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema")
pyautogui.press("enter")

time.sleep(3)

# Passo 2: Fazer login no sistema
pyautogui.click(x=1157, y=525)
pyautogui.write("gfcarvalho")

pyautogui.click(x=962, y=629)
pyautogui.write("12345")

pyautogui.click(x=1114, y=711)

time.sleep(3)
#print(pyautogui.position())