############################################################################################
#   File            :   configuration.py
#   Author          :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-06
#   Last Modified   :   2025-11-06
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module defines a Singleton class that ensures
#       Only one instance of itself can exist throughout the program's lifecycle.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

class Configuration(object):
    """
    A singleton class that ensures only one instance of itself can exist.

    Use `Configuration.getInstance()` to get the single instance.
    Direct instantiation with `Configuration()` is not allowed and
    will raise a RuntimeError.
    """

    __instance = None   ### private fields to hold instance
    
    ### private fields to store values
    _min=0
    _max=0
    _logfile=""
    _db_connection_str=""

    def __new__(cls, val=None):
        ### stop creating a new instance directly
        raise RuntimeError(" Use getInstance() instead")

    
    @classmethod
    def getInstance(cls):
        """
        Returns the single instance of the class.

        Args:
            None
        
        Returns:
            Configuration: this singleton instance of "Configuration"

        """

        ### if NOT initialized, the DO it 
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._initialize()

        return cls.__instance


    def _initialize(self):
        self._max = 50
        self._min=10
        self._logfile="/var/log/app.log"
        self._db_connection_str="this is DB connection string"

        ### do further initialization here

    @property
    def Max(self):
        return self._max
    
    @property
    def Min(self):
        return self._min

    @property
    def LogFilePath(self):
        return self._logfile

    @property
    def DB_Connection_Str(self):
        return self._db_connection_str
