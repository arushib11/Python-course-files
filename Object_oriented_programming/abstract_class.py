'''import random

class AbstractGame:
    def start(self):
        while True:
            start=input("Would you like to play? ")
            if start.lower()=="yes":
                break
        self.play()

    def end(self):
        print("The game has ended.")
        self.reset()

    def play(self):
        raise NotImplementedError("You must implement play()")
    
    def reset(self):
        raise NotImplementedError("You must implement reset()")

class AnotherGame:
    pass

class RandomGuesser(AbstractGame):
    def __init__(self,rounds):
        self.rounds=rounds
        self.round=0
    
    def reset(self):
        self.round=0

    def play(self):
        while self.round<self.rounds:
            self.round+=1

            print(f"Welcome to round {self.round}. Let's begin")
            random_num=random.randint(0,10)
            while True:
                guess=input("Enter a number between 1-10: ")
                if int(guess)==random_num:
                    print("You got it!")
                    break
        self.end()


#game=RandomGuesser(1)
#game.play()
        
games=[RandomGuesser(1),AnotherGame()]

for game in games:
    game.start()'''

class AbstractAnimal:
    def sleep(self):
        print("ZzzZzz")

    def animal_sound(self):
        raise NotImplementedError("Need to implement animal_sound()")
    
    def wake_up(self):
        self.animal_sound()
        print("I am awake!")

class Lion(AbstractAnimal):
    def animal_sound(self):
        print("Roar!")