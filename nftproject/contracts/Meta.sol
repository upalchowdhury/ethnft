// SPDX-License-Identifier: MIT
pragma solidity 0.6.6;


contract Metadata {

  string internal Name;
  string internal Id;

  mapping (uint256 => address) internal idToOwner;

  mapping (uint256 => string) internal tokenIdToUri;

  mapping (address => uint256) private ownerToNFTokenCount;


  constructor() public {}


  function name()
    external
    
    view
    returns (string memory _name)
  {
    _name = Name;
  }

 
  function symbol()
    external
    
    view
    returns (string memory _Id)
  {
    _Id = Id;
  }


function _addNFToken(
    address _to,
    uint256 _tokenId
  )
    internal
    virtual
  {
    require(idToOwner[_tokenId] == address(0), " token already exists");

    idToOwner[_tokenId] = _to;
    ownerToNFTokenCount[_to] += 1;
  }



function _mint(
    address _to,
    uint256 _tokenId
  )
    internal
    virtual
  {
    require(_to != address(0), "not correct address");
    require(idToOwner[_tokenId] == address(0), "not valid");

    _addNFToken(_to, _tokenId);

    //emit Transfer(address(0), _to, _tokenId);
  }

modifier validNFToken(
    uint256 _tokenId
  )
  {
    require(idToOwner[_tokenId] != address(0), "not valid");
    _;
  }

  function tokenURI(
    uint256 _tokenId
  )
    external
    
    view
    validNFToken(_tokenId)
    returns (string memory)
  {
    return _tokenURI(_tokenId);
  }

  function _tokenURI(
    uint256 _tokenId
  )
    internal
    virtual
    view
    returns (string memory)
  {
    return tokenIdToUri[_tokenId];
  }

  function _setTokenUri(uint256 _tokenId,string memory _uri)internal validNFToken(_tokenId)
  {
    tokenIdToUri[_tokenId] = _uri;
  }

}
