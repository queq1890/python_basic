class Car:
    def speed_up(self):
        print("加速します")

    def speed_down(self):
        print("減速します")

# pythonは親クラスを引数に取ることでクラスを継承できる

class PatrolCar(Car): #クラスの継承
    def siren(self):
        print("ピーポーピーポー")

class TruckCar(Car): #クラスの継承
    def carry(self):
        print("荷物を運びます")
