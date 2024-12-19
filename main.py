class Animal:
    def falar(self):
        print("Este animal faz um som.")

class Cachorro(Animal):
    def falar(self):
        print("O cachorro late.")

class Gato(Animal):
    def falar(self):
        print("O gato mia.")

animal = Animal()
cachorro = Cachorro()
gato = Gato()

animal.falar()
cachorro.falar()
gato.falar()