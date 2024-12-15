#############################################
# John's Explanation of The Blockchain
#############################################

from characters import Characters
import os
import time
from info import main_info

# Values
Loop = True
Main = True
Credits = False
Info = False

while Main == True:

    while Credits == True:
        os.system('clear')
        print(Characters['credits'])
        print("""\n    What Is the Blockchain?
    Massimo Di Pierro | DePaul University
    link: https://cse.sc.edu/~mgv/csce190f19/diPierro_mcs2017050092.pdf 
    ---------------------------------------------------------------------
    Blockchain 
    Peter Gom, Dirk Schiereck, Oliver Hinz, Dirk Schiereck
    link: https://cs.unibo.it/~danilo.montesi/CBD/Articoli/2017Blockchain.pdf
    ---------------------------------------------------------------------
    The Advantages and Disadvantagesnovs
    Julija Golosova and Andrejs Roma
    link: https://www.researchgate.net/profile/Andrejs-Romanovs-2/publication/330028734_The_Advantages_and_Disadvantages_of_the_Blockchain_Technology/links/60112538a6fdcc071b94ff3c/The-Advantages-and-Disadvantages-of-the-Blockchain-Technology.pdf
    ---------------------------------------------------------------------""")
        exit = input("\n[TYPE 'exit' to LEAVE] ").lower()
        match exit:
            case "exit":
                Loop = True
                Credits = False
    while Info == True:
        main_info()

    while Loop == True:
        # Main Menu while loop #
        os.system('clear')
        print(Characters['logo'])
        print("\n(1)START"), '\n', print("(2)CREDITS"), '\n', print("(3)QUIT")

        menu = str(input("[]> "))

        match menu:
            case "1":
                Info = True
                Loop = False
            case "2":
                Credits = True
                Loop = False
            case "3":
                Main = False

