import hashlib
import sys

sys.ps1 = '\033[94m'



print(sys.ps1)

print('''
 ████████╗██████╗ ██████╗ ██████╗ 
╚══██╔══╝██╔══██╗╚════██╗╚════██╗
   ██║   ██████╔╝ █████╔╝ █████╔╝
   ██║   ██╔══██╗ ╚═══██╗ ╚═══██╗
   ██║   ██║  ██║██████╔╝██████╔╝
   ╚═╝   ╚═╝  ╚═╝╚═════╝ ╚═════╝ 


string to hash converter by V1 MoDzZz
                       
''')

passw = input("Enter Words : ")



encwd = passw.encode('utf-8')



dig2 = hashlib.md5(encwd.strip()).hexdigest()

print(dig2)
