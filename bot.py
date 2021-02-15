import pyautogui
import time
print("Script creado por SantiModsz")
print("Recuerda leer el archivo README.MD")
time.sleep(0.5)
print("Cargando.")
time.sleep(1)
print("Cargando..")
time.sleep(1)
print("Cargando...")
time.sleep(1)
print("Script cargado con exito")
f = open("texto", 'r')
for word in f:
	pyautogui.typewrite(word)
	pyautogui.press("enter")
