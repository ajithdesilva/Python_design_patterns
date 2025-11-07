
############################################################################################
#   File            :   vanilla_cake.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-07
#   Last Modified   :   2025-11-07
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module defines the VanillaCake class for the Factory design pattern example.
#       Overrides the base Cake class methods to provide specific implementations for
#       preparing, baking, and decorating a chocolate cake.
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

from base.cake import Cake

class VanillaCake(Cake):
    def prepare(self):
        print("Preparing vanilla batter with eggs and vanilla essence...")

    def bake(self):
        print("Baking vanilla cake at 175°C for 25 minutes...")

    def decorate(self):
        print("Decorating vanilla cake with buttercream!")