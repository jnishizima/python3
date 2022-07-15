import pyautogui 
#import webbrowser as wb
import time

#wb.open('web.whatsapp.com')
time.sleep(30)
i = 0
qtdRepeticao = 20
while i < qtdRepeticao:
    pyautogui.typewrite('Mensagem')
    pyautogui.press('ENTER')
    i+=1
