# upgradeSC

Transparent Upgradable Proxy contract deployed @ **0x1292e2650955dB8C733af8E062e4388F951743b7** on Eth Testnet - **Sepolia**

Box v1 deployed @ **0x2AFd77374aAc428f58c2D0AA3eA0860DBb225f5e** on Eth Testnet - **Sepolia**

Box v2 deployed @ **0xeA76227963a2E49de5De738BbEFfBAb55e20F531** on Eth Testnet - **Sepolia**



# Deploy

## Testnet
To deploy on a testnet, get your keys for that testnet and the project id from infura.io.

For example Sepolia testnet:
```
$export PUBLIC_KEY="your_public_key"
$export PRIVATE_KEY="your_private_key"
$export WEB3_INFURA_PROJECT_ID="your_infura_project_id"
$brownie networks add Ethereum sepolia host="https://sepolia.infura.io/v3/your_infura_project_id" chainid=11155111
```
Then deploy the smart contract:
```
$brownie run scripts/deployAndUpgrade.py --network sepolia
```

## Mainnet-fork
To have locally a mainnet-fork go to alchemy.com and create a new app (creates a fork). Then run the following command to add that fork to your local enviroment with brownie:
```
brownie networks add development mainnet-fork cmd=ganache-cli host=http://127.0.0.1 fork=https://eth-mainnet.g.alchemy.com/v2/********* accounts=10 mnemonic=******* port=8545
```
Then deploy the SC with:
```
$brownie run scripts/deployAndUpgrade.py --network mainnet-fork
```

