from tkinter import *
import keyboard
import Keyboard_Control as keyboard1
#import Windows_Control as windows
import Volume_Control as volume
import Youtube_Control as youtube

import time

def nothing(arg):
    pass


Function_Dict = {"rot":youtube.Open_Youtube,
                 "touch": youtube.Open_Youtube,
                 "light": nothing,
                 #"button": windows.Toggle_Brightness,
                 "click": keyboard1.Enter,
                 "encoder": keyboard1.Scroll_Windows}


def GUI():
    rotItem = ''
    touchItem = ''
    lightItem = ''
    #buttonActItem = ''
    clickItem = ''
    encoderItem = ''

    tk = Tk()
    tk.title("Sensors and Actions")
    tk.geometry("400x200+300+200")

    rotVar = StringVar()
    touchVar = StringVar()
    lightVar= StringVar()
    clickVar = StringVar()
    encoderVar = StringVar()

    rotVar.set("YouTube")
    touchVar.set("Space")
    lightVar.set("Scroll Windows2")
    clickVar.set("New Tab")
    encoderVar.set("Scroll Windows")

    print("ahhh")


    '''
    def getTouchItem():
        touchItem = touchVar.get()
        if touchItem == 'YouTube':
            if keyboard.is_pressed('b'):
                Function_Dict["rot"] = youtube.Open_Youtube
                youtube.Open_Youtube(1)
            Function_Dict['touch'] = youtube.Open_Youtube

        elif touchItem == 'Toggle Brightness':
            Function_Dict['touch'] = windows.Toggle_Brightness


    def getLightItem():
        lightItem = lightVar.get()



    def getEncoderItem():
        encoderItem = encoderVar.get()
        if encoderItem == 'Scroll Windows':
            #if keyboard.is_pressed('e'):
            Function_Dict['encoder'] = keyboard1.Scroll_Windows
            #keyboard1.Scroll_Windows(0)
        elif encoderItem == 'Scroll Tabs':
            #if keyboard.is_pressed('e'):
            Function_Dict['encoder'] = keyboard1.Scroll_Tabs
            #keyboard1.Scroll_Tabs(0)
    '''



    Label(tk, text="a:").grid(column=0,row=0)
    Label(tk, text="b:").grid(column=0,row=1)
    Label(tk, text="c:").grid(column=0,row=2)
    Label(tk, text="d:").grid(column=0,row=3)
    Label(tk, text="e:").grid(column=0,row=4)

    '''
    def getRotItem(val):
        rotItem = rotVar.get()
        if (rotItem == "YouTube"):
            Function_Dict["rot"] = youtube.Open_Youtube
            #youtube.Open_Youtube(1)

        elif (rotItem == "New Tab"):
            Function_Dict["rot"] = youtube.Open_New_Tab
            #youtube.Open_New_Tab(1)
    

    def getClickItem(val):
        clickItem = clickVar.get()
        if clickItem == 'New Tab':
            Function_Dict['click'] = youtube.Open_New_Tab
        elif clickItem == 'Close Tab':
            Function_Dict['click'] = keyboard1.Ctrl_W
            
    '''

    def rotDef(rotVar):

        if (rotVar == "YouTube"):
            if keyboard.is_pressed('a'):
                Function_Dict["rot"] = youtube.Open_Youtube
                youtube.Open_Youtube(1)

        elif (rotVar == "New Tab"):
            if keyboard.is_pressed('a'):
                Function_Dict["rot"] = youtube.Open_New_Tab
                youtube.Open_New_Tab(1)

    def touchDef(touchVar):
        if touchVar == 'Space':
            keyboard1.Space(0)
            if keyboard.is_pressed('b'):
                Function_Dict['touch'] = keyboard1.Space
                keyboard1.Space(1)
                time.sleep(0.25)

        elif touchVar == 'Backspace':
            keyboard1.BackSpace(0)
            if keyboard.is_pressed('b'):
                Function_Dict['touch'] = keyboard1.BackSpace
                keyboard1.BackSpace(1)
                keyboard1.BackSpace(1)
                time.sleep(0.25)

    def lightDef(lightVar):
        if lightVar == 'Scroll Windows2':
            keyboard1.Scroll_Windows(0)
            if keyboard.is_pressed('c'):
                #print("cccc")
                Function_Dict['encoder'] = keyboard1.Scroll_Windows
                keyboard1.Scroll_Windows(0)
                time.sleep(0.25)

        elif lightVar == 'Scroll Tabs2':

            keyboard1.Scroll_Tabs(0)
            if keyboard.is_pressed('c'):
                #print("cccccc")
                Function_Dict['encoder'] = keyboard1.Scroll_Tabs
                keyboard1.Scroll_Tabs(0)
                time.sleep(0.25)

    def clickDef(clickVar):
        #print(clickVar)
        if clickVar == 'New Tab':
            if keyboard.is_pressed('d'):
                Function_Dict['click'] = youtube.Open_New_Tab
                youtube.Open_New_Tab(1)

        elif clickVar == 'Delete Tab':
            keyboard1.Ctrl_W(0)
            if keyboard.is_pressed('d'):
                Function_Dict['click'] = keyboard1.Ctrl_W
                keyboard1.Ctrl_W(1)
                time.sleep(0.25)

    def encoderDef(encoderVar):
        if encoderVar == 'Scroll Windows':
            keyboard1.Scroll_Windows(0)
            if keyboard.is_pressed('e'):
                #print("eeee")
                Function_Dict['encoder'] = keyboard1.Scroll_Windows
                keyboard1.Scroll_Windows(1)
                time.sleep(0.25)

        elif encoderVar == 'Scroll Tabs':
            keyboard1.Scroll_Tabs(0)
            if keyboard.is_pressed('e'):
                #print("eeee")
                Function_Dict['encoder'] = keyboard1.Scroll_Tabs
                keyboard1.Scroll_Tabs(1)
                time.sleep(0.25)

    rot = OptionMenu(tk, rotVar, "YouTube", "New Tab", command=rotDef)
    touch = OptionMenu(tk, touchVar, "Space", "Backspace", command=touchDef)
    light = OptionMenu(tk, lightVar, "Scroll Windows2", "Scroll Tabs2", command=lightDef)
    click = OptionMenu(tk, clickVar, "Delete Tab", "New Tab", command=clickDef)
    encoder = OptionMenu(tk, encoderVar, "Scroll Windows", "Scroll Tabs", command=encoderDef)


    rot.config(width=16)
    rot.grid(column=1, row=0)
    touch.config(width=16)
    touch.grid(column=1, row=1)
    light.config(width=16)
    light.grid(column=1, row=2)
    click.config(width=16)
    click.grid(column=1, row=3)
    encoder.config(width=16)
    encoder.grid(column=1, row=4)




    while True:
        rotDef(rotVar.get())
        clickDef(clickVar.get())
        encoderDef(encoderVar.get())
        touchDef(touchVar.get())
        lightDef(lightVar.get())

        #print("yes")
        tk.update_idletasks()
        tk.update()

GUI()