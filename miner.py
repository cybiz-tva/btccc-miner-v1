import os
import time
import hashlib
import requests
from pymongo import MongoClient
import datetime
import random

MONGODB_URI = 'mongodb://cybiz1:Admin123@ac-pwer4qx-shard-00-00.vbr56wv.mongodb.net:27017,ac-pwer4qx-shard-00-01.vbr56wv.mongodb.net:27017,ac-pwer4qx-shard-00-02.vbr56wv.mongodb.net:27017/?ssl=true&replicaSet=atlas-im60ry-shard-0&authSource=admin&retryWrites=true&w=majority'
DATABASE_NAME = 'btccc'
COLLECTION_NAME = 'users'
COLLECTION = MongoClient(MONGODB_URI)[DATABASE_NAME][COLLECTION_NAME]

def get_device_name():
    return os.uname().nodename

def check_mempool():
    try:
        requests.get('https://bitcoincc-networkdashboard.web.app/')
        return True
    except:
        return False

def generate_wallet_address():
    device_name = get_device_name()
    address = hashlib.sha256(device_name.encode()).hexdigest()
    wallet_address = 'BTCCC' + address[:20]
    print(f"")
    print(f"Welcome to Bitcoin Copy Cat Miner")
    print(f"")
    print(f"Wallet Address: {wallet_address}")
    return wallet_address

def get_wallet_balance(wallet_address):
    user = COLLECTION.find_one({'wallet_address': wallet_address})
    if not user:
        return 0
    wallet_balance = user.get('wallet_balance', 0)
    print(f"Wallet Balance: {wallet_balance} BTCCC")
    return wallet_balance

def update_wallet_balance(wallet_address, new_balance):
    user = COLLECTION.find_one_and_update(
        {'wallet_address': wallet_address},
        {'$set': {'wallet_balance': new_balance}},
        upsert=True,
        return_document=True,
    )
    return user.get('wallet_balance', 0)

def print_balance(wallet_address):
    balance = get_wallet_balance(wallet_address)
    print(f"Current Balance: {balance} BTCCC")

def update_balance(wallet_address):
    balance = get_wallet_balance(wallet_address)
    new_balance = balance + 0.0025
    update_wallet_balance(wallet_address, new_balance)
    return new_balance

def main():
    wallet_address = generate_wallet_address()
    print(f"Device Name: {get_device_name()}")
    print(f"Mem Pool : https://bitcoincc-networkdashboard.web.app/ ")

    while True:
        if not check_mempool():
            print("Miner disconnected, check if you have an active internet connection")
            time.sleep(60)
            continue

        current_time = datetime.datetime.now()
        unique_number = random.randint(10000000, 99999999)
        block_number = random.randint(1000, 9999)
        temperature = round(random.uniform(30, 60), 2)
        current_balance = update_balance(wallet_address)
        dag_size = round(random.uniform(2, 3), 1)
        pool = random.randint(200, 300)
        speed = random.randint(10, 30)
        diff = random.randint(2500, 3500)
        block_h = random.randint(1000, 9999)
        
        print(f" ")
        print(f"\nHash ID: {unique_number} | {current_time}")
        print(f"Block Number: {block_number} | Average Temperature: {temperature} °C")
        print(f"Generating DAG {dag_size} GB for btccc Pool {pool}")
        print(f"New Job: GPU #0 MINING BTCCC SPEED: {speed} H/s Diff: {diff} " )
        print(f"CPU Accepted (1/1) Block Height: {block_h}  " )
        
        time.sleep(23)

if __name__ == '__main__':
    main()