// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MonadNFT is ERC721URIStorage, Ownable {

    uint public nextTokenId;
    address public admin;

    constructor() ERC721("MonadBlockNFT", "MBNFT") {
        admin = msg.sender;
    }

    function mint(address to, string memory uri) public {
        require(msg.sender == admin, "Only admin can mint");
        uint tokenId = nextTokenId;
        nextTokenId++;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, uri);
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return "https://ipfs.io/ipfs/";
    }

    function setAdmin(address newAdmin) external onlyOwner {
        admin = newAdmin;
    }
}
