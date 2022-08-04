# aesecbdecryptor

This script analyzes the blocks inside the AES-ECB encrypted data and   
assigns a color for each same block and create a picture.
![demo](https://shino.club/aesecbdecryptor/sample.png)  
![demo2](https://shino.club/aesecbdecryptor/aesecb.gif)

## Online Demo
https://shino.club/aesecbdecryptor/

## Practice
Try to crack this file.
https://github.com/Sh1n0g1/aesecbdecryptor/raw/main/crackme.enc

## Requirements
* Python3
* Pillow library  
`pip install pillow`

## Usage
`python aes_ecb.py <encfilename>`  
`python aes_ecb.py <encfilename> <width>`  
`python aes_ecb.py <encfilename> <width> <offset>`  
