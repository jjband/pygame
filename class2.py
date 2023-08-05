class Hello():
    def __init__(self, name):
        self.name = name
    def greeting(self):
        print(self.name + "안녕하세요")

    def goodbye(self):
        print("안녕히가세요!!")


a = Hello("박성현")
a.greeting()
a.goodbye()
b = Hello("박건후")
c = Hello("현성박")
b.greeting()