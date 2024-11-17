from web3 import Web3


#-----using personal ganache, for making transactions

ganache_url = "HTTP://127.0.0.1:7545"
Web3 = Web3(Web3.HTTPProvider(ganache_url))

if Web3.is_connected(): # connection check kr
    print("Successfully connected to Ganache")
else:
    print("Failed to connect to Ganache")


# creating fake accounts
acc_1 = "0x9B0369515D9Ed16FEc420e3370BCeE87220E4448"
acc_2 = "0x0C18e7dF4209E4A3555F2cc2441dB2F38ff1284a"

private_key_acc_1 = "0xb0a2801399e24281c4e96b98fd7c6941ebbf18df2b9d5a9b597575ffbfabeda5" # private key added from 

# get the nonce 
nonce = Web3.eth.get_transaction_count(acc_1)

# build a transaction
tx = {
    'nonce': nonce, # prevents from repeated transacx
    'to': acc_2,
    'from': acc_1,
    'value': Web3.to_wei(2, 'ether'),
    'gas':  2000000,
    'gasPrice': Web3.to_wei('50', 'gwei')

}

signed_tx = Web3.eth.account.sign_transaction(tx, private_key_acc_1)    # sign a transaction

tx_hash = Web3.eth.send_raw_transaction(signed_tx.raw_transaction)    # send a transaction

print(tx_hash)  # get a transaction hash
  