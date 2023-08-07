
from web3 import Web3, EthereumTesterProvider


MyAddress = '0x8defF24E4c5FfB43E9A75714FfD4AF86993BC3Ac'
adress_2 = '0x91eCbE8844fd89baD57C188aE9ED11C42Aef1EDb'
web3 = Web3(Web3.HTTPProvider('https://rpc.ankr.com/bsc'))
print(web3.is_connected())
balance = web3.eth.get_balance(MyAddress)
ethConvert = web3.from_wei(balance, 'ether')
usdBalance = ethConvert * 240
print(usdBalance, 'usd')
print(ethConvert, 'bnb')
print(balance)

private_key = '2f1897d62c67a6648be7ae1ec81f72d5fae63dd3c8d57ca6e6420a8adb0c4cf9'

nonce = web3.eth.get_transaction_count(MyAddress)
tx = {
    'nonce': nonce,
    'to': adress_2,
    'value': web3.to_wei(0.0001,'ether'),
    'gas': 21000,
    'gasPrice': web3.to_wei('1','gwei'),
    'chainId': 56
}

signed_tx = web3.eth.account.sign_transaction(tx, private_key)
tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(web3.to_hex(tx_hash))




