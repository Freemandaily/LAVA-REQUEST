import time
print('BOOOOOM')
import requests,json,sys,os
import telegram,asyncio

LAVA_0 = 'https://eth1.lava.build/lava-referer-1b4b6ccb-ee4c-4a76-bf67-6f694f391fdc/'
LAVA_1 = 'https://eth1.lava.build/lava-referer-a405b758-f332-411f-8157-558aa65e7f5b/'
LAVA_2 = 'https://eth1.lava.build/lava-referer-e1f76db8-9f7c-4dfe-a9b4-332e16b1ed54/'
LAVA_3 = 'https://eth1.lava.build/lava-referer-442e0329-d146-47af-aae4-70ab18de28bc/'
LAVA_4 = 'https://eth1.lava.build/lava-referer-fa10926f-38eb-4e41-88f4-4a0c0b424ac9/'
LAVA_5 = 'https://eth1.lava.build/lava-referer-ba7ba48d-ce2e-4fc7-92ac-1c9b36ff7b6c/'
LAVA_6 = 'https://eth1.lava.build/lava-referer-3e7319ce-9c8c-408b-9ffc-7012c06b2f73/'
LAVA_7 = 'https://eth1.lava.build/lava-referer-9dd4c088-a59f-43c4-843d-8fec8ec4cef2/'
LAVA_8 = 'https://eth1.lava.build/lava-referer-5d42f6eb-ba0c-4bdf-9eaa-1ae3df04df2e/'
LAVA_9 = 'https://eth1.lava.build/lava-referer-38be6e34-9e91-423e-9538-a4b1973364a7/'
LAVA_11 = 'https://eth1.lava.build/lava-referer-008a60d9-32a9-43d3-871f-2287dc628f3f/'
LAVA_12 = 'https://eth1.lava.build/lava-referer-4592cc52-b007-453e-80e5-c3473e785c10/'
LAVA_13 = 'https://eth1.lava.build/lava-referer-8be00310-8398-4a08-bfbd-7d24949e6893/'

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
    bot_token = '6348189496:AAEa_9d8h-FPAG_OICpIq6rV8E0k3roPhvY'
    async def main():
        try:
            bot =  telegram.Bot(bot_token)
        except:
            bot = telegram.Bot(bot_token)
        async with bot:
            await bot.send_message(text=f'(RPC) Request Completed\n\nSYBIL_NAME: {account}',chat_id=963648721)
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

