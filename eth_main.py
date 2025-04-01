from web3 import Web3   

INFURA_URL = "https://mainnet.infura.io/v3/251315b2f23f4439b86206e0bfd79df3"  # Replace with your Infura/Alchemy URL
web3 = Web3(Web3.HTTPProvider(INFURA_URL))


if web3.is_connected():
    print("Connected to Ethereum Blockchain ✅")
else:
    print("Failed to connect ❌")
    
    
def get_eth_balance(address):
    balance_wei = web3.eth.get_balance(address)
    balance_eth = web3.from_wei(balance_wei, 'ether')
    return balance_eth



def send_eth_transaction(sender, receiver, private_key, amount_eth):
    nonce = web3.eth.get_transaction_count(sender)
    gas_price = web3.eth.gas_price  # Get current gas price

    tx = {
        'nonce': nonce,
        'to': receiver,
        'value': web3.to_wei(amount_eth, 'ether'),
        'gas': 21000,  # Standard gas for ETH transfer
        'gasPrice': gas_price
    }

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return web3.to_hex(tx_hash)