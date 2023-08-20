from Crypto.Hash import keccak

hex_code = '213d031b8d8604d6beca465584de588430badf68624eb9791dabe41ebd765bdc' #your hex code

# Convert hex code to bytes::
message = bytes.fromhex(hex_code)

# Calculate Keccak-256 hash:
hash_obj = keccak.new(digest_bits=256)
hash_obj.update(message)
keccak_hash = hash_obj.hexdigest()

print(keccak_hash)
