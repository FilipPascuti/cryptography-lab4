from typing import Tuple

alphabet = " abcdefghijklmnopqrstuvwxyz"


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
    pass


def encrypt(plaintext: str, public_key) -> str:
    pass


def decrypt(ciphertext: str, private_key) -> str:
    pass


def main():
    print_problem_statement()
    start = int(input(">>>lower bound: \n"))
    end = int(input(">>>upper bound: \n"))
    public_key, private_key = generate_keys(start, end)
    print(f"The public key is: {public_key} and the private key is {private_key}")

    plaintext = input("text to encrypt: \n")
    encrypted_text = encrypt(plaintext, public_key)
    print(f"The encrypted text is: {encrypted_text}")

    ciphertext = input("text to decrypt: \n")
    decrypted_text = decrypt(ciphertext, private_key)
    print(f"The decrypted text is: {decrypted_text}")


if __name__ == "__main__":
    main()
