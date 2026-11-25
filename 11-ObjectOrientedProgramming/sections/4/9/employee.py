class C:
    def __init__(self, name, surname, age, seniority):
        self.name = name # imie
        self.surname = surname # nazwisko
        self.age = age # wiek
        self.seniority = seniority # staz pracy

    def __str__(self):
        result = self.surname + self.name[0] + str(self.seniority)
        if self.age >= 18:
            return result.upper() # duze litery
        return result.lower() # male litery


print(C("Anna", "May", 17, 7))
print(C("George", "Brown", 21, 4))
