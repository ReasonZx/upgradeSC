from brownie import Box, ProxyAdmin, config, network, ProxyAdmin, TransparentUpgradeableProxy, Contract
from scripts import helpfulScripts


def deployBoxSC():
    account = helpfulScripts.getAccount()
    
    boxContract = Box.deploy({'from': account}    )
    print(boxContract.retrieve())

    proxyAdmin = ProxyAdmin.deploy({'from': account})

    #initializer = box.store, 1
    boxEncodeInitializerFunction = helpfulScripts.encodeFunctionData()

    proxy = TransparentUpgradeableProxy.deploy(boxContract.address, proxyAdmin.address, boxEncodeInitializerFunction, {'from': account, 'gas_limit': 1000000})
    print("Proxy deployed to " + proxy + "- you can now upgrade to v2.")
    proxyBox = Contract.from_abi("Box", proxy.address, Box.abi)

    print(proxyBox.retrieve())

    return boxContract

def main():
    deployBoxSC()