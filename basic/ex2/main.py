def hex_to_bin(hex_string):

    # 1 - Converts hexadecimal value to integer
    # 2 - Converts integer value to binary and removes "0b" prefix
    # 3 - Ensure the result is a multiple of 4 by paddind the binary string with leading zeros

    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)


def fixed_xor(hex_string1, hex_string2):
    bin_string1 = hex_to_bin(hex_string1)
    bin_string2 = hex_to_bin(hex_string2)

    return hex(int(bin_string1, 2) ^ int(bin_string2, 2))


print(
    fixed_xor(
        "1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965"
    )
)
