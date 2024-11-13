from web3 import Web3

# ethereum se connect kr
infura_url = 'https://mainnet.infura.io/v3/251315b2f23f4439b86206e0bfd79df3'  # infura id replace kr
web3 = Web3(Web3.HTTPProvider(infura_url))

if web3.is_connected(): # connection check kr
    print("Successfully connected to Ethereum")
else:
    print("Failed to connect to Ethereum")

latest_block = web3.eth.get_block('latest')  # infura ko pakad k laa 

print("Block Number:", latest_block['number'])
print("Block Hash:", web3.to_hex(latest_block['hash'])) # block ki details

block_hash = latest_block['hash']
print(f"Hash of Block {latest_block['number']}: {web3.to_hex(block_hash)}") # hash nikaal