from brownie import Collectible, network
from requests.models import DEFAULT_REDIRECT_LIMIT
# from scripts.helpful_scripts import get_imagenumber
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests, json, os, glob



################# generated image path ###########
rel_path = "../images/outputdata"
rel_path_metadata = "../metadata/rinkeby"

mod_path = Path(__file__).parent

metadata_path = (mod_path / rel_path_metadata)
# OR if we are `import helper_script`
# mod_path = Path(helper_script.__file__).parent

path_dir = (mod_path / rel_path).resolve()
files = []
for file in os.listdir(path_dir):
    files.append(str(path_dir)+"/"+file)
    # print(file)
imagepath = files[2]


def get_imagenumber(number):
    imageNumberMapping = {0:"train-0.png",1:"train-1.png",
                            2:"train-2.png",3:"train-3.png",
                                4:"train-4.png"}
    # imagelist = glob.glob(imagepath)
    # counter = 0
    # for item in imagelist:
    #     imageNumberMapping[counter]=item
    #     counter = counter + 1
    return imageNumberMapping[number]



def main():
    collectible = Collectible[-1]
    number_of_collectible = collectible.tokenCounter()
    print(f"just created {number_of_collectible} collectibles")
    collectible_metadata = metadata_template
    for token_id in range(number_of_collectible):
        image = get_imagenumber(collectible.tokenIdToImage(token_id))
        print(image)
        metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{image}.json"
        print(metadata_file_name)
        # if Path(metadata_file_name).exists():
        #     print("exist")
        # else:
        print("creating metadata files")
        collectible_metadata["name"] = image
        print (image)
        collectible_metadata["description"] = f"{image}"
            #image_path = image_path + breed.lower().replace("_","-")+".png"
            # image_path = "./images/"+ "193.png"

        image_uri = upload_to_ipfs(imagepath)
        collectible_metadata["image"] = image_uri

        with open(metadata_file_name, "w") as file:
            json.dump(collectible_metadata, file)
        upload_to_ipfs(metadata_file_name)

def upload_to_ipfs(filepath):
    # directory = glob.glob(directory)
    # for filepath in directory:
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        ipfs_url = "http://127.0.0.1:5001"
        endpoint = "/api/v0/add"
        response = requests.post(ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        with open(str(metadata_path) + "imageuri.json","w") as imageuri_file:
            json.dump(image_uri,imageuri_file)
        print(image_uri)
        return image_uri
