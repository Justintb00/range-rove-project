import keyboard

def returnInput():
    while True:
        key = keyboard.read_key()
        if key == 'esc':
            yield "Escape Key selected, end of function"
            break
        yield key

if __name__ == '__main__':
    for val in returnInput():
        print("Key Pressed ===> {key}".format(key=val))
