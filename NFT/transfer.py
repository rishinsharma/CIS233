from secrets import ALGOD_HEADERS, ALGOD_ADDRESS, account_address, account_private_key
from algosdk.future import transaction
from algosdk.future.transaction import AssetTransferTxn
from algosdk.v2client import algod

algod_client = algod.AlgodClient(
    algod_token = "", 
    algod_address = ALGOD_ADDRESS,
    headers = ALGOD_HEADERS
)
ASSET_ID = 82006992

def wait_for_confirmation(client, transaction_id, timeout):
    start_round = client.status()["last-round"] + 1
    current_round = start_round

    while current_round < start_round + timeout:
        try:
            pending_txn = client.pending_transaction_info(transaction_id)
        except Exception:
            return

        if pending_txn.get("confirmed-round", 0) > 0:
            return pending_txn
        elif pending_txn["pool-error"]:
            raise Exception('pool error: {}'.format(pending_txn["pool-error"]))

        client.status_after_block(current_round)
        current_round += 1

    raise Exception('pending tx not found in timeout rounds, timeout value = : {}'.format(timeout))

params = algod_client.suggested_params()

txn = AssetTransferTxn(
    sender=account_address,
    sp=params,
    receiver='UAHTM3EC3PTNDYBA5AGPHVBMXOK4YQE3N23VQEUFAMTHY3AXHBUXDHIWKE',
    amt=1,
    index=ASSET_ID)

stxn = txn.sign(account_private_key)


# Send the transaction to the network and retrieve the txid.
try:
    txid = algod_client.send_transaction(stxn)
    print("Signed transaction with txID: {}".format(txid))
    # Wait for the transaction to be confirmed
    confirmed_txn = wait_for_confirmation(algod_client, txid, 4) 
    print("TXID: ", txid)
    print("Result confirmed in round: {}".format(confirmed_txn['confirmed-round']))
except Exception as err:
    print(err)
