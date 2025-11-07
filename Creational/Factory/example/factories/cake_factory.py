
############################################################################################
#   File            :   cake_factory.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-07
#   Last Modified   :   2025-11-07
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module uses a Factory design pattern to create cakes of different types.
#       It demonstrates the creation of chocolate, vanilla, and fruit cakes using a
#       centralized CakeFactory. Each cake type has its own preparation, baking, and decoration
#       methods.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################


from libs.chocolate_cake import ChocolateCake
from libs.vanilla_cake import VanillaCake
from libs.fruit_cake import FruitCake


class CakeFactory:
    @staticmethod
    #def create_cake(cake_type: str):
    #    cake_type = cake_type.lower()
    #    if cake_type not in CAKE_COLLECTION:
    #        raise ValueError(f"Unknown cake type: {cake_type}")
    #    return CAKE_COLLECTION[cake_type]()  # instantiate and return
    
    def create_cake(cake_type: str):
        cake_type = cake_type.lower()

        if cake_type == "chocolate":
            return ChocolateCake()
        elif cake_type == "vanilla":
            return VanillaCake()
        elif cake_type == "fruit":
            return FruitCake()
        else:
            raise ValueError(f"Unknown cake type: {cake_type}")