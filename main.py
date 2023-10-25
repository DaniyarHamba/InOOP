class Device:
    def __init__(self, model, price):
        self.model = model
        self.price = price


class CoffeeMachine(Device):
    def __init__(self, model, price, coffee):
        super().__init__(model, price)
        self.coffee = coffee

    def Hello():
        return f"Hello I'm coffe and i like "