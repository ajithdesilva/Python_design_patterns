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

class NormalOven(CakeMaker):
    def make_cake(self):
        return "🍰 Cake baked using Normal Oven"
