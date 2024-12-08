import platform, os, sys
from colorama import Fore, Back, Style
import urllib.request as urec

class app:
    def __init__(self):
        self.system = self.osDetector()
        self.connection = self.check_connection()

    @staticmethod
    def check_connection():
        try:
            urec.urlopen("https://www.github.com")
            return True
        except:
            return False

    @staticmethod        
    def osDetector():
        system_operation = platform.system()
        
        if system_operation == "Linux":
            if "ANDROID_ARGUMENT" in os.environ:
                return "Android"
            else:
                return "Linux"
        elif system_operation == "Windows":
            return "Windows"
        elif system_operation == "Darwin":
            return "Mac"
        else:
            return "Unknown"
        

    def test(self):
        permittedOS=False
        system=self.system
        connection=self.connection
        notSystem=["as","Windows","Darwin","Unknown"]
        if system in notSystem:
            print(Fore.RED + "[!]", Fore.RESET + "Your system is not compatible.")
            sys.exit()
        else:
            if connection == True:
                permittedOS=True
                print(Fore.GREEN + "[√]", Fore.RESET + "The device has internet access.")
            else:
                print(Fore.RED + "[!]", Fore.RESET + "Your device does not have internet access.")
                sys.exit()




if __name__ == "__main__":
    apps=app()
    apps.test()