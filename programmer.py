class Programmer:
    def __init__(self, name, post):
        self.name = name
        self.post = post
        self.time = 0
        self.pricing = {"Junior": 10, "Middle": 15, "Senior": 20}
        self.pay = self.pricing[post]
        self.total = 0

    def work(self, time):
        """— отмечает
        новую
        отработку
        в
        количестве
        часов
        time;"""
        self.time += time
        self.total += time * self.pay

    def rise(self):
        """— повышает
        программиста;"""
        if self.post == "Junior":
            self.post = "Middle"
            self.pay = self.pricing[self.post]
        elif self.post == "Middle":
            self.post = "Senior"
            self.pay = self.pricing[self.post]
        else:
            self.pay += 1

    def info(self):
        """— возвращает
        строку
        для
        бухгалтерии
        в
        формате: < имя > < количество
        отработанных
        часов > ч. < накопленная
        зарплата > тгр."""
        return f"{self.name} {self.time}ч. {self.total}тгр."


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())