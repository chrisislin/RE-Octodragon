import webbrowser
import keyword as key

def Open_Youtube(arg):
    if arg == 0:
        return
    try:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = "http://youtube.com/"
        webbrowser.get(chrome_path).open(url)
    except Exception as e:
        print(e)
def Open_New_Tab(arg):
    if arg == 0:
        return
    try:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = "https://google.com/"
        webbrowser.get(chrome_path).open(url)
    except Exception as e:
        print(e)