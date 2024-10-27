import hashlib

test_text = "I love dogs"

hash_obj = hashlib.sha256()

hash_obj.update(test_text.encode())

hex_hash = hash_obj.hexdigest()

with open('text.txt', 'r+') as file:
    hex_text = file.read()
    if hex_hash in hex_text:
        print("It's here!")
    else:
        print("It's not here")
        file.writelines('\n' + hex_hash)

print(f"Test: {hex_hash}")
