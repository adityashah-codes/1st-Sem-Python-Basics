class Dog:
    species = "Canis"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def desciption(self):
        return f"{self.name} is {self.age} Years old"
        
    def __str__(self):
        return f"{self.name} is {self.age} Years old"
    
print(Dog.species)

ollama = Dog("ollama", 7)

print(ollama.desciption())

print(ollama)