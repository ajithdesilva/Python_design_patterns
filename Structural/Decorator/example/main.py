
############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-19
#   Last Modified   :   2025-11-19
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module defines a Decorater design pattern
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

### import decorators
from decorators.chocolate import ChocolateDecorator
from decorators.creame import CreamDecorator
from decorators.fruit import FruitDecorator
from decorators.nuts import NutDecorator
from decorators.message import MessageDecorator


from cakes.plaincake import PlainCake


if __name__ == "__main__":
    cake = PlainCake()  ### create base cake that we need to decorate
    print("Description:", cake.describe())
    print("Total Cost: $", cake.cost())
    
    print("Starting Cake decoration .......")
    decorated_cake = ChocolateDecorator(cake)
    print("\tDescription:", decorated_cake.describe())
    print("\tTotal Cost: $", decorated_cake.cost())

    decorated_cake = CreamDecorator(decorated_cake)
    print("\tDescription:", decorated_cake.describe())
    print("\tTotal Cost: $", decorated_cake.cost())


    decorated_cake = FruitDecorator(decorated_cake)
    print("\tDescription:", decorated_cake.describe())
    print("\tTotal Cost: $", decorated_cake.cost())

    decorated_cake = NutDecorator(decorated_cake)
    print("\tDescription:", decorated_cake.describe())
    print("\tTotal Cost: $", decorated_cake.cost())

    decorated_cake = MessageDecorator(decorated_cake,"Happy Birthday!")
    print("\tDescription:", decorated_cake.describe())
    print("\tTotal Cost: $", decorated_cake.cost())
    
    print("Cake decoration ........... DONE")
