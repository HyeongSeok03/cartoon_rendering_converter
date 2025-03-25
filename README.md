# cartoon_rendering_converter

This Python script converts a normal image into a **cartoon-style image** by combining **edge detection** and **color quantization** techniques.

---

## Features

- **Bold edges**: Detected using adaptive thresholding on blurred grayscale images.
- **Flat color regions**: Created using k-means clustering to simulate a hand-drawn feel.
- Can be easily adapted to save or batch-process multiple images.

---

## 📂 Input

The script loads the image from:

## bad demo
- original

![Image](https://github.com/user-attachments/assets/06b25ed8-5bb1-4072-96fa-39ef96065f88)

- cartoon

<img width="719" alt="Image" src="https://github.com/user-attachments/assets/728e4818-1973-4815-aeca-423f43b8c74d" />

- Low contrast between subject and background
- Flat lighting with little shading
- Monotone colors → poor color segmentation
- Too many unnecessary edge lines from textures (e.g. hat)
- Cartoon effect looks noisy and unclear



## good demo
- original

![Image](https://github.com/user-attachments/assets/5506cd0e-e521-4a71-85e9-18ad7d9acec5)

- cartoon

<img width="370" alt="Image" src="https://github.com/user-attachments/assets/5dc11f92-594c-4538-ac67-f154d81e8eb9" />

- Clear contrast between subject and background
- Strong highlights and shadows help edge detection
- Distinct color regions → smooth poster-like surfaces
- Only meaningful edges are emphasized
- Clean and expressive cartoon effect

## Summary
This cartoon rendering algorithm works best when:
- The image has **clear lighting and shadows**
- The subject is **well separated from the background**
- There are **distinct color regions**
- Textures are not overly detailed
