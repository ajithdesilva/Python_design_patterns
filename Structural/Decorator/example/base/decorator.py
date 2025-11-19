from base.cake import Cake

# --- Base Decorator ---
class CakeDecorator(Cake):
    def __init__(self, cake: Cake):
        self._cake = cake

    def describe(self) -> str:
        return self._cake.describe()

    def cost(self) -> float:
        return self._cake.cost()