def change_zero_last_bits(bits, num_of_bits):
    bits_list = list(str(bits))
    for i in range(num_of_bits):
        bits_list[-(i+1)] = '0'

    return int("".join(bits_list))
