# HMAC server with SHA256

import asyncio
import websockets
import hashlib

def gen_sha256_hmac(message, key):
    blocksize = 64

    # ipad and opad
    trans_5C = bytes((x ^ 0x5C) for x in range(256))
    trans_36 = bytes((x ^ 0x36) for x in range(256))

    # Key padding
    key_bytes = key.encode().ljust(blocksize, b'\\0')

    # Xor key with ipad
    xored_key_bytes_ipad = key_bytes.translate(trans_36)

    # HMAC calculation
    h1 = hashlib.sha256(xored_key_bytes_ipad + message.encode()).digest()
    xored_key_bytes_opad = key_bytes.translate(trans_5C)
    return hashlib.sha256(xored_key_bytes_opad + h1).hexdigest()

async def serve(websocket, path):
    shared_key = "supersecret"
    await websocket.send("Please provide me a comma-separated message,hmac")
    client_data = await websocket.recv()
    client_message, client_hmac = client_data.split(",")
    server_hmac = gen_sha256_hmac(client_message, shared_key)

    if client_hmac == server_hmac:
        await websocket.send("Access granted!")
    else:
        await websocket.send("Access denied!")

print("Server started!")
start_server = websockets.serve(serve, "localhost", 1234)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
