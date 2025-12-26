class Alpha:
    def show_alpha(self):
        print("This is Alpha class")

class Beta(Alpha):
    def show_beta(self):
        print("This is Beta class")


obj = Beta()
obj.show_alpha()
obj.show_beta()
