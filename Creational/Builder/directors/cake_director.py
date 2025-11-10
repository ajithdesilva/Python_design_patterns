
############################################################################################
#   File            :   director.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-10
#   Last Modified   :   2025-11-10
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows how we can use the Director class to create complex instance in steps.       
#       Client code uses the Director instance , which contains all the methods with different params.
#       
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

from  builders.cake_builder import CakeBuilder

class CakeDirector:
    def __init__(self, builder: CakeBuilder):
        self.builder = builder
   
    def builder(self,builder: CakeBuilder):
        """
        make director to work with any bulder passed by the client code
        """
        self.builder=builder

    def make_chocolate_cake(self):        
        self.builder.add_layer("chocolate sponge")
        self.builder.add_layer("chocolate mousse")
        self.builder.add_frosting("dark chocolate ganache")
        self.builder.add_topping("chocolate curls")
        

    def make_fruit_cake(self):
        self.builder.add_layer("fruit mix base")
        self.builder.add_layer("spice sponge")
        self.builder.add_frosting("glazed fruit syrup")
        self.builder.add_topping("dried fruits & nuts")
        


    def make_cake(self,type="chocolate"):
        if type=="chocolate":
            self.builder.add_layer("chocolate sponge")
        else:
            self.builder.add_layer("fruit mix base")
        

