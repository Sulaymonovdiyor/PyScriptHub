from pynput import keyboard

keys = []

def on_press(key):
    global keys
    keys.append(key)
    print(f"{key} pressed")

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

print("".join([key.char for key in keys if hasattr(key, "char")]))
