from brownie import Box, ProxyAdmin, config, network, ProxyAdmin, TransparentUpgradeableProxy, Contract, BoxV2
from scripts import helpfulScripts


def deployBoxSC():
    account = helpfulScripts.getAccount()
    
    boxContract = Box.deploy({'from': account})
    print(boxContract.retrieve())

    proxyAdmin = ProxyAdmin.deploy({'from': account})

    boxEncodeInitializerFunction = helpfulScripts.encodeFunctionData()

    proxy = TransparentUpgradeableProxy.deploy(boxContract.address, proxyAdmin.address, boxEncodeInitializerFunction, {'from': account, 'gas_limit': 1000000})
    print(f"Proxy deployed to {proxy} ! You can now upgrade it to BoxV2!")
    proxyBox = Contract.from_abi("Box", proxy.address, Box.abi)

    tx = proxyBox.store(1,{'from': account})
    tx.wait(1)

    print(proxyBox.retrieve())

    return proxyBox, proxyAdmin, proxy


def upgradeBox(proxyBoxSC, newImplAddress, proxyAdminContract=None, initializer=None, *args):
    account = helpfulScripts.getAccount()
    transaction = None

    if proxyAdminContract:
        if initializer:
            encodedFunctionCall = helpfulScripts.encodeFunctionData()
            transaction = proxyAdminContract.upgradeAndCall(proxyBoxSC.address, newImplAddress, encodeFunctionData, {'from': account})
        else:
            tx = proxyAdminContract.upgrade(proxyBoxSC.address, newImplAddress, {'from': account})
    else:
        if initializer:
            encodedFunctionCall = helpfulScripts.encodeFunctionData()
            tx = proxyBoxSC.upgradeToAndCall(newImplAddress, encodedFunctionCall, {'from': account})
        else:
            tx = proxyBoxSC.upgradeTo(newImplAddress, {'from': account})
    tx.wait(1)

    print("SmartContract upgraded!")

    return tx

def deployV2():
    account = helpfulScripts.getAccount()
    boxV2Contract = BoxV2.deploy({'from': account})
    return boxV2Contract
    
def main():
    account = helpfulScripts.getAccount()

    proxyBoxSC, proxyAdmin, proxy = deployBoxSC()
    boxV2SC = deployV2()
    upgradeBox(proxyBoxSC, boxV2SC.address, proxyAdminContract = proxyAdmin)


    proxyBoxSC = Contract.from_abi("BoxV2", proxy.address, BoxV2.abi)
    tx = proxyBoxSC.increment({'from': account})
    tx.wait(1)
    print(proxyBoxSC.retrieve())
