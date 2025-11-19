

from base.decorator import CakeDecorator

class MessageDecorator(CakeDecorator):
    def __init__(self, cake, message):
        super().__init__(cake)
        self.message = message

    def describe(self) -> str:
        return self._cake.describe() + f', Message: "{self.message}"'

    def cost(self) -> float:
        return self._cake.cost() + 1.0