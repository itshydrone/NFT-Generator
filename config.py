"""
Fill in your information in the configuration variables below
"""

traits = [
    "Background", 
    "Pumpkin Color",
    "Headwear",
    "Mouth",
    "Nose",
    "Extras",
    "Eyes"
] # The different layers and the order that they will be used - MUST be same as trait layer folders
imageCount = 1 # Total number of images to create
nameFormat = "NFT #[NUMBER]" # The name of each NFT - '[NUMBER]' will be replaced with the NFT number
description = "Really awesome description!" # Description of collection
royalty = 2.5 # Royalty percentage (we take a 25% comission of this royalty, e.g. if you set 4% royalties, you get 3% and we get 1%)
royaltyAddress = "6R1YMnnjWsj93a438whWkimCimNzAgKRid7QkUfpkCxF" # Address to pay the royalties to
collectionName = "Cool collection" # Name of collection
collectionFamily = "Cool collection" # Name of family (often same as collection)
symbol = "" # Symbol (often blank)
blockchain = "ETH" # ETH or SOL