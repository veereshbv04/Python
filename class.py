#class learnings
class human():
    def __init__(self,n,o):
        self.name=n
        self.occupation=o

    def work(self):
        if self.occupation =="Tennies" :
            print(self.name,"palys tennies")
        elif self.occupation =="Actor":
            print(self.name ,"do acting")

    def speak(self):
        print(self.name,"how are you")
        
tom=human("tom","Actor")
tom.work()
tom.speak()
maria=human("maria","Tennies")
maria.work()
maria.speak()
