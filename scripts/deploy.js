// Import necessary Hardhat packages
const hre = require("hardhat");

async function main() {
  // Get the list of accounts from your wallet
  const [deployer] = await hre.ethers.getSigners();

  // Display the account address deploying the contract
  console.log("Deploying contracts with the account:", deployer.address);

  // Deploy the MonadNFT contract
  const MonadNFT = await hre.ethers.getContractFactory("MonadNFT");
  const monadNFT = await MonadNFT.deploy();  // Deploy the contract

  console.log("MonadNFT contract deployed to:", monadNFT.address);

  // Optionally, you can mint an NFT here for testing
  // Example: minting an NFT to the deployer's address
  // const tokenURI = "https://ipfs.io/ipfs/QmSomeIPFSHash";  // Replace with your IPFS URL
  // await monadNFT.mint(deployer.address, tokenURI);
  // console
