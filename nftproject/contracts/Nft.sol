// SPDX-License-Identifier: MIT
pragma solidity 0.6.6;
 
import "./Meta.sol";

 
contract Nft is Metadata{

  uint256 public count;
  address public owner;
  event totalcount(uint256 count);

  constructor() public {
    owner = msg.sender;
    Name = "generative NFT";
    Id = "DG";
  }

  event Minted(
    address indexed owner,
    address indexed minter
  );

  event Mint(
    address to,
    string tokenuri
  );

  modifier onlyOwner()
  {
    require(msg.sender == owner, "Not the owner");
    _;
  }

  

  function incrementCount() public {
        count++;
        emit totalcount(count);
    }

    function setCount(uint256 _count) public {
        require(_count > 0);
        count = _count;
    }

  function transfer(address _minter) public onlyOwner
  {
    require(_minter != address(0), "Not valid address");
    emit Minted(owner, _minter);
    owner = _minter;
  }

 
  function mint(address _to, uint256 _tokenId, string calldata _uri) external onlyOwner {
    super._mint(_to, _tokenId);
    super._setTokenUri(_tokenId, _uri);
    emit Mint(_to,_uri)
  }
 
}