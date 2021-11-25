from scripts.helpful_scripts import (
    get_account,
    OPENSEA_URL,
    get_contract,
    fund_with_link,
)
from brownie import Collectible, network, config


def deploy_and_create():
    account = get_account()

    collectible = Collectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        config["networks"][network.show_active()]["keyhash"],
        config["networks"][network.show_active()]["fee"],
        {"from": account},
    )
    fund_with_link(collectible.address)
    creating_tx = collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("token  created!")
    return collectible, creating_tx


def main():
    deploy_and_create()