import colorama
import random
colorama.init(autoreset=True)

colors = [colorama.Fore.BLUE, colorama.Fore.RED, colorama.Fore.WHITE, colorama.Fore.GREEN]

print(random.choice(colors) + """
 _____       __       ______                           
|_   _|     / _|      | ___ \                          
  | | _ __ | |_ ___   | |_/ /___  __ _ _ __   ___ _ __ 
  | || '_ \|  _/ _ \  |    // _ \/ _` | '_ \ / _ \ '__|
 _| || | | | || (_) | | |\ \  __/ (_| | |_) |  __/ |   
 \___/_| |_|_| \___/  \_| \_\___|\__,_| .__/ \___|_|   
                                      | |              
                                      |_|              """)