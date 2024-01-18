
class Players:
    def __init__(self, name, age, weight, team):
        self.name = name
        self.age = age
        self.weight = weight
        self.team = team

    def show(self):
        print(self.name, self.age, self.team, sep='\n')

    def is_young(self):
        if 16 <= self.age <= 35:
            return True
        else:
            return False

p = Players('Mikhail', 15, 80, 'Inter')

p.show()
print(p.is_young())
