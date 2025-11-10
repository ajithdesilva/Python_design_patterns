
############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-10
#   Last Modified   :   2025-11-10
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows how we can use the prototype pattern to clone a instance.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

from base.cake import Cake
from store.cakestore import CakeStore


if __name__ == "__main__":
    # Create some cake prototypes that we need for the example
    chocolate_cake = Cake("Chocolate", "Medium", "Chocolate Ganache", ["Cherries", "Sprinkles"])
    vanilla_cake = Cake("Vanilla", "Small", "Vanilla Frosting", ["Strawberries"])
    
    # Register prototypes in the CakeStore. Those will be the valid cackes in our store
    store = CakeStore()
    store.register_cake("ChocolateCake", chocolate_cake)
    store.register_cake("VanillaCake", vanilla_cake)

    # Clone ChocolateCake cake from the store, modify it
    birthday_cake = store.create_cake("ChocolateCake")
    birthday_cake.size = "Large"
    birthday_cake.toppings.append("Birthday Candle")

    # Clone VanillaCake cake from the store, modify it
    wedding_cake = store.create_cake("VanillaCake")
    wedding_cake.size = "Extra Large"
    wedding_cake.toppings.extend(["Flowers", "Ribbons"])

    print("Birthday Cake:\n", birthday_cake)
    print("Wedding Cake:\n", wedding_cake)

    # Original prototypes remain unchanged
    print("Original Chocolate Cake Prototype:\n", chocolate_cake)
    print("Original Vanilla Cake Prototype:\n", vanilla_cake)
