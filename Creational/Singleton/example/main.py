############################################################################################
#   File            :   main.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-06
#   Last Modified   :   2025-11-06
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module uses a Singleton class Configuration
#       Only one instance of itself can exist throughout the program's lifecycle.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################


from libs.configuration import Configuration

if __name__=="__main__":
    print("\nApplication Singleton Test == START")

    _configuration=Configuration.getInstance()

    print(
    "\t\nMin => ",_configuration.Min,
    "\t\nMax => ",_configuration.Max,
    "\t\nLog File=> ",_configuration.LogFilePath,
    "\t\nDB Str =>",_configuration.DB_Connection_Str
    )
    
    _configuration=None

    print("\nApplication Singleton Test -- FINISHED")