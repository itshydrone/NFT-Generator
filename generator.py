from PIL import Image
import os
import random
from time import sleep
import json
from config import *  

"""
IMPORTANT: Update config.py with your own variables
"""

# Reset variables
possibleOutput = 1
totalMetadata = []
weightedTraits = {}

# Create weighted traits dictionary
for trait in traits:
    traitFiles = os.listdir(os.path.dirname(os.path.realpath(__file__)) + "\\traits\\" + trait)

    possibleOutput = possibleOutput * len(traitFiles)

    weightedTraits[trait] = []

    # Iterate through each variation of trait
    for traitFile in traitFiles:
        traitSplit = traitFile.split("#")
        traitProbRaw = traitSplit[1]

        traitProbRawSplit = traitProbRaw.split(".")
        traitProb = traitProbRawSplit[0]

        traitList = [traitFile] * int(traitProb)
        weightedTraits[trait].append(traitList)

# If not enough traits
if possibleOutput < imageCount:
    print("Not enough traits")
    exit()

# Reset variables
completedOutput = []
outputCount = 0

# Check the blockchain being used
if blockchain.upper() == "SOL":
    devAddress = "Cp4qLAgcAoNgg6aH1scCiVVH48iNjtTikiQMsiSztcCm"
else:
    devAddress = "0xfa1db77200f3Ca7B9171b2c362484a1A1374243d"

# While more images need to be generated
while outputCount < imageCount:
    # Reset variables
    layerFiles = {}
    outputString = ""

    # Create metadata
    metadataDict = {} 
    metadataDict["name"] = nameFormat.replace("[NUMBER]", str(outputCount))
    metadataDict["description"] = description
    metadataDict["image"] = str(outputCount) + ".png"
    metadataDict["edition"] = outputCount
    metadataDict["seller_fee_basis_points"] = int(royalty * 100)
    metadataDict["collection"] = {}
    metadataDict["collection"]["name"] = collectionName
    metadataDict["collection"]["family"] = collectionFamily
    metadataDict["symbol"] = symbol
    metadataDict["properties"] = {}
    metadataDict["properties"]["files"] = []

    filesDict = {}
    filesDict["uri"] = str(outputCount) + ".png"
    filesDict["type"] = "image/png"
    metadataDict["properties"]["files"].append(filesDict)

    metadataDict["properties"]["category"] = "image"
    metadataDict["properties"]["creators"] = []

    royaltyDict = {}
    royaltyDict["address"] = royaltyAddress
    royaltyDict["share"] = 100
    metadataDict["properties"]["creators"].append(royaltyDict)

    metadataDict["attributes"] = []

    # Get traits
    for trait in traits:
        traitChoice = random.choice(weightedTraits[trait])[0]
        outputString += traitChoice

        layerFiles[trait] = Image.open(os.path.dirname(os.path.realpath(__file__)) + "\\traits\\" + trait + "\\" + traitChoice)
        layerFiles[trait] = layerFiles[trait].convert("RGBA")

        traitChoiceSplit = traitChoice.split("#")
        traitChoiceName = traitChoiceSplit[0]

        metadataTraits = {}
        metadataTraits["trait_type"] = trait
        metadataTraits["value"] = traitChoiceName
        metadataDict["attributes"].append(metadataTraits)

    # If image hasn't been created before
    if outputString not in completedOutput:
        completedOutput.append(outputString)

        output = layerFiles[traits[0]]

        # Layer traits
        for trait in traits:
            if trait != traits[0]:
                output.paste(layerFiles[trait], (0,0), mask = layerFiles[trait])

        # Save image
        output.save(os.path.dirname(os.path.realpath(__file__)) + "\\output\\" + str(outputCount) + ".png","PNG")

        # Save metadata
        jsonString = json.dumps(metadataDict, indent = 4) 
        textFile = open(os.path.dirname(os.path.realpath(__file__)) + "\\output\\" + str(outputCount) + ".json", "w")
        textFile.write(jsonString)
        textFile.close()

        totalMetadata.append(metadataDict)

        print("Saving " + str(outputCount) + ".png")

        outputCount = outputCount + 1
    
    else:
        print("Already done this combination")

# Save overall metadata
jsonString = json.dumps(totalMetadata, indent = 4) 
textFile = open(os.path.dirname(os.path.realpath(__file__)) + "\\output\\_metadata.json", "w")
textFile.write(jsonString)
textFile.close()