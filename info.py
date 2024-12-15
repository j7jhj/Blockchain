
import os
import time
def printt(string, strDelay):
  for i in str(string + "\n"):
    print(i, end="", flush=True)
    time.sleep(strDelay)

text = """The Blockchain is an internet innovation that is mainly known for the popular digital currency known as, “Bitcoin”. 
The Blockchain isn’t just used for bitcoin, it's also used for digital transactions to store data in different data sets to prevent tampering of the data. 
The blockchain works by first having the “genesis block” which is the main data and all other data blocks are made with a timestamp, a hash value of the 
previous block, and the nonce which is a random value, confirming the hash value. The hash value is important against fraud and tampering as changes in the 
block chain will also change the hash value. The only way to find the hash value is to find a collision in the data but is impossible to find as it would take 
so much computing time that the struggle would be rendered useless. Although the blockchain sounds beneficial, it still has a glaring problem which is energy 
consumption. According to Julia Kolosova and Andrejs Roma , “The consumption of power is needed for keeping a real-time ledger. Every time the new node is created 
and in the same time it communicates with each and other node” (Julija Golosova and Andrejs Roma, 2018)."""

def main_info():
    os.system('clear')
    printt(text, 0.07)
    exit = input("[Type 'exit' to exit]").lower()

    match exit:
        case "exit":
            Info = False
            Loop = True
