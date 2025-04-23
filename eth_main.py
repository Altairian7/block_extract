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






def listen_to_contract_events(contract_address):
    contract_abi = [
        {
            "anonymous": False,
            "inputs": [
                {"indexed": True, "internalType": "uint256", "name": "oldValue", "type": "uint256"},
                {"indexed": False, "internalType": "uint256", "name": "newValue", "type": "uint256"}
            ],
            "name": "ValueChanged",
            "type": "event"
        }
    ]

    contract = web3.eth.contract(address=contract_address, abi=contract_abi)
    
    event_filter = contract.events.ValueChanged.create_filter(fromBlock="latest")

    while True:
        for event in event_filter.get_new_entries():
            print(f"Value changed from {event.args.oldValue} to {event.args.newValue}")



def get_gas_price():
    return web3.from_wei(web3.eth.gas_price, 'gwei')



def estimate_gas(sender, receiver, amount_eth):
    tx = {
        'to': receiver,
        'value': web3.to_wei(amount_eth, 'ether'),
        'gasPrice': web3.eth.gas_price
    }
    return web3.eth.estimate_gas(tx)



















def mint_nft(contract_address, private_key, to_address, token_uri):
    nft_abi = [...]  # Replace with the actual ABI of your NFT contract
    contract = web3.eth.contract(address=contract_address, abi=nft_abi)
    account = web3.eth.account.from_key(private_key)

    tx = contract.functions.mintNFT(to_address, token_uri).build_transaction({
        'from': account.address,
        'gas': 300000,
        'gasPrice': web3.eth.gas_price,
        'nonce': web3.eth.get_transaction_count(account.address)
    })

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return web3.to_hex(tx_hash)






def send_erc20(token_contract_address, private_key, to_address, amount):
    erc20_abi = [...]  # Use the standard ERC20 ABI
    contract = web3.eth.contract(address=token_contract_address, abi=erc20_abi)
    account = web3.eth.account.from_key(private_key)

    tx = contract.functions.transfer(to_address, amount).build_transaction({
        'from': account.address,
        'gas': 100000,
        'gasPrice': web3.eth.gas_price,
        'nonce': web3.eth.get_transaction_count(account.address)
    })

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return web3.to_hex(tx_hash)







def get_nft_metadata_uri(contract_address, token_id):
    nft_abi = [...]  # ERC-721 ABI
    contract = web3.eth.contract(address=contract_address, abi=nft_abi)
    uri = contract.functions.tokenURI(token_id).call()
    return uri





def get_pending_transactions(address):
    pending_txs = web3.eth.filter("pending").get_new_entries()
    user_pending = [tx for tx in pending_txs if tx['from'].lower() == address.lower()]
    return user_pending




def get_token_info(token_address):
    abi = [...]  # Standard ERC20 ABI
    contract = web3.eth.contract(address=token_address, abi=abi)
    symbol = contract.functions.symbol().call()
    decimals = contract.functions.decimals().call()
    return {'symbol': symbol, 'decimals': decimals}



def safe_estimate_gas(tx_object):
    try:
        estimated = web3.eth.estimate_gas(tx_object)
        return int(estimated * 1.1)  # 10% buffer
    except Exception as e:
        print("Gas estimation failed:", e)
        return 300000  # Fallback default




def deploy_erc20_token(private_key, name, symbol, initial_supply):
    abi = [...]       # ERC20 ABI
    bytecode = "0x..."  # Compiled ERC20 bytecode

    account = web3.eth.account.from_key(private_key)
    contract = web3.eth.contract(abi=abi, bytecode=bytecode)

    tx = contract.constructor(name, symbol, initial_supply).build_transaction({
        'from': account.address,
        'gas': 4000000,
        'gasPrice': web3.eth.gas_price,
        'nonce': web3.eth.get_transaction_count(account.address)
    })

    signed_tx = web3.eth.account.sign_transaction(tx, private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    receipt = web3.eth.wait_for_transaction_receipt(tx_hash)
    return receipt.contractAddress




# Run Ethereum Blockchain Functions
if __name__ == "__main__":
    user_address = "0xYourEthereumAddressHere"  # Replace with an actual Ethereum address
    receiver_address = "0xReceiverAddressHere"
    private_key = "YourPrivateKeyHere"  # Keep this safe! Never expose it in production

    # Get ETH balance
    balance = get_eth_balance(user_address)
    print(f"ETH Balance: {balance} ETH")
    
    # Send ETH Transaction
    tx_hash = send_eth_transaction(user_address, receiver_address, private_key, 0.01)
    print(f"Transaction Hash: {tx_hash}")

    # Deploy Smart Contract
    contract_address = deploy_smart_contract(private_key)
    print(f"Deployed Smart Contract Address: {contract_address}")

    # Interact with Smart Contract
    tx_hash = interact_with_contract(contract_address, private_key)
    print(f"Contract Interaction TX: {tx_hash}")

    # Listen to Events (Run this in a separate thread)
    listen_to_contract_events(contract_address)
    
    # Get Gas Price
    gas_price = get_gas_price()
    print(f"Current Gas Price: {gas_price} Gwei")

    # Estimate Gas for Transaction
    estimated_gas = estimate_gas(user_address, receiver_address, 0.01)
    print(f"Estimated Gas: {estimated_gas}")