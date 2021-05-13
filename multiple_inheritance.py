class Father():
    def gardening(self):
        print("I enjoy gardening")

class Mother():
    def cooking(self):
        print("I enjoy cooking")

class Child(Father,Mother):
    #Father.gardening()
    def sports(self):
        print(" I love sports")

c=Child()
c.sports()
c.gardening()
c.cooking()
