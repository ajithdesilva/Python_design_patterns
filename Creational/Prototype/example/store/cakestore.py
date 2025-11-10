
############################################################################################
#   File            :   cakestore.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-10
#   Last Modified   :   2025-11-10
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module manage the prototyping of cakes
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################


class CakeStore:
    def __init__(self):
        self._prototypes = {}   ### cake holder

    def register_cake(self, name, cake):
        """Register a cake prototype with a name"""
        self._prototypes[name] = cake

    def create_cake(self, name):
        """Clone a registered cake prototype"""
        cake = self._prototypes.get(name)
        if not cake:
            raise ValueError(f"Cake '{name}' is not registered!")
        return cake.clone()
