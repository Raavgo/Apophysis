# 🧬 What is RLSB?
**RLSB (Randomized Least Significant Bit)** is a variation of traditional LSB steganography that adds an additional layer of obfuscation by randomizing the locations of payload embedded within a digital image.
RLSB uses a **pseudo-random shuffle** of pixel positions to ensure that the embedding pattern is non-deterministic.

---

## 🧱 What is a Pixel?
A **pixel** (short for "picture element") is the smallest unit of a digital image. 
Each pixel consists of **three color channels** - **Red, Green** and **Blue** (RGB).
Each channel stores a value between 0 - 255, in essence 8 bits per channel, resulting in **24 bits per pixel**.

A pixel might be represented in binary as the following:

| R (Red)  | G (Green) | B (Blue) |
|----------|-----------|----------|
| 11001000 | 10111001  | 11100010 |


## 📘 RLSB embedding theory
The RLSB embedding technique modifies the **least significant bit** in each color channel, allowing up to **3 bits of hidden data per pixel**, meaning, one per channel, without noticeably altering image representation.
Unlike traditional LSB, which embeds data sequentially, RLSB uses a **pseudo-randomized pixel order** to scatter the payload across the image.
This randomness is governed by a fixed **seed value**, allowing for reconstruction of the embedding order during decoding.

RLSB is particularly effective in evading statistical steganalysis tools that focus on pixel sequence or pattern recognition.
Despite randomization, the embedded image remains visually indistinguishable from the original to the human eye.

The following table illustrates the embedding procedure in RLSB, where each payload bit is pseudo-randomly assigned to a pixel (pixel position) in a non-sequential order.

| **Pixel Position** | Channel | Original Binary  | Secret Bit | Modified Binary  |
|--------------------|---------|------------------|------------|------------------|
| (42, 17)           | Red     | 1100100**0**     |     1      | 1100100**1**     |
| (12, 88)           | Green   | 1011100**1**     |     0      | 1011100**0**     |
| (5, 3)             | Blue    | 1110001**0**     |     1      | 1110001**1**     |

🛈 *Note: The least significant bit is not simply "flipped" but replaced with the intended secret bit. If the bit is already correct, it remains unchanged. This ensures the hidden message is preserved while keeping visual distortion to a minimum.*


# ⚙️ How does the RLSB embedding code work?
The class RLSB implements two main functions as well as a helper function.

---

## Function Method
**Aim**: Embedding of the secret payload (a binary executable) into the image using RLSB steganography.

The function takes a cover image and a binary executable as input.
The executable payload is first converted to a hexadecimal string and then into a binary bitstream with a null character (\x00) appended to signal the end of the payload.
The pixel positions within the image are stored in a list, which is then shuffled using a randomization process controlled by a fixed seed.
The function then iterates over the list of shuffled pixel positions. 
For each pixel, the least significant bit of each color channel (Red, Green and Blue) is replaced with the next bit from the payload bitstream. 
This continues until all payload bits are embedded or all pixels are processed.
The modified pixel values are then written back to the image, creating a cover image that appears visually unchanged but contains the embedded hidden data.

## Reverse Function Method
**Aim**: Extraction of the hidden payload from the cover image.

The positions of the pixels are shuffled again using the same fixed seed value, ensuring the pixel order matches the one used during the embedding process.
The function then iterates over the shuffled pixel positions, extracting the least significant bit from each color channel of the pixel (Red, Green and Blue).
These bits are collected and concatenated to a bitstream.
The bitstream is then grouped into bytes, and each byte is converted back into its corresponding character.
The characters are then concatenated to reconstruct the original payload.
The null character (\x00) marks the end of the payload, and any data beyond the null character gets discarded.

## Limiter Function Method
**Aim**: Sets a limit on how much data can be embedded into the cover image.

The limiter_function calculates the maximum size of payload that can be embedded based on the dimensions of the image.
It does so by multiplying the total number of pixels by 3 (one for each color channel) and dividing the result by 8 to convert the total bit capacity into bytes.
This ensures the payload remains within the image capacity and prevents data overflows.

---

# 🚀 How is RLSB invoked?
The RLSB class inherits from a shared base class called <em>EmbeddingBase</em>.
It is designed to be invoked as part of the embedding pipeline.