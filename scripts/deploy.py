from brownie import FundMe,config, network, MockV3Aggregator

from scripts.helpful_script import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS



def deploy_fund_me():
    account = get_account()

    if network.show_active()  not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        print(network.show_active())
        price_feed_address = config["networks"][network.show_active()]["eth_usd_price_feed"]
        print(price_feed_address, "WTXDS")
    else:
        deploy_mocks() 
        price_feed_address = MockV3Aggregator[-1].address 

    fund_me = FundMe.deploy("0x5f4eC3Df9cbd43714FE2740f5E3616155c5b8419",{"from": account}, publish_source=config["networks"][network.show_active()].get("verify"))
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()