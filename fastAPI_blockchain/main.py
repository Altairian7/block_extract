import fastapi as _fastapi
import blockchain as _blockchain


blockchain = _blockchain.Blockchain()
app = _fastapi.FastAPI()

# endpoint to mine a block
@app.post("/mine_block/")
def mine_block(data: str):
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="blockchain is Invalid")
    
    block = blockchain.mine_block(data=data)
    
    return block


# EP to return blockchain
@app.get("/blockchain/")
def get_blockchain():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="blockchain is Invalid")
    
    chain = blockchain.chain
    return chain


# EP to return the previo block
@app.get("/previous_block/")
def previous_block():
    if not blockchain.is_chain_valid():
        return _fastapi.HTTPException(status_code=400, detail="blockchain is Invalid")
    
    return blockchain.get_previous_block()


# EP to see if blockchian is fr
@app.get("/validate/")
def is_blockchain_valid():
    return blockchain.is_chain_valid()
