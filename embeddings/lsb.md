# 🧬 What is LSB?
**LSB (Least Significant Bit)** is a simple yet powerful steganographic technique used to hide secret information inside digital images.
It works by modifying the least significant bit of each pixel's color channel. In fact, these tiny changes are so subtle that they are visually invisible to the human eye. 👁️

---

## 🧱 What is a Pixel?
A **pixel** (short for "picture element") is the smallest unit of a digital image. 
Each pixel consists of **three color channels** - **Red, Green** and **Blue** (RGB).
Each channel stores a value between 0 - 255, in essence 8 bits per channel, resulting in **24 bits per pixel**.

A pixel might be represented in binary as the following:

| R (Red)  | G (Green) | B (Blue) |
|----------|-----------|----------|
| 11001000 | 10111001  | 11100010 |


## 📘 LSB embedding theory
The LSB embedding technique targets the **last bit** in each color channel.
This allows up to **3 bits of hidden data per pixel**, meaning, one per channel, without noticeably affecting the image representation.

| Channel | Original Binary | Secret Bit | Modified Binary |
|---------|-----------------|------------|-----------------|
| Red     | 1100100**0**    |     1      | 1100100**1**    |
| Green   | 1011100**1**    |     0      | 1011100**0**    |
| Blue    | 1110001**0**    |     1      | 1110001**1**    |

🛈 *Note: The least significant bit is not simply "flipped" but replaced with the intended secret bit. If the bit is already correct, it remains unchanged. This ensures the hidden message is preserved while keeping visual distortion to a minimum.*


# ⚙️ How does the LSB embedding code work?
The class LSB implements two main functions as well as a helper function.

---

## Function Method
**Aim**: Embedding of the secret payload (a binary executable) into the image using LSB steganography.

The function takes a cover image and a binary executable as input.
The executable is first converted into a hexadecimal string and then to a binary bitstream, with a null character (\x00) appended to signal at the end of the payload.
The function then iterates over all pixels in the image (row by row), and for each pixel, it replaces the least significant bit of each color channel (Red, Green, Blue) with one bit from the payload.
This process continues until the entire payload is embedded within the cover image.
The resulting image looks visually unchanged but now contains the embedded data.

## Reverse Function Method
**Aim**: Extraction of the hidden payload from the cover image.

The reverse_function performs the decoding of the embedded data back to the original byte format.
It iterates through all pixels in the image and extracts the LSB from each RGB color channel into a list of bits.
These bits are then grouped into bytes (8 Bit = 1 Byte) and converted back to characters.
Once the null character (\x00) is detected, the function stops and converts the collected character string back from hexadecimal into the original byte format of the payload.

## Limiter Function Method
**Aim**: Sets a limit on how much data can be embedded into the cover image.

The limiter_function calculates the maximum size of the payload that can be embedded based on the dimensions of the image.
This is conducted by multiplying the total number of pixels by 4 (3 channels + 1 control byte per pixel), and then dividing by 8 to get the size in bytes.
The function serves to avoid data overflows and ensures that the payload fits within the image capacity.

---

# 🚀 How is LSB invoked?
The LSB class inherits from a shared base class called <em>EmbeddingBase</em>.
It is designed to be invoked as part of the embedding pipeline.