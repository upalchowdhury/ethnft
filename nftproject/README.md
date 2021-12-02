# blockchain-developer-bootcamp-final-project
ConsenSys bootcamp final project

#### Project name: generative art

## Link to the app : http://54.227.29.224/


## The app allows user to generate arts using GANs and then mint it as nft. once user hit generatenft button it hits a flask backend server which runs GANs using tensorflow and also create and upload metadata of the images to ipfs(pinata cloud ). Then when user hit MINT it gathers the metadata for this generated image and using settokenuri function it mints nft. The contracts deployed in rinkeby so users can check the minted nft in Opensea testnet. 


## Note:  Currently this app is running in aws ec2 with a flask/nginx combination. the server might be deleted in future

#### Project summary:
This is a nft project that will have an web interface with associated ERC721 contracts.
This platform will allow users to choose a base image and other features from the platform to generate a new image based on GANs.
This generative art then will be owned by the user as nft and can be sold in secondary market place.

please contact if you have any questions or comments. 