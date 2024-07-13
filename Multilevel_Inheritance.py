#multilevel_inheritance

class plants:
    def greens(self, name):
        self.name = name
        return f"{self.name} is the health food"

class mammal(plants):
    def goat(self, bread_name):
        self.bread_name = bread_name
        return f"{self.bread_name} can eat {self.name}"

class humans(mammal):
    def man(self):
        return f"human can eat both {self.name}  and {self.bread_name}"

obj = humans()
obj.greens("Moringa leaves")
obj.goat("Jamunapari")
print(obj.man())