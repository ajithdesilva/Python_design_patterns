

############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-23-19
#   Last Modified   :   2025-23-19
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module defines a Adapter design pattern
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

from cakemaker.base.cakemaker import CakeMaker
from adaptors.bakery_oven_adaptor import BakeryOvenAdapter
from cakemaker.ovens.normal.normal_oven import NormalOven
from cakemaker.ovens.bakery.bakery_oven import BakeryOven

### bake today function
def bake_today(cake_maker: CakeMaker):
    print(cake_maker.make_cake())



def main():

    
    normal = NormalOven()   ### Normal Oven
    bake_today(normal)      ### Bake today with normal oven
    
    
    bakery_oven = BakeryOven()  ### Bakery Oven
    oven_adapter = BakeryOvenAdapter(bakery_oven)   ### Adapter for bakery oven
    
    bake_today(oven_adapter)    ### Bake today with bakery oven via adapter


if __name__ == "__main__":
    main() 