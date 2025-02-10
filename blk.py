
import json
from web3 import Web3, HTTPProvider


# truffle development blockchain address
blockchain_address = 'http://127.0.0.1:9545'
# Client instance to interact with the blockchain
web3 = Web3(HTTPProvider(blockchain_address))
# Set the default account (so we don't need to set the "from" for every transaction call)
web3.eth.defaultAccount = web3.eth.accounts[0]
compiled_contract_path = 'C:/Users/ASHITHA/Desktop/external project/forensic_eviden (6)/forensic_eviden/node_modules/.bin/build/contracts/forensic.json'
# Deployed contract address (see `migrate` command output: `contract address`)
deployed_contract_address = '0xaa209E5760dBD1FD7Eb5EC1dE111a813bA63c06A'
syspath=r"C:\Users\ASHITHA\Desktop\external project\forensic_eviden (6)\forensic_eviden\static\\"
