

from base.decorator import CakeDecorator

class CreamDecorator(CakeDecorator):
    def describe(self) -> str:
        return self._cake.describe() + ", Whipped Cream"

    def cost(self) -> float:
        return self._cake.cost() + 1.5