from sound import Sound


def Change_Volume(direction):
    if int(direction) == 1:
        Increase_Volume()
    else:
        Decrease_Volume()
def Increase_Volume():
    Sound.volume_up()

#Increase_Volume()

def Decrease_Volume():
    Sound.volume_down()

def Mute():
    Sound.mute()


def Max_Volume():
    Sound.volume_max()

def Min_Volume():
    Sound.volume_min()

def Get_Volume():
    return Sound.current_volume()

def Set_Volume(amount):
    Sound.volume_set(amount/1023*100)