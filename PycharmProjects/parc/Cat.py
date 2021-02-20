from Animal import Animal


class Cat(Animal):

    def __init__(self,name,colour,age,sex):
        self.maofa = "短毛"
        super().__init__(name,colour,age,sex)

    def pro(self):
        print("我会捉老鼠")

    def cry(self):
        print("喵喵叫")


