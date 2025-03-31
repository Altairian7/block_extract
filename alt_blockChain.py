import hashlib
import json
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.noonce = nonce
        self.hash = self.calculate_hash()
    
    def calculate_hash(self):
        """Generates the hash of the block using SHA-256."""
        block_string = json.dumps({
            "index": self.index,
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "nonce": self.noonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def mine_block(self, difficulty):
        """Mines the block by finding a nonce that satisfies the difficulty level."""
        target = '0' * difficulty
        while self.hash[:difficulty] != target:
            self.noonce += 1
            self.hash = self.calculate_hash()
    


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_transactions = []
        self.balance = {}
        
    def create_genesis_block(self):
        return Block(0, time.time(), "Genesis Block", "0")
        
        
    def add_block(self, data):
        last_block = self.chain[-1]
        new_index = Block(len(self.chain), time.time(), data, last_block.hash)
        self.chain.append(new_index)

    def add_transaction(self, sender, receiver, amount):
        """Adds a new transaction to the pending transactions pool."""
        self.pending_transactions.append({"sender": sender, "receiver": receiver, "amount": amount})
        
        # Update balances
        self.balances[sender] = self.balances.get(sender, 0) - amount
        self.balances[receiver] = self.balances.get(receiver, 0) + amount
        
    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:  
                return False
        return True 
    
    def print_chain(self):
        for block in self.chain:
            print(f"Block {block.index} [Hash: {block.hash}]")
            print(f"Timestamp: {block.timestamp}")
            print(f"Block {block.index} [Hash: {block.hash}]")
            print(f"Timestamp: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Previous Hash: {block.previous_hash}\n")
    
    


# Create a blockchain instance
my_blockchain = Blockchain()

# Add some blocks
my_blockchain.add_block("First transaction")
my_blockchain.add_block("Second transaction")

# Print the blockchain
my_blockchain.print_chain()

# Validate the blockchain
print("Is blockchain valid?", my_blockchain.is_valid())

    