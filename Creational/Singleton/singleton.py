############################################################################################
#   File            :   singleton.py
# #   Author        :   Ajith de Silva (ajithdesilva@gmail.com)
#   Created         :   2025-11-06
#   Last Modified   :   2025-11-06
#   Version         :   1.0.0
############################################################################################
#   Description:
#       This module defines a Singleton class that ensures
#       Only one instance of itself can exist throughout the program's lifecycle.
#       Provides a global access point to that instance.
#       Well organized code with low coupling.
#
#-------------------------------------------------------------------------------------------
# License:
#     © 2025 epita.fr | All rights reserved.
#     This code is provided for educational and demonstration
#     purposes. Redistribution or modification without permission is prohibited.
############################################################################################

class MySingletonClass(object):
    """
    A singleton class that ensures only one instance of itself can exist.

    Use `MySingletonClass.getInstance()` to get the single instance.
    Direct instantiation with `MySingletonClass()` is not allowed and
    will raise a RuntimeError.
    """

    __instance = None   ### private fields to hold instance

    def __new__(cls, val=None):
        ### stop creating a new instance directly
        raise RuntimeError(" Use getInstance() instead")

    ##@staticmethod 
    @classmethod
    def getInstance(cls):
        """
        Returns the single instance of the class.

        Args:
            None
        
        Returns:
            MySingletonClass: this singleton instance of "MySingletonClass"

        """

        ### if NOT initialized, the DO it 
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._initialize()

        return cls.__instance


    
    def _initialize(self):
        self.val = "I am MySingletonClass"

if __name__=="__main__":
    print("Singleton Test")
    
    s1 = MySingletonClass.getInstance()
    s2 = MySingletonClass.getInstance()

    print(s1 is s2)  # True
    print("s1.value -> ",s1.val) 
    print("s1.value -> ",s1.val) 
