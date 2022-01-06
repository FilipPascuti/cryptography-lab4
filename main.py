from typing import Tuple, List
from collections import defaultdict
import math
import random
import sympy


# alphabet = " abcdefghijklmnopqrstuvwxyz"


def print_problem_statement():
    print(
        """
        Create a project with the following features:
        (i) Setting. The alphabet will have 27 characters: 
        the blank and the 26 letters of the English alphabet.
        (ii) Generates a public key and a private key. 
        The public key will be randomly generated in the required interval.
        (iii)Using the public key, encrypts a given plaintext.
        (iv)Using the private key, decrypts a given ciphertext.
        """)


def generate_keys(start: int, end: int) -> Tuple:
    p = sympy.randprime(start, end)
    g = random.randint(2, p - 1)
    a = random.randint(1, p - 2)
    public_key = [p, g, pow(g, a, p)]
    private_key = a

    return public_key, private_key


def get_symmetric_letters_to_numbers():
    alphabet = {" ": 10, 10: " "}
    val = ord('a')
    for idx in range(0, 26):
        letter, key = chr(val + idx), idx + 11
        alphabet[letter] = key
        alphabet[key] = letter
    return alphabet


def translate_plaintext_into_numerical(plaintext, alphabet):
    numerical = []
    for char in plaintext:
        numerical.append(str(alphabet[char]))
    return int("".join(numerical))


def translate_numerical_into_plaintext(numerical, alphabet):
    plaintext = ''
    numerical = str(numerical)
    for index in range(0, len(numerical), 2):
        num = int(numerical[index: index+2])
        plaintext += alphabet[num]
    return plaintext


def encrypt(plaintext: str, public_key) -> List:
    message = translate_plaintext_into_numerical(plaintext, alphabet=get_symmetric_letters_to_numbers())

    p, g, g_a = public_key

    k = random.randint(1, p - 2)

    alpha = pow(g, k, p)

    beta = (message * pow(g_a, k, p)) % p

    return [alpha, beta]


def decrypt(ciphertext: List, public_key, private_key) -> str:
    alpha, beta = ciphertext
    p, g, g_a = public_key

    message = (pow(alpha, -private_key, p) * beta) % p

    message = translate_numerical_into_plaintext(message, alphabet=get_symmetric_letters_to_numbers())

    return message


def main():
    # print_problem_statement()

    # plaintext = input("text to encrypt: \n")
    # plaintext = "a b c d e f g h i j k l m n o p q r s t u v x y z a a a a a a a a a a a a a a a a a a a a a a a a a a a a a a  a a a a a a a a a a a a a a  a aa aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasasasasasasasasasasasasasasas"
    plaintext = "a" * 500
    # start = int(input(">>>lower bound: \n"))
    start = 10 ** (len(plaintext) * 2)
    # end = int(input(">>>upper bound: \n"))
    end = 10 ** (len(plaintext) * 3)

    public_key, private_key = generate_keys(start, end)
    print(f"The public key is: {public_key} and the private key is {private_key}")

    encrypted_text = encrypt(plaintext, public_key)
    print(f"The encrypted text is: {encrypted_text}")

    # ciphertext = input("text to decrypt: \n")
    ciphertext = encrypted_text
    decrypted_text = decrypt(ciphertext, public_key, private_key)
    print(f"The decrypted text is: {decrypted_text}")


if __name__ == "__main__":
    main()
