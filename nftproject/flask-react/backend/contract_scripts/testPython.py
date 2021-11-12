import os, json, glob

from pathlib import Path


######################## GOOD RESOURCE ###################

# https://stackoverflow.com/questions/918154/relative-paths-in-python

#########################  GOOD RESOURCE #################

# from scripts.create_metadata import DIRECTORY

rel_path = "../images/outputdata/"

mod_path = Path(__file__).parent
# OR if we are `import helper_script`
# mod_path = Path(helper_script.__file__).parent

path_dir = (mod_path / rel_path).resolve()
files = []
for file in os.listdir(path_dir):
    files.append(file)
    print(file)





# imagepath = "../images/outputdata/*.png"
# imageNumberMapping = {}

# def get_imagenumber(number,imagepath):
#     imagelist = glob.glob(imagepath)
#     counter = 0
#     for item in imagelist:
#         imageNumberMapping[counter]=item
#         counter = counter + 1
# #     return imageNumberMapping[number]
# file = open("/Users/upalc/Documents/ethapp/ethnft/ethnft/nftproject/metadata/rinkeby/0-train-2.png.json")
# json_data = json.load(file)

# stud_list = json_data['image']
# y = {}
# for var in stud_list:
#     x = {var['name']: var['Avg']}
#     y = dict(list(x.items()) + list(y.items()))


    # DIRECTORY.append(file)
# imagepath = DIRECTORY[1]
print(files[2])
# print(imagepath)








# if __name__=="__main__":
    # print(get_imagenumber(0, imagepath))
    