class Bird:
    def __init__(self, name):
        self.name = name

    def sing(self):
        print(f"{self.name} is singing.")

    def fly(self):
        print(f"{self.name} is flying.")


class Parrot(Bird):
    def fly(self):
        super().fly()
        print(f"{self.name} is flying beautifully.")

    def talk(self):
        print(f"{self.name} can talk!")


generic_bird = Bird("Generic Bird")
generic_bird.sing()
generic_bird.fly()

parrot = Parrot("Polly")
parrot.sing()
parrot.fly()
parrot.talk()
