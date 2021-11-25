from  scripts.fullTrain import getdata, train
from scripts.upload_To_Pinata import main
# from contract_scripts.set_tokenuri import main
from flask_cors import CORS
# TextBlob(sentence).sentiment

from flask import Flask, jsonify, request
app = Flask(__name__)
CORS(app)


####### Trainning vars and get data ######
DATA_PATH = './images/'
EPOCHS = 5

train_dataset = getdata(DATA_PATH)
ipfsfilepath = "../ui/frontend/src/ipfs.json"




@app.route('/predict', methods=['POST'])
def generate():
    data = request.get_json()
    # digit = data['digit']
    # TODO
    # Smartcontract Pay
    train(train_dataset, EPOCHS)
    main(ipfsfilepath)
    
    
    # sentiment = TextBlob(sentence).sentiment
    # score = sum(sentiment)/len(sentiment)
    # if score > 0.5:
    #     res = "Positive"
    # else:
    #     res = "Negative"
    # 
    return jsonify({"image":"image generation done"})

@app.route('/mint', methods=['POST'])
def mint():
    return main()


# /Users/upalc/Documents/ethapp/ethnft/ethnft/nftproject/scripts/set_tokenuri.py

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"response":"This is Sentiment Application"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", threaded=True, port=5000)