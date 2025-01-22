# HMAC client with SHA256

import asyncio
import websockets
import hashlib

def gen_sha256_hmac(message, key):
    blocksize = 64
    trans_5C = bytes((x ^ 0x5C) for x in range(256))
    trans_36 = bytes((x ^ 0x36) for x in range(256))
    key_bytes = key.encode().ljust(blocksize, b'\\0')

    xored_key_bytes_ipad = key_bytes.translate(trans_36)
    h1 = hashlib.sha256(xored_key_bytes_ipad + message.encode()).digest()
    xored_key_bytes_opad = key_bytes.translate(trans_5C)
    return hashlib.sha256(xored_key_bytes_opad + h1).hexdigest()

async def try_auth(uri):
    async with websockets.connect(uri) as websocket:
        shared_key = "supersecret"
        message = "Hello from Kirill"
        await websocket.recv()
        message_HMAC = gen_sha256_hmac(message, shared_key)
        await websocket.send(f"{message},{message_HMAC}")
        print(await websocket.recv())

asyncio.get_event_loop().run_until_complete(try_auth('ws://localhost:1234'))
