
from cakemaker.base.cakemaker import CakeMaker
from cakemaker.ovens.bakery.bakery_oven import BakeryOven

class BakeryOvenAdapter(CakeMaker):
    def __init__(self, fancy_machine: BakeryOven):
        self.fancy_machine = fancy_machine

    def make_cake(self):
        # Translate the expected interface to the 3rd-party interface
        self.fancy_machine.start_baking()
        return self.fancy_machine.get_result()
