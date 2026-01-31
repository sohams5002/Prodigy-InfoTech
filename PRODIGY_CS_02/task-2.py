import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

class RealWorldImageEncryptor:
    def __init__(self, key: bytes = None):
   
        self.key = key if key else AESGCM.generate_key(bit_length=256)

    def encrypt_image(self, input_path: str, output_path: str):
       
        with open(input_path, 'rb') as f:
            data = f.read()

       
        nonce = os.urandom(12)
        aesgcm = AESGCM(self.key)
        
        ciphertext = aesgcm.encrypt(nonce, data, None)

    
        with open(output_path, 'wb') as f:
            f.write(nonce + ciphertext)
            
    def decrypt_image(self, input_path: str, output_path: str):
        with open(input_path, 'rb') as f:
            file_content = f.read()

 
        nonce = file_content[:12]
        ciphertext = file_content[12:]

        aesgcm = AESGCM(self.key)
        
       
        decrypted_data = aesgcm.decrypt(nonce, ciphertext, None)

        with open(output_path, 'wb') as f:
            f.write(decrypted_data)

my_key = b'\x01' * 32 
cipher = RealWorldImageEncryptor(my_key)

cipher.encrypt_image("sensitive_scan.jpg", "secure_vault.enc")
print("Image encrypted using AES-256-GCM.")

cipher.decrypt_image("secure_vault.enc", "restored_image.jpg")
print("Image decrypted successfully.")