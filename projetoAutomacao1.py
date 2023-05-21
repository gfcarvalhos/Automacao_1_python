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

time.sleep(5)

# Passo 2: Fazer login no sistema
pyautogui.click(x=820, y=475)
pyautogui.write("gfcarvalho")
pyautogui.click(x=787, y=578)
pyautogui.write("12345")
pyautogui.click(x=950, y=652)

time.sleep(3)
#print(pyautogui.position())

# Passo 3: Baixar base dados
pyautogui.click(x=486, y=533, button = "right")
pyautogui.click(x=589, y=839)

# Passo 4: Calcular indicadores



#Passo 5: Enviar e-mail