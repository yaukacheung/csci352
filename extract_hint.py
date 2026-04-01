import base64
from stegano import exifHeader
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import sys

def derive_key(password: str) -> bytes:
    """Derive the same Fernet key as the embedding script."""
    salt = b'csci352_rellis_project' 
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password.encode()))
    return key

def decrypt_message(encrypted_message: str, password: str) -> str:
    """Decrypt the message using the student's password (CWID)."""
    key = derive_key(password)
    f = Fernet(key)
    return f.decrypt(encrypted_message.encode()).decode()

def main():
    if len(sys.argv) < 3:
        print("Usage: python extract_hint.py <image_path> <cwid>")
        sys.exit(1)
        
    image_path = sys.argv[1]
    password = sys.argv[2]
    
    try:
        # Step 1: Extract the hidden data from EXIF header
        encrypted_hint = exifHeader.reveal(image_path)
        
        # Step 2: Decrypt the hidden data using the CWID
        decrypted_hint = decrypt_message(encrypted_hint.decode() if isinstance(encrypted_hint, bytes) else encrypted_hint, password)
        print(f"\n--- SUCCESS ---")
        print(f"Decrypted Hint: {decrypted_hint}")
    except Exception as e:
        print(f"\n--- ERROR ---")
        print(f"Failed to extract or decrypt. Possible reasons:")
        print(f"1. Incorrect CWID (Password).")
        print(f"2. Image file is corrupted or not a valid steganography image.")
        print(f"3. Path to image is incorrect.")
        # print(f"Raw error: {e}")

if __name__ == "__main__":
    main()
