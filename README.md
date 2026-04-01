# CSCI 352: Personal Project - Student Instructions

Welcome to your Personal Project! You have been assigned a unique file named after your Student CWID (e.g., `50399920`). This file contains the components needed to complete your project, but it requires some technical investigation to unlock.

## General Steps

### Step 1: Identify the File Type
The file you received currently has **no extension**. Your first task is to identify the file format using a "Magic Number" or a file identification tool (like the `file` command in a terminal).
*   **Hint**: Once identified, add the appropriate extension to the file to open it.

### Step 2: Extract the Package
Inside the newly identified archive, you will find two files:
1.  **An Image File**: `[FirstName][LastName].jpg`.
2.  **A Data File**: Another extensionless file named with your **CWID**.

### Step 3: Identify the Second Magic Number
The hidden data file also has no extension. Repeat the identification process to find its magic number.
*   **Hint**: This is a legacy file format. Rename it with the correct extension to see your QR code bit matrix.

### Step 4: Extract the Hidden Hint
The image file in your package has a secret hint hidden inside it using steganography.
*   To extract it, use the provided `extract_hint.py` script.
*   **Command**: `python3 extract_hint.py <your_image.jpg> <your_cwid>`
*   The **CWID** serves as your decryption password.

### Step 5: Solve the QR Code
Using the **Bit Matrix** from the data file and the **Hint** from the image:
1.  Reconstruct the QR code (1 = black module, 0 = white module).
2.  Remove the padding specified in the hint.
3.  Scan the resulting QR code to reveal your **Unique Secret Key**.

### Step 6: Submission
Submit your Secret Key along with your project report with screenshots of all the steps.

---
**Technical Note**: If you encounter issues identifying magic numbers, look for the first few bytes of the file in a Hex Editor. Common headers:
*   `PK\x03\x04` -> ?
*   `D0 CF 11 E0` -> ?
