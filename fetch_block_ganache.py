from web3 import Web3


#-----using personal ganache, for making transactions

ganache_url = "HTTP://127.0.0.1:7545"
Web3 = Web3(Web3.HTTPProvider(ganache_url))

if Web3.is_connected(): # connection check kr
    print("Successfully connected to Ganache")
else:
    print("Failed to connect to Ganache")



