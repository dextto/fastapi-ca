import pickle
import binascii

if __name__ == "__main__":
    serialized_result = binascii.unhexlify("80054B052E")

    result = pickle.loads(serialized_result)

    print(result)
