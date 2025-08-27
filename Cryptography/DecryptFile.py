from cryptography.fernet import Fernet
import os
from datetime import datetime

def load_key():
    """
    Load the encryption key from file
    """
    try:
        with open("encryption_key.txt", "rb") as key_file:
            return key_file.read()
    except FileNotFoundError:
        print("[-] Encryption key not found. Make sure encryption_key.txt exists in the same directory.")
        return None

def decrypt_file(encrypted_file, key, output_dir="decrypted_files"):
    """
    Decrypt a single file and save it to the output directory
    """
    try:
        # Create output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Get the original filename without the 'e_' prefix
        original_name = encrypted_file[2:] if encrypted_file.startswith('e_') else encrypted_file
        output_path = os.path.join(output_dir, f"decrypted_{original_name}")

        with open(encrypted_file, 'rb') as f:
            data = f.read()

        fernet = Fernet(key)
        decrypted = fernet.decrypt(data)

        with open(output_path, 'wb') as f:
            f.write(decrypted)
        
        print(f"[+] Successfully decrypted {encrypted_file} to {output_path}")
        return True

    except Exception as e:
        print(f"[-] Failed to decrypt {encrypted_file}: {str(e)}")
        return False

def main():
    # Load the encryption key
    key = load_key()
    if not key:
        return

    # Define the encrypted files
    encrypted_files = {
        'e_system.txt': 'System Information',
        'e_clipboard.txt': 'Clipboard Data',
        'e_keys_logged.txt': 'Keylog Data',
        'e_audio.wav': 'Audio Recording',
        'e_screenshot.png': 'Screenshot'
    }

    # Create timestamp for this decryption session
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = f"decrypted_files_{timestamp}"

    print("\n=== ShadowKey Decryption Tool ===")
    print(f"Starting decryption at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Output directory: {output_dir}")
    print("=" * 30 + "\n")

    # Decrypt each file
    successful = 0
    for enc_file, desc in encrypted_files.items():
        if os.path.exists(enc_file):
            if decrypt_file(enc_file, key, output_dir):
                successful += 1
        else:
            print(f"[-] {desc} file not found: {enc_file}")

    print(f"\nDecryption complete: {successful}/{len(encrypted_files)} files processed")

if __name__ == "__main__":
    main()
