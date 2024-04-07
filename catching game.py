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
            
class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("bob.jpg")
        self.sandwich_sound = simpleGE.Sound("sandwich_catching_sound.mp3")
        self.num_sandwiches = 5
        self.steve = Steve(self)
        
        self.sandwiches = [] 
        for i in range(self.num_sandwiches):
            self.sandwiches.append(Sandwich(self))
        self.sprites = [self.steve,self.sandwiches]
   
    def process(self):
        for sandwich in self.sandwiches:
            if sandwich.collidesWith(self.steve):
                sandwich.reset()
                self.sandwich_sound.play()
        

def main():
    game = Game()
    game.start()

if __name__ == "__main__":
    main()

