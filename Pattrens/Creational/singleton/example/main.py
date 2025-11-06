from libs.configuration import Configuration

if __name__=="__main__":
    print("\nApplication Singleton Test")

    _configuration=Configuration.getInstance()

    print(
    "\t\nMin => ",_configuration.Min,
    "\t\nMax => ",_configuration.Max,
    "\t\nLog File=> ",_configuration.LogFilePath
    )

    _configuration.Min=20
    _configuration=None

    print("\nApplication Singleton Test -- FINISH")