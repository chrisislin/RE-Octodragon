from tkinter import *


def nothing(arg):
    pass

'''
Function_Dict = {"rot":volume.Set_Volume ,
                 "touch": youtube.Open_Youtube,
                 "light": nothing,
                 #"button": windows.Toggle_Brightness,
                 "click": keyboard.Enter,
                 "encoder": keyboard.Scroll_Windows}
'''

def GUI():
    '''

    rotItem = ''
    touchItem = ''
    lightItem = ''
    buttonActItem = ''
    clickItem = ''
    encoderItem = ''

    :return:
    '''


    tk = Tk()
    tk.title("Sensors and Actions")
    tk.geometry("400x200+300+200")

    rotVar = StringVar(tk)
    touchVar = StringVar(tk)
    lightVar= StringVar(tk)
    buttonActVar = StringVar(tk)
    clickVar = StringVar(tk)
    encoderVar = StringVar(tk)

    rotVar.set("Volume")
    touchVar.set("YouTube")
    lightVar.set("Auto-Dim")
    buttonActVar.set('Toggle Brightness')
    clickVar.set("Enter")
    encoderVar.set("Scroll Windows")


    '''
    
    def getRotItem(self):
        rotItem = rotVar.get()
        if (rotItem == "Volume"):
            Function_Dict["rot"] = volume.Set_Volume
        elif (rotItem == "Brightness"):
            "JUst clicked Brightness"
            Function_Dict["rot"] = windows.Change_Brightness
            
            
    def getTouchItem(self):
        touchItem = touchVar.get()
        if touchItem == 'YouTube':
            Function_Dict['touch'] = youtube.Open_Youtube
        elif touchItem == 'Toggle Brightness':
            Function_Dict['touch'] = windows.Toggle_Brightness
    
    def getLightItem(self):
        lightItem = lightVar.get()

    def getbuttonActItem(self):
        buttonActItem = buttonActVar.get()
        if buttonActItem == 'YouTube':
            Function_Dict['button'] = youtube.Open_Youtube
        elif buttonActItem == 'Toggle Brightness':
            Function_Dict['button'] = windows.Toggle_Brightness

    def getClickItem(self):
        clickItem = clickVar.get()
        if clickItem == 'Enter':
            Function_Dict['click'] = keyboard.Enter
        elif clickItem == 'New Tab':
            Function_Dict['click'] = youtube.Open_New_Tab
        elif clickItem == 'Close Tab':
            Function_Dict['click'] = keyboard.Ctrl_W

    def getEncoderItem(self):
        encoderItem = encoderVar.get()
        if encoderItem == 'Scroll Windows':
            Function_Dict['encoder'] = keyboard.Scroll_Windows
        elif encoderItem == 'Scroll Tabs':
            Function_Dict['encoder'] = keyboard.Scroll_Tabs
            
    def sendData(data):
        print("send data")
    '''


    Label(tk, text="Rot:").grid(column=0,row=0)
    Label(tk, text="Touch:").grid(column=0,row=1)
    Label(tk, text="Light:").grid(column=0,row=2)
    Label(tk, text="Button:").grid(column=0,row=3)
    Label(tk, text="Encoder:").grid(column=0,row=4)
    Label(tk, text="Encoder Click:").grid(column=0,row=5)

    rot = OptionMenu(tk, rotVar, "Volume", "Brightness")#, command=getRotItem())
    rot.config(width=16)
    rot.grid(column=1,row=0)
    touch = OptionMenu(tk, touchVar, "YouTube", "Toggle Brightness")#, command=getTouchItem)
    touch.config(width=16)
    touch.grid(column=1,row=1)
    light = OptionMenu(tk, lightVar, "Auto-Dim")#, command=getLightItem)
    light.config(width=16)
    light.grid(column=1,row=2)
    buttonAct = OptionMenu(tk, buttonActVar, "Toggle Brightness", "YouTube")#, command=getbuttonActItem)
    buttonAct.config(width=16)
    buttonAct.grid(column=1,row=3)
    click = OptionMenu(tk, clickVar, "Enter", "New Tab", "Close Tab")#, command=getClickItem)
    click.config(width=16)
    click.grid(column=1,row=4)
    encoder = OptionMenu(tk, encoderVar, "Scroll Windows", "Scroll Tabs")#,  command=getEncoderItem)
    encoder.config(width=16)
    encoder.grid(column=1,row=5)

    button = Button(tk, text="OK")#, command=getRotItem)

    while True:
        tk.update_idletasks()
        tk.update()
GUI()