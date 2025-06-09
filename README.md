# DeGate Lottery Tool

A secure and verifiable lottery system using Bitcoin block hashes and cryptographic delay functions.

## Overview

The DeGate Lottery Tool is designed to generate provably fair and tamper-resistant lottery numbers in the range of 0-99,999,999. This tool employs a combination of Bitcoin block hashes as a source of public randomness and a cryptographic delay function (onion hash) to prevent manipulation.

## Features

- **Provably Fair**: Uses public Bitcoin block hashes as a source of randomness
- **Tamper-Resistant**: Implements a computationally intensive cryptographic delay function
- **Transparent**: All calculations can be independently verified
- **Range**: Generates lottery numbers from 0 to 99,999,999

## Technical Implementation

The lottery drawing process involves three main steps:

1. **Source of Randomness**: A Bitcoin block hash is used as the initial seed for randomness. This provides a public, unpredictable, and tamper-resistant starting point.

2. **Delay Function**: The block hash undergoes an "onion hash" - a computationally intensive process that:
   - Uses multiple cryptographic hash functions (SHA3-256, BLAKE2b, SHA-512, SHA-384, SHA-256)
   - Executes a large number of rounds (default: 10000 * 1000 * 35)
   - Creates a time delay that prevents advance computation of results

3. **Final Mapping**: The output of the delay function is hashed once more with SHA-256 and then mapped to the range 0-99,999,999.

## Security Features

- **Anti-Mining Protection**: The onion hash algorithm uses a combination of different hash functions to prevent optimization via specialized hardware.
- **Unpredictable Path**: The specific hash function used in each round depends on the previous round's output, creating an unpredictable execution path.
- **Time Delay**: The large number of rounds creates a significant computational delay, preventing advance calculation of results.

## Usage

1. Run the tool:
   ```
   python lottery-tool.py
   ```

2. Enter a Bitcoin block hash when prompted, or press Enter to use the provided sample hash.

3. The tool will:
   - Execute the onion hash calculation (this may take some time)
   - Display progress at regular intervals
   - Generate and display the final lottery number
   - Save the result to a JSON file (`lottery_result.json`)



## Example Output

```
DeGate Lottery Tool v1.0
Tip: You can use any specified BTC block hash for the lottery draw
Note: It's recommended to stop betting well before the drawing time
Enter BTC block hash (press Enter to use sample hash): 

Using BTC block hash: 000000000000000000018a8b6a7f7b41e90a23b1c3f42c03db6d4d16e8f273d4
Starting onion hash delay calculation...
Starting onion hash, total rounds: 350000000
Progress: 0.29%, Completed 1000000 rounds, Time elapsed: 0.86 seconds
...
Onion hash completed, total time: 301.89 seconds
Onion hash calculation completed, intermediate random value: 18745f67ae27e95b8ee4ac037fae58ee9e911306fcae3eace2393d1d35ee481ef1d511e9502e03f12e9c4656c845bd9d665514d9267ebf7c3d111087305a4349
Final random value: 0acc950da48797bab5f7e9d158ba6ef523efa61a5a0d29f1645bce2b9523caa0
🎯 Lottery number (0-99,999,999): 41480608

Lottery result generated and saved
Result saved to lottery_result.json
```

## Verification

To verify the results, run the same calculation with the same Bitcoin block hash. The process is deterministic and will produce the same lottery number. 
