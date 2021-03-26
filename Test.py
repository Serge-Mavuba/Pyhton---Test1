############################################[[[[[[[[[[ DISCLAIMER ]]]]]]]]]]]]]###################################
# 
#       While I did not solve the problem; I found a way aroud using the List comprehensipons method 
#
#################################################################################################################
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
##################################################################################################################

TEST1 = [4,1,3,5,6,7]
print(Fore.WHITE + Back.GREEN + Style.BRIGHT + str(TEST1))

solution = [number for number in TEST1 if number < 5]
solution2 = [number for number in TEST1 if number >= 5]

print(Fore.WHITE + Back.RED + "sample input " + str(solution) + " is known to be: TRUE")
print (Fore.RED+ Back.WHITE + Style.BRIGHT + "sample input " + str(solution2) + " is known to be: FALSE")
print(153*"-")