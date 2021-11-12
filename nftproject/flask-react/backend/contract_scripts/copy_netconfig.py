import yaml, os, json

def copy_netconfig():
    with open("../brownie-config.yaml", "r") as config:
        conf = yaml.load(config, Loader=yaml.FullLoader)
        with open("../flask-react/ui/frontend/src/netconig.json", "w") as config_json:
            json.dump(conf, config_json)

if __name__=="__main__":
    copy_netconfig()
