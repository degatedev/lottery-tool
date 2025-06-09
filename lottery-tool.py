import hashlib
import os
import json
from typing import List
import time


def onion_hash_strong(seed: bytes, rounds=10000 * 1000 * 35) -> bytes:
    """
    Strong anti-mining onion hash, using multiple >=256-bit hash functions
    Structure: sha3_256, blake2b, sha512, sha384, sha256
    """
    r = seed
    hash_names = ['sha3_256', 'blake2b', 'sha512', 'sha384', 'sha256']
    
    start_time = time.time()
    print(f"Starting onion hash, total rounds: {rounds}")
    
    for i in range(rounds):
        algo = hash_names[(i + r[0]) % len(hash_names)]
        if algo == 'sha3_256':
            r = hashlib.sha3_256(r).digest()
        elif algo == 'blake2b':
            r = hashlib.blake2b(r, digest_size=32).digest()
        elif algo == 'sha256':
            r = hashlib.sha256(r).digest()
        elif algo == 'sha384':
            r = hashlib.sha384(r).digest()
        elif algo == 'sha512':
            r = hashlib.sha512(r).digest()
        
        # Show progress every 1 million rounds
        if i > 0 and i % 1000000 == 0:
            elapsed = time.time() - start_time
            percent = (i / rounds) * 100
            print(f"Progress: {percent:.2f}%, Completed {i} rounds, Time elapsed: {elapsed:.2f} seconds")
    
    total_time = time.time() - start_time
    print(f"Onion hash completed, total time: {total_time:.2f} seconds")
    return r


def run_lottery_from_btc(btc_hash_hex: str) -> int:
    """
    Complete lottery draw process:
    1. Receive BTC block hash
    2. Execute onion hash delay calculation
    3. Generate final random number (0-99,999,999)
    """
    print(f"Using BTC block hash: {btc_hash_hex}")
    
    # Ensure correct hash length
    btc_hash = bytes.fromhex(btc_hash_hex[:64])
    
    # Execute onion hash
    print("Starting onion hash delay calculation...")
    intermediate_random = onion_hash_strong(btc_hash)
    print(f"Onion hash calculation completed, intermediate random value: {intermediate_random.hex()}")
    
    # Calculate final random value
    final_random = hashlib.sha256(intermediate_random).digest()
    print(f"Final random value: {final_random.hex()}")
    
    # Map to 0-99,999,999 range
    final_number = int.from_bytes(final_random, 'big') % 100_000_000
    print(f"🎯 Lottery number (0-99,999,999): {final_number}")
    
    return final_number


if __name__ == "__main__":
    # Example: Using BTC block hash for lottery draw
    print("DeGate Lottery Tool v1.0")
    print("Tip: You can use any specified BTC block hash for the lottery draw")
    print("Note: It's recommended to stop betting well before the drawing time")
    
    # Sample BTC block hash (user needs to provide actual hash)
    sample_btc_hash = "000000000000000000018a8b6a7f7b41e90a23b1c3f42c03db6d4d16e8f273d4"
    
    # User input for block hash, use sample if empty
    input_hash = input("Enter BTC block hash (press Enter to use sample hash): ")
    btc_hash = input_hash if input_hash.strip() else sample_btc_hash
    
    # Run lottery process
    winning_number = run_lottery_from_btc(btc_hash)
    
    print("\nLottery result generated and saved")
    
    # Save result to file
    result = {
        "btc_hash": btc_hash,
        "timestamp": time.time(),
        "winning_number": winning_number
    }
    
    with open("lottery_result.json", "w") as f:
        json.dump(result, f, indent=2)
    
    print(f"Result saved to lottery_result.json") 