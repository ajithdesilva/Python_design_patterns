

from base.cake import Cake
class PlainCake(Cake):
    def describe(self) -> str:
        return "Plain Cake"

    def cost(self) -> float:
        return 10.0