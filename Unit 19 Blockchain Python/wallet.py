# Import dependencies
import subprocess
import json
from dotenv import load_dotenv
import os
from pprint import pprint 

# Load and set environment variables
load_dotenv()
mnemonic=os.getenv("MNEMONIC")

# Import constants.py and necessary functions from bit and web3
from constants import *
from web3 import Web3, middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy
 
 
# Create a function called `derive_wallets`
def derive_wallets(coin, mnemonic):
    command = f'php derive -g --mnemonic="{mnemonic}" --cols=path,address,privkey,pubkey --coin="{coin}" --numderive=3 --format=json'

    p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, err = p.communicate()
    p_status = p.wait()
    return json.loads(output)

# Create a dictionary object called coins to store the output from `derive_wallets`.
coins = {ETH: derive_wallets(ETH, mnemonic),
        BTCTEST: derive_wallets(BTCTEST, mnemonic)
        }

# Create a function called `priv_key_to_account` that converts privkey strings to account objects.
def priv_key_to_account(coin, priv_key):
    if coin == ETH:
        return Account.privateKeyToAccount(priv_key)
    elif coin == BTCTEST:
        return PrivateKeyTestnet(priv_key)

# Create a function called `create_tx` that creates an unsigned transaction appropriate metadata.
def create_tx(coin, account, to, amount):
    value = Web3.toWei(amount, "ether")
    gas_estimate = web3.eth.estimateGas({'to': to, 
    'from': account["address"], 
    'value': amount})
    gas_price = web3.eth.gasPrice


    if coin == ETH:
        return {"to": to, 
        "from": account, 
        "value": value, 
        "gas": gas_estimate, 
        "gasPrice": gas_price,
        "nonce": 1,
        "chainID": 972}
    if coin == BTCTEST:
        return PrivateKeyTestnet.prepare_transaction(account.address, [(to, amount, BTC)])
# Create a function called `send_tx` that calls `create_tx`, signs and sends the transaction.
def send_tx(create_tx):
    if coin == ETH: 
        return w3.eth.sendRawTransaction(signed.rawTransaction)
    if coin == BTCTEST: 
        return NetworkAPI.broadcast_tx_testnet(signed)

pprint(coins)