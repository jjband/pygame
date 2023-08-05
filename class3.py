class God():
    def __init__(self, name, age, country, height):
        self.name = name
        self.age = age
        self.country = country
        self.height = height
    def introduce(self):
        print(f"나의 이름은 {self.name}이고 나이는{self.age}살, 국적은{self.country} 입니다 그리고 키는{self.height} 입니다")
a = God("김철수", 13, "대한민국", 164)
b = God("마카타", 14 , "일본", 158)
c = God("잡", 20, "미국", 181)
d = God("그리즈만", 32, "프랑스", 178)
e = God("토마스 뮐러", 22,"독일", 176)
a.introduce()
b.introduce()
c.introduce()
d.introduce()
e.introduce()                                                                                                                                               


        