from for_import import Queue

class Dog:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.type = "dog"

class Cat:
    def __init__(self, name):
        self.name = name
        self.next = None
        self.type = "cat"

class AnimalShelter :
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self,animal):
        if animal.type == 'dog':
            self.dog.enqueue(animal.name)
            print('Add Dog')

        elif animal.type == 'cat':
            self.cat.enqueue(animal.name)
            print('Add Cat')

    def dequeue(self, pref):

        if pref == "dog":
            self.dog.dequeue()

        elif pref == "cat":
            self.cat.dequeue()

        else:
            return 'Null'

# if __name__ == "__main__":
    # dog1 = Dog("Oscar")
    # dog2 = Dog("Max")
    # cat1 = Cat("kitty")
    # cat2 = Cat("mshmesh")

    # animal_shelter = AnimalShelter()
    # animal_shelter.enqueue(dog1)
    # animal_shelter.enqueue(dog2)
    # animal_shelter.enqueue(cat1)
    # animal_shelter.enqueue(cat2)
    # print(animal_shelter.cat)
    # print(animal_shelter.dog)
    # animal_shelter.dequeue("cat")
    # print(animal_shelter.cat)


