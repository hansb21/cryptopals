import string

base64_chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + "+/"

base64_encoding_table = {i: char for i, char in enumerate(base64_chars)}


def hex_to_bin(hex_string):

    # 1 - Converts hexadecimal value to integer
    # 2 - Converts integer value to binary and removes "0b" prefix
    # 3 - Ensure the result is a multiple of 4 by paddind the binary string with leading zeros

    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)


def bin_to_base64(bin_string):
    bin_chunks = [bin_string[i : i + 6] for i in range(0, len(bin_string), 6)]

    base64_string = ""

    for i in bin_chunks:
        base64_string += base64_encoding_table[int("0b" + i, 2)]

    return base64_string


bin_str = hex_to_bin(
    "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
)
print(
    bin_to_base64(bin_str)
)  # SdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
