import keyboard
from time import sleep

def Scroll_Windows(arg):
    if arg == 0:
        Alt_Tab()
    else:
        Alt_Shift_Tab()
def Scroll_Tabs(arg):
    if arg == 0:
        Ctrl_Tab()
    else:
        Ctrl_Shift_Tab()

def Tab():
    keyboard.press_and_release('tab')

def Shift_Tab():
    keyboard.press_and_release('shift, tab')

def Enter(arg):
    if arg == 0:
        return
    keyboard.press_and_release('enter')

def Shift():
    keyboard.press_and_release('shift')


def Ctrl():
    keyboard.press_and_release('left ctrl')

def BackSpace():
    keyboard.press_and_release('backspace')


def B_Back():
    keyboard.press_and_release('alt, left arrow')


def B_Favorite():
    keyboard.press_and_release('alt, left arrow')


def B_Forward():
    keyboard.press_and_release('left ctrl, shift, t')



def Alt_Tab():
    keyboard.press_and_release('alt,tab ')

def Alt_Shift_Tab():
    keyboard.press_and_release('alt,shift, tab')

def Ctrl_Tab():
    keyboard.press_and_release('left ctrl, tab')


def Ctrl_Shift_Tab():
    keyboard.press_and_release('left ctrl, shift,  tab')

def Ctrl_W(arg):
    if arg == 0:
        return
    keyboard.press_and_release('left ctrl+w')
