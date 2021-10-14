from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests, json, os

def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectible = advanced_collectible.tokenCounter()
    print(f"just created {number_of_advanced_collectible} collectibles")
    collectible_metadata = metadata_template
    for token_id in range(number_of_advanced_collectible):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        print(breed)
        metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        print(metadata_file_name)
        if Path(metadata_file_name).exists():
            print("exist")
        else:
            print("creating metadata files")
            collectible_metadata["name"] = breed
            print (breed)
            collectible_metadata["description"] = f"nice{breed}"
            image_path = "./images/"+ breed.lower().replace("_","-")+".png"
            # image_path = "./images/"+ "193.png"

            image_uri = upload_to_ipfs(image_path)
            collectible_metadata["image"] = image_uri

            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            upload_to_ipfs(metadata_file_name)

def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
