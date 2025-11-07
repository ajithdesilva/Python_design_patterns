############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-06
#   Last Modified   :   2025-11-06
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


from factories.cake_factory import CakeFactory  ### Import the CakeFactory


def main():
    ### Create and prepare different types of cakes using the factory
    
     for cake_type in ["chocolate", "vanilla", "fruit"]:
        print(f"\n--- Making a {cake_type.title()} Cake ---")
        cake = CakeFactory.create_cake(cake_type)
        cake.prepare()
        cake.bake()
        cake.decorate()
        print(f"--- Making a {cake_type.title()} Cake --- ---- DONE")
        
        
if __name__ == "__main__":
    print("Welcome to the Cake Factory!")
    main()
    print("\nAll cakes are ready to be served!")