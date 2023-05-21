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
