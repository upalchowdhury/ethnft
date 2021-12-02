from UnitTests.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract
)
from brownie import Nft, network, config


def deploy_and_create():
    account = get_account()

    collectible = Nft.deploy(
        {"from": account}
    )
    print(collectible, account, network.show_active())
    return collectible


def main():
    deploy_and_create()