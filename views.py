from django.http import HttpResponse
import requests
from secrets import ALGOD_HEADERS, ALGOD_ADDRESS

# TODO USE THIS package
from algosdk.v2client import algod

# TODO Feel free to copy-paste the secrets.py file into the Step3 folder and import it here

PINATA_GATEWAY = "https://gateway.pinata.cloud/ipfs/"

# TODO fill me out
ASSET_ID = 82006992

def serve_image(request):
    # TODO modify this function to:
    # 1. Query the algorand blockchain for your NFT
    # 2. Recover the IPFS Metadata address from the NFT
    # 3. Query the metadata from IPFS
    # 4. Extract the IPFS image address
    # 5. Query the image from IPFS
    # 6. Serve the image as an HTTP response

    algod_client = algod.AlgodClient(
        algod_token = "", 
        algod_address=ALGOD_ADDRESS, 
        headers = ALGOD_HEADERS
    )

    nft_data = algod_client.asset_info(ASSET_ID)

    address = nft_data['params']['url']
    section = address.split("//")[1]
    metadata_address = PINATA_GATEWAY+section

    storage = requests.get(metadata_address).json()

    ipfs_image_address = storage['image']
    ipfs_section = ipfs_image_address.split("//")[1]

    ipfs_address = PINATA_GATEWAY+ipfs_section

    storage_image = requests.get(ipfs_address)

    return HttpResponse(storage_image, content_type=storage['image_mimetype'])

def home_page(request):
    return HttpResponse("<h1>Visit localhost:8000/nft to view your NFT!</h1>")