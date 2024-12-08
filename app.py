import platform, os, sys
from colorama import Fore, Back, Style
import urllib.request as urec

class app:
    def __init__(self):
        self.system = self.osDetector()
        self.connection = self.check_connection()
        self.permittedOS = self.test(self)

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
        
        if "PREFIX" in os.environ and os.path.exists("/data/data/com.termux"):
            return "Termux"
        elif system_operation == "Linux":
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
        
    @staticmethod
    def test(self):
        system=self.system
        connection=self.connection
        notSystem=["Linux","Windows","Darwin","Unknown"]
        if system in notSystem:
            return False
        else:
            if connection == True:
                print(Fore.GREEN + "[√]", Fore.RESET + "The device has internet access.")
                return True
            else:
                print(Fore.RED + "[!]", Fore.RESET + "Your device does not have internet access.")
                return False
            
    def launcher(self):
        permittedOS = self.permittedOS
        if permittedOS == True:
            print("as")
        elif permittedOS == False:
            print(Fore.RED + "[!]", Fore.RESET + "Your system is not compatible.")
            sys.exit()




if __name__ == "__main__":
    apps=app()
    apps.launcher()