from PIL import Image

def encrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert("RGBA")  # handle both RGB and RGBA
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b, a = pixels[i, j]
            # apply encryption only on RGB, keep alpha unchanged
            pixels[i, j] = (
                (r + key) % 256,
                (g + key) % 256,
                (b + key) % 256,
                a
            )

    img.save("encrypted_image.png")
    print("Image encrypted successfully! Saved as encrypted_image.png")


def decrypt_image(image_path, key):
    img = Image.open(image_path)
    img = img.convert("RGBA")
    pixels = img.load()

    for i in range(img.size[0]):
        for j in range(img.size[1]):
            r, g, b, a = pixels[i, j]
            pixels[i, j] = (
                (r - key) % 256,
                (g - key) % 256,
                (b - key) % 256,
                a
            )

    img.save("decrypted_image.png")
    print("Image decrypted successfully! Saved as decrypted_image.png")


def main():
    print("=== Image Encryption Tool ===\n")
    path = input("Enter the image file name (e.g., sample.png): ")
    key = int(input("Enter encryption key (e.g., 50): "))
    mode = input("Choose mode (encrypt/decrypt): ").lower()

    if mode == "encrypt":
        encrypt_image(path, key)
    elif mode == "decrypt":
        decrypt_image(path, key)
    else:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")


if __name__ == "__main__":
    main()
