import time
print('BOOOOOM')
import requests,json,sys,os
import telegram,asyncio

# You can add the string of a many of your RPC key using the conventio lava_1,lava_2 etc
LAVA_0 = ''



def getBlockNumber(RPC_ENDPOINT):
    payload = {
        'jsonrpc': '2.0',
        'method': 'eth_blockNumber',
        'param': [],
        'id': 1
    }
    response = requests.post(RPC_ENDPOINT,json=payload)
    result = response.json()
    latest_block = int(result['result'],16)
    print(f'Latest Block Is {latest_block}')

def get_block_by_number(RPC_ENDPOINT):
    block_number = 123456
    payload = {
        "jsonrpc": "2.0",
        "method": "eth_getBlockByNumber",
        "params": [hex(block_number), True],
        "id": 1
    }
    response = requests.post(RPC_ENDPOINT, json=payload)
    result = response.json()
    blockkData = result['result']
    sample = {}
    if type(sample) == type(blockkData):
        print('Block Data Has Been Retrieved Successfully')


def get_transaction_by_hash(RPC_ENDPOINT):
    sample = {}
    hashes = ['0xed32da064a43eae8fed2d93ddc5e2c3b8bf596788222fc3959e8e9174160fb03','0x49058807b30771c9edfba5f118599ce6cc2ecbee51c7c82bc3c5f3cc9c2c34d2']
    for hash in hashes:
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getTransactionByHash",
            "params": [hash],
            "id": 1
        }
        response = requests.post(RPC_ENDPOINT, json=payload)
        result = response.json()
        transactionData = result['result']
        if type(sample) == type(transactionData):
            print('Transaction Data Has Been Retrieved Successfully')
        time.sleep(3)

def get_transaction_receipt(RPC_ENDPOINT):
    sample = {}
    hashes = ['0xed32da064a43eae8fed2d93ddc5e2c3b8bf596788222fc3959e8e9174160fb03','0x49058807b30771c9edfba5f118599ce6cc2ecbee51c7c82bc3c5f3cc9c2c34d2']
    for hash in hashes:
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getTransactionReceipt",
            "params": [hash],
            "id": 1
        }
        response = requests.post(RPC_ENDPOINT, json=payload)
        result = response.json()
        transactionReceipt = result['result']
        if type(sample) == type(transactionReceipt):
            print('TransactionReceipt Data Has Been Retrieved Successfully')
        time.sleep(3)

def get_balance(RPC_ENDPOINT):
    addresses = ['0x77E3DaE164c3145452B81F5aFfb2e8c6f0a226C9','0x20f8Dd24C933ea9FBc247Db7Dc835654A0051Af6']
    for address in addresses:
        payload = {
            "jsonrpc": "2.0",
            "method": "eth_getBalance",
            "params": [address, "latest"],
            "id": 1
        }
        response = requests.post(RPC_ENDPOINT, json=payload)
        result = response.json()
        balance = int(result['result'], 16)
        print(f'Address {address[:5]} Has {balance/10**18} ETH Balance')
        time.sleep(4)

  
def Alert(account):
    # Get Your Telegram bot token
    bot_token = ''
    async def main():
        try:
            bot =  telegram.Bot(bot_token)
        except:
            bot = telegram.Bot(bot_token)
        async with bot:
            await bot.send_message(text=f'(RPC) Request Completed\n\nSYBIL_NAME: {account}',chat_id= # YOUR Telegram Chat Id)
    if __name__ == '__main__':
        asyncio.run(main())

def main(RPC_ENDPOINT,lavaCommand):
    try:
        get_balance(RPC_ENDPOINT)
        time.sleep(7)
        get_transaction_receipt(RPC_ENDPOINT)
        time.sleep(7)
        get_transaction_by_hash(RPC_ENDPOINT)
        time.sleep(7)
        get_block_by_number(RPC_ENDPOINT)
        time.sleep(7)
        getBlockNumber(RPC_ENDPOINT)
        Alert(lavaCommand)
    except Exception as e:
        print(f'The issue is {e}')


# Taking Command From The Subprocess
lavaCommand = sys.argv[1]
if lavaCommand in globals():
    RPC_ENDPOINT = globals()[lavaCommand]
    print('About To Use RPC')
    main(RPC_ENDPOINT,lavaCommand)
else:
    pass

