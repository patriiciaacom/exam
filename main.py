#Sarcina1
# class Animal:
#     def __init__(self, specie, an):
#         self.specie = specie
#         self.an = an
#
#
# class Caine(Animal):
#     def __init__(self, specie, an, rasa):
#         super().__init__(specie, an)
#         self.rasa = rasa
#     def make_sound(self):
#         return "Ham-Ham"
#
#
# first_animal = Animal(specie="mamifer", an=5)
# print("Rasa:",first_animal.specie)
# print("An",first_animal.an)
#
# second_animal = Caine(specie="mamifer", an=3, rasa="chihuahua")
# print(second_animal.make_sound())
# print("Rasa2:", second_animal.specie)
# print("An2:", second_animal.an)
# print("Rasa2:", second_animal.rasa)

#Sarcina2
class Calculator:
    def __init__(self, min_numar, max_numar):
        self.min_numar = min_numar
        self.max_numar = max_numar
    def __iter__(self):
        self.min_numar = self.min_numar
        return self
    def __next__(self):
        self.min_numar += 1
        if self.min_numar > self.max_numar:
            raise StopIteration
        return self.min_numar
Calculator1 = Calculator(1, 6)
for elem in Calculator1:
    print(elem)