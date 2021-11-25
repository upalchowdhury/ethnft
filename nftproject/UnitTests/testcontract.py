from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fund_with_link,
)
from brownie import Collectible, network, config

def main():
    print(f"Working on {network.show_active()}")
    collectible = Collectible[-1]
    message = "tsting"
    print(collectible.sign(message))