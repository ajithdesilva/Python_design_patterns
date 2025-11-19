

from base.decorator import CakeDecorator

class FruitDecorator(CakeDecorator):
    def describe(self) -> str:
        return self._cake.describe() + ", Fresh Fruits"

    def cost(self) -> float:
        return self._cake.cost() + 3.0