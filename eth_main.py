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







def deploy_smart_contract(private_key):
    compiled_contract = {
        "abi": [
            {
                "inputs": [{"internalType": "uint256", "name": "_value", "type": "uint256"}],
                "name": "store",
                "outputs": [],
                "stateMutability": "nonpayable",
                "type": "function",
            },
            {
                "inputs": [],
                "name": "retrieve",
                "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
                "stateMutability": "view",
                "type": "function",
            }
        ],
        "bytecode": "6080604052348015600f57600080fd5b5060d08061001e6000396000f3fe60806040..."
    }

    account = web3.eth.account.from_key(private_key)
    contract = web3.eth.contract(abi=compiled_contract["abi"], bytecode=compiled_contract["bytecode"])

    tx = contract.constructor().build_transaction({
        'from': account.address,
        'gas': 3000000,
        'gasPrice': web3.eth.gas_price,
        'nonce': web3.eth.get_transaction_count(account.address)
    })

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    
    return receipt.contractAddress






def interact_with_contract(contract_address, private_key):
    contract_abi = [
        {
            "inputs": [{"internalType": "uint256", "name": "_value", "type": "uint256"}],
            "name": "store",
            "outputs": [],
            "stateMutability": "nonpayable",
            "type": "function",
        },
        {
            "inputs": [],
            "name": "retrieve",
            "outputs": [{"internalType": "uint256", "name": "", "type": "uint256"}],
            "stateMutability": "view",
            "type": "function",
        }
    ]

    account = web3.eth.account.from_key(private_key)
    contract = web3.eth.contract(address=contract_address, abi=contract_abi)

    # Call function to get stored value
    stored_value = contract.functions.retrieve().call()
    print(f"Stored Value: {stored_value}")

    # Send transaction to update value
    tx = contract.functions.store(42).build_transaction({
        'from': account.address,
        'gas': 200000,
        'gasPrice': web3.eth.gas_price,
        'nonce': web3.eth.get_transaction_count(account.address)
    })

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    
    web3.eth.wait_for_transaction_receipt(tx_hash)
    return tx_hash