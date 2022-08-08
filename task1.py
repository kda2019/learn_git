class House:
    def __init__(self):
        self.t = 20

    def konder(self, x=1):
        self.t -= x
        print(f'Вы охладили помещение на {x} градусов')

    def batareya(self, x=1):
        self.t += x
        print(f'Вы нагрели помещение на {x} градусов')
