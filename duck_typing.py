class Duck:
    def swim(self):
        print("Swim Duck")

    def fly(self):
        print("Fly duck")

class Whale:
        def swim(self):
            print("Swim whale")

animals=[Duck(),Duck(),Whale()]

for animal in animals:
     animal.swim()
     animal.fly()