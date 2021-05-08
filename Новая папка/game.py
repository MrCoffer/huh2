from pygame import*
w=400
h=300

win = display.set_mode((w,h))

while True:
    
    for e in event.get():
        if e.type == 12:
            exit()
    win.fill((229,190,1))
    display.update()

