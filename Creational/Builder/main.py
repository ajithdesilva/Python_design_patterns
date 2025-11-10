
############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-10
#   Last Modified   :   2025-11-10
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module shows how we can use the builder pattern to create complex instance in steps.       
#       Client code uses the Director instance , which contains all the methods with different params.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################
# # main.py
from builders.cake_builder import CakeBuilder
from directors.cake_director import CakeDirector

def main():

    # Build Chocolate Cake - Default
    cake_builder1=CakeBuilder()     ### create the required builder
    cake_director1 = CakeDirector(cake_builder1)    ### create the director with the builder
    cake_director1.make_cake()
    print("\n Default Cake Built:\n",cake_builder1.get_cake())

    # Build Chocolate Cake - Default    
    cake_builder2=CakeBuilder()
    cake_director2 = CakeDirector(cake_builder2)
    cake_director2.make_chocolate_cake()
    print("\n🍫 Chocolate Cake Built:\n",cake_builder2.get_cake())


    # Build Fruit Cake - Default
    cake_builder_3= CakeBuilder()
    cake_director3 = CakeDirector(cake_builder_3)
    cake_director3.make_fruit_cake()
    print("\n🍓 Fruit Cake Built:\n",cake_builder_3.get_cake())
    
    ### ??? can we use Bulder pattern without Director ????

    

if __name__ == "__main__":
    main()
