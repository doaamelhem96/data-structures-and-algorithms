class Animal:
    '''
    A Class to  initializes instances with two arguments species and name
    '''
    def __init__(self, species, name):
        self.species = species
        self.name = name

class AnimalShelter:
    '''
    A class initializes instances dogs and cats lists
    '''
    def __init__(self):
        self.dogs = []
        self.cats = []

    def enqueue(self, animal):# define enqueue which append animals name to our previous lists like dogs and cats
        if animal.species == "dog":
            self.dogs.append(animal.name)
        elif animal.species == "cat":
            self.cats.append(animal.name)

    def dequeue(self, pref):# to pop these animals from my lists and when insert data differs from cat && dog returns None
        if pref == "dog":
            if self.dogs:
                return self.dogs.pop(0)
        elif pref == "cat":
            if self.cats:
                return self.cats.pop(0)
        return None

if __name__ == "__main__":
    shelter = AnimalShelter()
    shelter.enqueue(Animal("dog", "boby"))
    shelter.enqueue(Animal("cat", "kitty"))

    print(shelter.dequeue("dog"))  # Output: "boby"
    print(shelter.dequeue("cat"))  # Output: "kitty"
    print(shelter.dequeue("dog"))  # Output: None
