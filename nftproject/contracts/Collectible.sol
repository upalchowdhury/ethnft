// SPDX-License-Identifier: MIT
pragma solidity 0.6.6;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@chainlink/contracts/src/v0.6/VRFConsumerBase.sol";

contract Collectible is ERC721, VRFConsumerBase {
    uint256 public tokenCounter;
    bytes32 public keyhash;
    uint256 public fee;
    bytes32 message;
    uint256 public count;
    enum Image{first,second,third,fourth, fifth}

    mapping(uint256 => Image) public tokenIdToImage;

    mapping(bytes32 => address) public requestIdToSender;

    event totalcount(uint256 count);

    event requestedCollectible(bytes32 indexed requestId, address requester);

    //event signtransaction(msg.sender,bytes32 message);

    //event Assigned(uint256 indexed tokenId, Image image);

    constructor(address _vrfCoordinator, address _linkToken, bytes32 _keyhash, uint256 _fee) public 
    VRFConsumerBase(_vrfCoordinator, _linkToken)
    ERC721("GEN", "genshub")
    {
        tokenCounter = 0;
        keyhash = _keyhash;
        fee = _fee;
    }

    function createCollectible() public returns (bytes32){
        bytes32 requestId = requestRandomness(keyhash, fee);
        requestIdToSender[requestId] = msg.sender;
        emit requestedCollectible(requestId, msg.sender);
    }

    function fulfillRandomness(bytes32 requestId, uint256 randomNumber) internal override {
        Image image = Image(randomNumber % 5);
        uint256 newTokenId = tokenCounter;
        tokenIdToImage[newTokenId] = image;
        //emit Assigned(newTokenId, image);
        address owner = requestIdToSender[requestId];
        _safeMint(owner, newTokenId);
        tokenCounter = tokenCounter + 1;
    }

    function setTokenURI(uint256 tokenId, string memory _tokenURI) public {

        require(_isApprovedOrOwner(_msgSender(), tokenId), " not authorized");
        _setTokenURI(tokenId, _tokenURI);
    }

    

    function incrementCount() public {
        count++;
        emit totalcount(count);
    }

    function setCount(uint256 _count) public {
        require(_count > 0);
        count = _count;
    }

    function sign(string memory message) public view returns (string memory){
        // address owner = ERC721.ownerOf(tokenId);
        // require(msg.sender == owner);
        return message;
        
    }
}