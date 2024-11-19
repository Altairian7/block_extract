from web3 import Web3


# ethereum se connect kr
infura_url = 'https://mainnet.infura.io/v3/251315b2f23f4439b86206e0bfd79df3'  # infura id replace kr
web3 = Web3(Web3.HTTPProvider(infura_url))