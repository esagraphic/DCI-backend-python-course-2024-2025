from dog import Dog

class GermanShepard(Dog):
    def walk(self):
        super().walk()
        print("German Shepards show their beautiful fur while running.")