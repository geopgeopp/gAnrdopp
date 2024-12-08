import platform, os
from colorama import Fore, Back, Style

class app:
    def __init__(self):
        self.system = self.osDetector()

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
            return "Desconocido"
        

    def aa(self):
        system=self.system
        notSystem=["Linux","Windows","Darwin"]
        if system in notSystem:
            print(Fore.RED + "[!]", Fore.RESET + "Your system is not compatible.")
        else:
            print("WELCOME!")




if __name__ == "__main__":
    apps=app()
    apps.aa()