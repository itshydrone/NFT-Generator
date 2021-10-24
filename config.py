"""
Fill in your information in the configuration variables below
"""

traits = [
    "Background", 
    "Pumpkin Color",
    "Headwear",
    "Mouth",
    "Nose",
    "Emotions",
    "Extras",
    "Eyes"
] # The different layers and the order that they will be used - MUST be same as trait layer folders
imageCount = 5 # Total number of images to create
nameFormat = "Pumpkin #[NUMBER]" # The name of each NFT - '[NUMBER]' will be replaced with the NFT number
description = "These spooky pumpkins have arrived on the blockchain just in time for Halloween! Make sure you don't miss out!" # Description of collection
royalty = 2.5 # Royalty percentage (we take a 25% cut of this royalty)
royaltyAddress = "6R1YMnnjWsj93V438whWkimCimNzAKKRid7QkUfpkCxF" # Address to pay the royalties to
collectionName = "HalloweeNFT" # Name of collection
collectionFamily = "HalloweeNFT" # Name of family (often same as collection)
symbol = "" # Symbol (often blank)
blockchain = "ETH" # ETH or SOL