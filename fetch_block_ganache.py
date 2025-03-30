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

print(Web3.to_hex(tx_hash))  # get a transaction hash
  








#  Get Token Holders & Their Balances

from web3.middleware import geth_poa_middleware

web3.middleware_onion.inject(geth_poa_middleware, layer=0)  # Needed for some testnets

transfer_event = contract.events.Transfer

# Get recent 10 blocks and scan for USDT transfers
latest_block = web3.eth.block_number
start_block = latest_block - 10  # Adjust range as needed

event_filter = transfer_event.create_filter(fromBlock=start_block, toBlock="latest")

for event in event_filter.get_all_entries():
    print(f"From: {event['args']['from']}, To: {event['args']['to']}, Value: {web3.from_wei(event['args']['value'], 'ether')} USDT")






# track transactions of a specific address

wallet_address = "0xF977814e90dA44bFA03b6295A0616a897441aceC"

# Fetch the latest transactions involving this wallet
tx_count = web3.eth.get_transaction_count(wallet_address)
print(f"Total transactions by {wallet_address}: {tx_count}")

# Fetch details of the last transaction
latest_tx = web3.eth.get_transaction(web3.eth.get_block("latest")["transactions"][-1])
print(latest_tx)


