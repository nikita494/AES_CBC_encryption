from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad


def encrypt(data, key, iv):
    return AES.new(key, AES.MODE_CBC, iv).encrypt(pad(data, 16))


def main():
    path = input('Path to file:')
    try:
        file = open(path, "rb+")
    except FileNotFoundError:
        print("Oops! Can`t find file. Check path to it")
        exit(-1)
    iv, key = get_random_bytes(16), get_random_bytes(32)
    print(f'IV: {iv.hex()}')
    print(f'Key: {key.hex()}')
    data = file.read()
    file.seek(0)
    file.write(encrypt(data, key, iv))
    file.close()
    print("Encryption complete.")


if __name__ == "__main__":
    main()
