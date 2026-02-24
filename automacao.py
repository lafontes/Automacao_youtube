import pyautogui as pa #para controlar o mouse e o teclado.
import time #para ajustar o tempo de execução.
pa.PAUSE = 1 #tempo de espera entre cada comando.

pa.press('win') 
pa.write("chrome")
pa.press('ENTER')
pa.write("https://www.youtube.com")
pa.press('ENTER')
time.sleep(5) #espera 5 segundos para a página carregar.
pa.click(x=646, y=174) #para verificar a posição do mouse
pa.write("python")
pa.press('ENTER')
