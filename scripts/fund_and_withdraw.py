from brownie import FundMe
from scripts.helpful_script import get_account

def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getConversionRate(444444444444)  
    print(entrance_fee)

    print("Funding")
    fund_me.fund({"from": account, "value": entrance_fee, "gas_price": 10000000000, "allow_revert": True, "gas_limit": 500000})
 

def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    print("withdrawing")
    fund_me.withdraw({"from": account})

def main():
    fund()
    withdraw()