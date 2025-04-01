from web3 import Web3   

INFURA_URL = "https://mainnet.infura.io/v3/251315b2f23f4439b86206e0bfd79df3"  # Replace with your Infura/Alchemy URL
web3 = Web3(Web3.HTTPProvider(INFURA_URL))


if web3.is_connected():
    print("Connected to Ethereum Blockchain ✅")
else:
    print("Failed to connect ❌")