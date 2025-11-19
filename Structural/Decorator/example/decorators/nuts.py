

from base.decorator import CakeDecorator

class NutDecorator(CakeDecorator):
    def describe(self) -> str:
        return self._cake.describe() + ", Crushed Nuts"

    def cost(self) -> float:
        return self._cake.cost() + 2.0