from brownie import network, config, accounts,MockV3Aggregator

DECIMALS = 8
INITIAL_VALUE = 200000000000
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development","ganache-local"]
FORKED_LOCAL_ENVIRONMENTS=["mainnet-fork","mainnet-fork-dev"]

def get_account():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS or network.show_active() in FORKED_LOCAL_ENVIRONMENTS:
        return accounts[0]
    else: 
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    MockV3Aggregator.deploy(DECIMALS, INITIAL_VALUE, {"from": get_account()})