from brownie import network, Nft
from UnitTests.helpful_scripts import OPENSEA_URL, get_account, get_imagenumber
import json, os
from pathlib import Path

# metadata_dic = {
#     "198": "https://ipfs.io/ipfs/Qme5s3x7jyrZkoaZZZzPD9YSV8o39pMAxooBCVQbhXN13o?filename=0-198.json"
# }
# metadata/rinkeby/0-train-2.png.json
jsonpath = "../metadata/rinkeby/0-train-2.png.json"

rel_path_metadata = "../metadata/rinkeby"

mod_path = Path(__file__).parent

metadata_path = (mod_path / rel_path_metadata)


# uri = json.load(str(metadata_path)+"rinkebyimageuri.json")
# print (uri)
uri = "https://ipfs.io/ipfs/QmauaLsFHqoZ81hxo5FZzd1kqkbaJE9VJL4HLxqTJSDVks?filename=0-train-2.png.json"


# "https://ipfs.io/ipfs/QmauaLsFHqoZ81hxo5FZzd1kqkbaJE9VJL4HLxqTJSDVks?filename=0-train-2.png.json"
def get_meta(jsonpath):
    file = open(jsonpath)
    json_data = json.load(file)
    stud_list = json_data['image']
    print(stud_list)
    return stud_list

def main():
    print(f"Working on {network.show_active()}")
    collectible = Nft[-1]
    number_of_collectibles = collectible.tokenCounter()
    print(f"You have {number_of_collectibles} tokenIds")
    for token_id in range(number_of_collectibles):
        image = get_imagenumber(collectible.tokenIdToImage(token_id))
        if not collectible.tokenURI(token_id).startswith("https://"):
            print(f"Setting tokenURI of {token_id}")
            set_tokenURI(token_id, collectible, uri)


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Please view your NFT at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
    print("Please wait up to 10 minutes")
