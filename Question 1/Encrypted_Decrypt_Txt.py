def encrypt_char(c, n, m):
    if c.islower():
        if c <= 'm':
            return chr((ord(c) - ord('a') + (n * m)) % 26 + ord('a'))
        else:
            return chr((ord(c) - ord('a') - (n + m)) % 26 + ord('a'))
    elif c.isupper():
        if c <= 'M':
            return chr((ord(c) - ord('A') - n) % 26 + ord('A'))
        else:
            return chr((ord(c) - ord('A') + (m ** 2)) % 26 + ord('A'))
    else:
        return c

def decrypt_char(c, n, m):
    if c.islower():
        if chr((ord(c) - ord('a') - (n * m)) % 26 + ord('a')) <= 'm':
            return chr((ord(c) - ord('a') - (n * m)) % 26 + ord('a'))
        else:
            return chr((ord(c) - ord('a') + (n + m)) % 26 + ord('a'))
    elif c.isupper():
        if chr((ord(c) - ord('A') + n) % 26 + ord('A')) <= 'M':
            return chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        else:
            return chr((ord(c) - ord('A') - (m ** 2)) % 26 + ord('A'))
    else:
        return c

def encrypt_file(n, m):
    with open("raw_text.txt", "r") as infile:
        content = infile.read()

    encrypted = ''.join(encrypt_char(c, n, m) for c in content)

    with open("encrypted_text.txt", "w") as outfile:
        outfile.write(encrypted)

def decrypt_file(n, m):
    with open("encrypted_text.txt", "r") as infile:
        encrypted = infile.read()

    decrypted = ''.join(decrypt_char(c, n, m) for c in encrypted)

    with open("decrypted_text.txt", "w") as outfile:
        outfile.write(decrypted)

def verify_files():
    with open("raw_text.txt", "r") as original, open("decrypted_text.txt", "r") as decrypted:
        return original.read() == decrypted.read()

def main():
    try:
        n = int(input("Enter value for n: "))
        m = int(input("Enter value for m: "))

        encrypt_file(n, m)
        print("Encryption complete. Output written to encrypted_text.txt.")

        decrypt_file(n, m)
        print("Decryption complete. Output written to decrypted_text.txt.")

        if verify_files():
            print("✅ Verification passed. The decrypted text matches the original.")
        else:
            print("❌ Verification failed. The decrypted text does not match the original.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
