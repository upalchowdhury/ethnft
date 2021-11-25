from scripts.sample_metadata import metadata_template
from pathlib import Path
import requests, json, os, glob


################# generated image path ###########
rel_path = "../../../images/outputdata"
rel_path_metadata = "./metadata/rinkeby"

mod_path = Path(__file__).parent

metadata_path = (mod_path / rel_path_metadata).resolve()
metadata = []
for file in os.listdir(metadata_path):
    metadata.append(str(metadata_path)+"/"+file)
# OR if we are `import helper_script`
# mod_path = Path(helper_script.__file__).parent

path_dir = (mod_path / rel_path).resolve()
files = []
for file in os.listdir(path_dir):
    files.append(str(path_dir)+"/"+file)
    # print(file)
# imagepath = files[2]

def uploadToPinata(ipfsfilepath):

    PINATA_BASE_URL = 'https://api.pinata.cloud/'
    endpoint = 'pinning/pinFileToIPFS'
    # Change this to upload a different file
    filepath = metadata[1]
    filename = filepath.split('/')[-1:][0]
 
    headers = {'pinata_api_key': os.getenv('REACT_APP_PINATA_KEY'),
            'pinata_secret_api_key': os.getenv('REACT_APP_PINATA_SECRET')}

    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(PINATA_BASE_URL + endpoint,
                                files={"file": (filename, image_binary)},
                                headers=headers)
        with open(ipfsfilepath, 'w', encoding='utf-8') as f:
            json.dump(response.json(), f, ensure_ascii=False, indent=4)                
        print(response.json())

def main(ipfsfilepath):
    uploadToPinata(ipfsfilepath)
# if __name__ == "__main__":
#     main()