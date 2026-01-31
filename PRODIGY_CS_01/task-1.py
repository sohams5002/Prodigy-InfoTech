import string

class CaesarCipher:
    def __init__(self, shift: int):
        # The shift is normalized to 0-25 using modulo
        self.shift = shift % 26
        self._setup_tables()

    def _setup_tables(self):
        """Pre-computes the translation tables for O(1) character lookup."""
        # Standard alphabets
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        
        # Shifted alphabets
        shifted_lower = lower[self.shift:] + lower[:self.shift]
        shifted_upper = upper[self.shift:] + upper[:self.shift]
        
        # Create a single mapping for both cases
        self.encrypt_table = str.maketrans(lower + upper, shifted_lower + shifted_upper)
        self.decrypt_table = str.maketrans(shifted_lower + shifted_upper, lower + upper)

    def encrypt(self, text: str) -> str:
        return text.translate(self.encrypt_table)

    def decrypt(self, text: str) -> str:
        return text.translate(self.decrypt_table)

# --- Usage Example ---
if __name__ == "__main__":
    # 1. Initialize with a shift (e.g., 13 is 'ROT13')
    cipher = CaesarCipher(shift=3)
    
    # 2. Encrypt a message
    secret = "Python is the future! 2026"
    encrypted = cipher.encrypt(secret)
    print(f"Encrypted: {encrypted}") # Sbwkrq lv wkh ixwxuh! 2026
    
    # 3. Decrypt it back
    decrypted = cipher.decrypt(encrypted)
    print(f"Decrypted: {decrypted}")