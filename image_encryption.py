from PIL import Image
import numpy as np

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)

    # Example encryption: Add key to each pixel value
    encrypted_pixels = (pixels + key) % 256

    encrypted_image = Image.fromarray(encrypted_pixels.astype('uint8'))
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    pixels = np.array(image)

    # Example decryption: Subtract key from each pixel value
    decrypted_pixels = (pixels - key) % 256

    decrypted_image = Image.fromarray(decrypted_pixels.astype('uint8'))
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved to {output_path}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Encrypt or decrypt an image using pixel manipulation.")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt")
    parser.add_argument("input_path", help="Path to the input image")
    parser.add_argument("output_path", help="Path to save the output image")
    parser.add_argument("key", type=int, help="Encryption/Decryption key (integer value)")

    args = parser.parse_args()

    if args.mode == "encrypt":
        encrypt_image(args.input_path, args.output_path, args.key)
    elif args.mode == "decrypt":
        decrypt_image(args.input_path, args.output_path, args.key)
