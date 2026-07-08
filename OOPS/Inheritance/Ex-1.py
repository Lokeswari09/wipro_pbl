class Animal:
    def eat(self):
        print("Animal is eating")
    def sleep(self):
        print("Animal is sleeping")
class Bird(Animal):
    def eat(self):
        print("Bird is eating")
    def sleep(self):
        print("Bird is sleeping")
    def fly(self):
        print("Bird is flying")
animal_instance=Animal()
animal_instance.eat()
animal_instance.sleep()
bird_instance=Bird()
bird_instance.eat()
bird_instance.sleep()
bird_instance.fly()