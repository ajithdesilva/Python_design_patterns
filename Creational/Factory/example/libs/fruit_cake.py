

############################################################################################
#   File            :   fruit_cake.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-07
#   Last Modified   :   2025-11-07
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module defines the FruitCake class for the Factory design pattern example.
#       Overrides the base Cake class methods to provide specific implementations for
#       preparing, baking, and decorating a chocolate cake.
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

from base.cake import Cake

class FruitCake(Cake):
    def prepare(self):
        print("Preparing red fruit cake with Pineapple, fresh berries,cocoa and red coloring...")

    def bake(self):
        print("Baking fruit cake  at 170°C for 35 minutes...")

    def decorate(self):
        print("Decorating fruit cake with cream cheese frosting!")