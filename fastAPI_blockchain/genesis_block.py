"""

Genesis block
{
    index: 0,
    timestamp: current time,
    data: "It all started with me"
    proof: 3,
    previous_hash: "0"
} -> hash() -> 45646asda


{
    index: 1,
    timestamp: current time,
    data: "after the genesis block",
    proof: 2343,
    previous_hash: 45646asda
} -> hash() -> 54566asdd


{
    index: 2,
    timestamp: current time,
    data: "ends with me",
    proof: 2134123,
    previous_hash: 54566asdd
}


"""


import datatime as _dt
import hashlib as _hashlib
import json as _json


class Blockchain:
    def __init__(self) -> None:
        self.chain = list()
        genesis_block = self._create_block(data="It all started with me", proof=1, previous_hash="0", index=0)
        self.chain.append(genesis_block)
        
    def mine_block(self, data: str) -> dict:
        previous_block = self.get_previous_block()
        previous_proof = previous_proof["proof"]
        index = len(self.chain) + 1
        proof = None
        pass
    
    def get_previous_block(self) -> dict:
        return self.chain[-1]
    
    def _create_block(self, data: str, proof: int, previous_hash: str, index: int) -> dict:
        block = {
            "index": index,
            "timestamp": str(_dt.datetime.now()),
            "data": data,
            "proof": proof,
            "previous_hash": previous_hash,
        }
    