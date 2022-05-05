from algosdk import mnemonic

# TODO
PINATA_API_KEY = "ee8a153acc33b2ee9766"
PINATA_API_SECRET = "9fea9798742c79c22415c1b3b460ba471a1e826ed283c54017a72b177c3f38dc"

# TODO
PURESTAKE_API_KEY = "Umcu1tQNS52lDCwjXHKYE1CmY2aPk5CW5NEAUFQC"

# TODO
account_mnemonic = "pluck weather pioneer brown sun treat ten write select result menu diary wisdom damp float oppose dance civil magnet dizzy more kid believe absorb moon" 
account_private_key = mnemonic.to_private_key(account_mnemonic)
account_address = mnemonic.to_public_key(account_mnemonic)

ALGOD_ADDRESS = "https://testnet-algorand.api.purestake.io/ps2"
ALGOD_HEADERS = {"X-API-Key": PURESTAKE_API_KEY}
