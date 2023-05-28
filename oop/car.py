class Car(object):
    def __init__(self, model_name, mileage, manufacture):
        self.model_name = model_name
        self.mileage = mileage
        self.manufacture = manufacture

    def gas(self):
        print(f"{self.model_name} is gas Car")
        print("{0.manufacture}の{0.model_name}(燃費：{0.mileage}), アクセル全開！".format(self))

    def breaks(self):
        print(f"{self.model_name} is bresks")


if __name__ == "__main__":
    prius = Car("Prius", 100000, "TOYOTA")
    print(prius.model_name)
    print(prius.mileage)
    print(prius.manufacture)
    prius.gas()
    prius.breaks()
