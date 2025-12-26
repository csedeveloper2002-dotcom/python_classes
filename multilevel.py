class Alpha:
    def show_alpha(self):
        print("This is Alpha class")

class Beta(Alpha):
    def show_beta(self):
        print("This is Beta class")

class Gamma(Beta):
    def show_gamma(self):
        print("This is Gamma class")


obj = Gamma()
obj.show_alpha()
obj.show_beta()
obj.show_gamma()
