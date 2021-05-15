from pygame import*
w=400
h=300

win = display.set_mode((w,h))
class Alfa(sprite.Sprite):
    def __init__(self,x,y,h,w,image_name,speed):
        super().__init__()
        self.image = image.load(image_name)
        self.rect = Rect(w,h,y,x)
        self.hface = "right"
        self.speed = speed
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))




class Ball(Alfa):
    def update(self):


        if self.hface == "right":
            self.rect.x += self.speed
            if self.rect.x > w:

                self.hface="left"

        
        else:
            if self.hface == "left":
                self.rect.x -= self.speed
                if self.rect.x < 0:

                    self.hface="right" 

        self.reset()
        

ball = Ball(100,100,100,100,'pixil-frame-0 (2).png',1) 

    

while True:
    
    for e in event.get():
        if e.type == 12:
            exit()
    win.fill((229,190,1))
    ball.update()
    display.update()

