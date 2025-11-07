############################################################################################
#   File            :   no_singleton.py
# #   Author        :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-07
#   Last Modified   :   2025-11-07
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module defines a collection of Constants that can be used accross the application.
#       No singleton pattern is applied here.
#       Constants are defined as module-level variables.
#       Configuration constants are not well grouped.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

### define  global constants for application configuration.
### will be used in multiple modules.
CONFIG_NAME = "APP1_CONFIG"
CONFIG_VERSION = "1.0.0"
CONFIG_DB_HOST = "localhost"
CONFIG_DB_PORT = 5432
CONFIG_DB_USER = "admin"
CONFIG_DB_PASSWORD = "password" 
CONFIGB_DB_NAME = "app1_db"


if __name__=="__main__":
    print("App Test with constants -- START")
    
    ### print configuration constants
    print(f"Configuration Name: {CONFIG_NAME}")
    print(f"Configuration Version: {CONFIG_VERSION}")
    print(f"Database Host: {CONFIG_DB_HOST}")
    print(f"Database Port: {CONFIG_DB_PORT}")
    print(f"Database User: {CONFIG_DB_USER}")
    print(f"Database Password: {CONFIG_DB_PASSWORD}")
    
    print("App Test with constants -- END")
