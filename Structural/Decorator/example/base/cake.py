from abc import ABC, abstractmethod

# --- Component Interface ---
class Cake(ABC):
    @abstractmethod
    def describe(self) -> str:
        pass

    @abstractmethod
    def cost(self) -> float:
        pass
