class Fighter():
    def __init__(self, model, missile):
        self.model = model
        self.missile = missile
    def attack(self):
        print(self.model+" 출격 !")
    def fire(self):
        print(self.missile+" 발사 !")

fighter1 = Fighter('박성현', '총알 ')
fighter1.fire()
fighter2 = Fighter("박건후", "ICBM")
fighter2.attack()
fighter3 = Fighter("박성후", "nuclear")