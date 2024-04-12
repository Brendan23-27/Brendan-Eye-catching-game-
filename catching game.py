# -*- coding: utf-8 -*-
"""
Brendan Eye 
sandwich
catch
game 
"""
import simpleGE, random, pygame

class Sandwich(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("sandwich.jpg")
        self.setSize(75,75)
        self.min_speed = 3
        self.max_speed = 8
        self.reset()
   
    def reset(self):
        self.y =10
        
        self.x = random.randint(0, self.screenWidth)
        
        self.dy = random.randint(self.min_speed,self.max_speed)
        
    def checkBounds(self):
        if self.bottom > self.screenHeight:
            self.reset()
        
class Steve(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("steve.png")
        self.setSize(150,150)
        self.position = (320,400)
        self.move_speed = 8
        

        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.move_speed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.move_speed
            
class Lbl_time(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = "Time left 10"
        self.center = (500,30)
        
            
class Lbl_score(simpleGE.Label):
    def __init__(self):
        super().__init__()
        self.text = ("score 0")
        self.center = (100, 30)
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("bob.jpg")
        self.response = "quit"
        self.sandwich_sound = simpleGE.Sound("sandwich_catching_sound.mp3")
        self.num_sandwiches = 5
        self.score = 0 
        
        self.timer = simpleGE.Timer()
        self.timer.totalTime = 10
        self.lbl_time= Lbl_time()
       
        self.steve = Steve(self)
        
        self.lbl_score = Lbl_score()
        
        self.sandwiches = [] 
        for i in range(self.num_sandwiches):
            self.sandwiches.append(Sandwich(self))
        self.sprites = [self.steve,self.sandwiches, self.lbl_score, self.lbl_time]
   
    def process(self):
        for sandwich in self.sandwiches:
            if sandwich.collidesWith(self.steve):
                sandwich.reset()
                self.sandwich_sound.play()
                self.score += 1 
                self.lbl_score.text = f"Score: {self.score}"
        self.lbl_time.text = f"Time Left: {self.timer.getTimeLeft():.2f}"
        if self.timer.getTimeLeft() < 0:
            print(f"Score: {self.score}")
            self.stop()

class Instructions(simpleGE.Scene):
    def __init__(self, prev_score):
            super().__init__()
            
            
            self.prev_score = prev_score
            
            self.setImage("bob.jpg")
            self.response = "quit"
            
            
            self.tutorial =  simpleGE.MultiLabel() 
            self.tutorial.textLines = ["you're running a sandwich shop in pittsburgh", 
                                     "you need to catch the sandwiches",
                                     "if the time runs out your custmers leave",
                                     "move left and right with the arrow keys"]
            self.tutorial.center = (320,240)
            self.tutorial.size = (500,250)
            
            self.button_play = simpleGE.Button()
            self.button_play.text = ("play")
            self.button_play.center = (100,400)
            
              
            self.button_quit = simpleGE.Button()
            self.button_quit.text = ("quit")
            self.button_quit.center = (540,400)
            
            self.lbl_score = simpleGE.Label()
            self.lbl_score.text = "last score 0"
            self.lbl_score.center = (320,400)
            
            self.lbl_score.text = f"last score: {self.prev_score}"
            
            self.sprites = [self.tutorial, self.button_play, self.button_quit, self.lbl_score]
            

    
    def process(self):
        if self.button_play.clicked:
            self.response = "play"
            self.stop() 
        
        if self.button_quit.clicked:
            self.response = ("quit")
            self.stop()
       
    
def main():
    keep_going = True
    last_score = 0 
    
    while(keep_going):   
        tutorial = Instructions(last_score)
        tutorial.start()
        if tutorial.response == "play":
            game = Game()
            game.start()
            last_score = game.score
        
        elif tutorial.response == "quit":
         keep_going = False
    
if __name__ == "__main__":
    main()

