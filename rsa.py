# -*- coding: utf-8 -*-
import random
DIGITS = 3


def is_simple(num):
    for i in range(2, num//2):
        if num % i == 0:
            return False
    return True


def get_random_num(digits):
    return random.randint(int("1" + "0" * (digits - 1)), int("9" * digits))


def generate_simple_num(digits):
    num = get_random_num(digits)
    while not is_simple(num):
        num = get_random_num(digits)
    return num


def get_d(m, digits):
    d = generate_simple_num(digits)
    while True:
        if m % d != 0:
            break
        d = generate_simple_num(digits)
    return d


def get_e(d, m):
    i = 1
    while True:
        if (i * m + 1) % d == 0:
            return int((i * m + 1) / d)
        else:
            i += 1


def to_hex(crypted_numbers):
    return [hex(num) for num in crypted_numbers]


def from_hex(encrypted_string):
    hex_edited = encrypted_string.split("0x")[1:]
    return [int("0x" + symb, 0) for symb in hex_edited]


def get_char_nums(inp_string):
    return [ord(symbol) for symbol in inp_string]


def crypt_nums(char_numbers, e, n):
    return [(number ** e) % n for number in char_numbers]


def decrypt_nums(crypted_numbers, d, n):
    return [(number ** d) % n for number in crypted_numbers]


def get_decrypted_string(decrypted_nums):
    return "".join([chr(num) for num in decrypted_nums])


def init_vars():
    p = generate_simple_num(DIGITS)
    q = generate_simple_num(DIGITS)
    print(p, q)
    n = p * q
    m = (p - 1) * (q - 1)
    d = get_d(m, DIGITS)
    print(d, m)
    e = get_e(d, m)
    print(e)
    return p, q, n, m, d, e


def rsa_encrypt(inp_string, e, n):
    char_numbers = get_char_nums(inp_string)
    crypted_numbers = crypt_nums(char_numbers, e, n)
    hex_crypted = to_hex(crypted_numbers)
    hex_string = "".join(hex_crypted)
    return hex_string


def rsa_decrypt(hex_crypted, d, n):
    dec_crypted = from_hex(hex_crypted)
    decrypted_nums = decrypt_nums(dec_crypted, d, n)
    decrypted_string = get_decrypted_string(decrypted_nums)
    return decrypted_string


def main():
    p, q, n, m, d, e = init_vars()
    inp_string = input()
    encrypted_string = rsa_encrypt(inp_string, e, n)
    decrypted_string = rsa_decrypt(encrypted_string, d, n)
    print(encrypted_string)
    print(decrypted_string)


if __name__ == "__main__":
    main()
