# PRODIGY_CS_02
Pixel Manipulation for Image Encryption and Decryption - Developed a simple image encryption tool using pixel manipulation. This program can perform operations like swapping pixel values or apply a basic mathematical operation to each pixel. It allows users to encrypt & decrypt images.<br><br>
Some prerequisites needed for the program to work:-
1) Make sure you have Python installed on your system.
2) We will use the 'Pillow' library for image manipulation.<br>
The Python file, as well as the 'input_image.jpg' (image file that would be encrypted or decrypted) file must be saved in the same directory of the folder.<br><br?
Explanation of the code:-
1) Imports:<br>
a)PIL (Python Imaging Library) is used for opening and saving images.<br>
b)'numpy' is used for efficient pixel manipulation.<br>
2) Encryption/Decryption Logic: The pixel values are manipulated by adding or subtracting a key. The modulo operation ensures the values stay within the valid range for pixel values (0-255).<br>
3)Argument Parsing: The script uses 'argparse' to handle command-line arguments, allowing users to specify the mode (encrypt/decrypt), input and output paths, and the key.<br>
#To run the script for encryption, use the following command: python image_encryption.py encrypt input_image.jpg encrypted_image.jpg 42<br>
Replace 'input_image.jpg' with the path to your input image, 'encrypted_image.jpg' with the desired output path, and '42' with your chosen key.<br>
#To run the script for decryption, use the following command: python image_encryption.py decrypt encrypted_image.jpg decrypted_image.jpg 42<br>
Replace 'encrypted_image.jpg' with the path to your encrypted image, 'decrypted_image.jpg' with the desired output path, and '42' with the same key used for encryption.<br><br>
Common mistakes to avoid:-
1)Ensure you are running the command from the correct directory where image_encryption.py is located.
2)Double-check the image file names and paths. They should be accurate and relative to the script's location or absolute paths.<br>
By following these steps, you should be able to run the script without encountering any error.
