import time
import ctypes  # An included library with Python install.
def Mbox(title, text, style):
    return ctypes.windll.user32.MessageBoxW(0, text, title, style)
Mbox("GO TO BED!!", "It's !", 1)

time.strftime('%l:%M%p %z on %b %d, %Y')