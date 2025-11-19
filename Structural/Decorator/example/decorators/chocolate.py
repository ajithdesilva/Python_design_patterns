

from base.decorator import CakeDecorator

# --- Concrete Decorators ---
class ChocolateDecorator(CakeDecorator):
    def describe(self) -> str:
        return self._cake.describe() + ", Chocolate Layer"

    def cost(self) -> float:
        return self._cake.cost() + 2.5