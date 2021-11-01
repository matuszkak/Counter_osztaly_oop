class Counter:
    def __init__(self, value):
        self.value = value
        self.step = 1
        # print('\nCounter created!')

    def increment(self):
        self.value = self.value + self.step

    def decrement(self):
        self.value = self.value - self.step

    def set_value(self, new_value):
        self.value = new_value
        return self.value

    def set_step(self, new_step):
        self.step = new_step
        return self.step

    def get_value(self):
        print(self.value)


class ScoreCounter(Counter):
    def __init__(self, value, name, age):
        super().__init__(value)
        self.name = name
        self.age = age
        self.winner = False

    # increment and decrement functions customised with winner check step added
    def increment(self):
        self.value = self.value + self.step
        self.winner = self.win_check()

    def decrement(self):
        self.value = self.value - self.step
        self.winner = self.win_check()

    # function checks is win value is reached
    def win_check(self):
        win_value = 12
        if self.value >= win_value:
            return True
        else:
            return False


print(f'\n##### 2.1 #####')
myCounter = Counter(10)
myCounter.increment()
myCounter.increment()
myCounter.get_value()
myCounter.set_step(5)
myCounter.decrement()
myCounter.get_value()
myCounter.set_value(100)
myCounter.increment()
myCounter.get_value()

print(f'\n##### 2.2 #####')
myScoreCounter = ScoreCounter(10, 'Zsolt', 34)

myScoreCounter.increment()
myScoreCounter.get_value()
myScoreCounter.increment()
myScoreCounter.get_value()
print(myScoreCounter.winner)
