import time
import pyautogui
import os

os.chdir(r'C:\Users\Thiago\PycharmProjects\pythonProject')
partida = 'photos/aceitar2.PNG'
choose = 'photos/choose.PNG'
confirm = 'photos/confirm.PNG'
ref = 'photos/reference_champ.PNG'
search = 'photos/search.PNG'
ban = 'photos/ban.PNG'
banclick = 'photos/banclick.PNG'

def sc():
    pyautogui.click()
    time.sleep(0.5)
def gobutton():
    local0 = pyautogui.locateCenterOnScreen(partida, confidence =0.55)
    if local0 is not None:
        pyautogui.moveTo(local0)
        sc()
        print("aceito")
        time.sleep(1)


def phase(text, go, champ):
    local = pyautogui.locateCenterOnScreen(text, confidence=0.90)
    local2 = pyautogui.locateCenterOnScreen(search, confidence=0.90)
    if local and local2 is not None:
        pyautogui.moveTo(local2)
        sc()
        print("pesquisar")
        pyautogui.write(champ)
        print("escrito")
        refx, refy = pyautogui.locateCenterOnScreen(ref, confidence=0.50)
        if refx is not None:
            pyautogui.moveTo(refx, refy + 40)
            sc()
            local3 = pyautogui.locateCenterOnScreen(go, confidence=0.90)
            if local3 is not None:
                pyautogui.moveTo(local3)
                sc()
                print("confirmado")



banchamp = "Zed"
#banchamp2 = "Kog"
#banchamp3 = "Vi"
champ = "Neeko"

while True:
    gobutton()
    phase(ban, banclick, banchamp)
    phase(choose, confirm, champ)
