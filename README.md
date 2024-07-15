# vCard QR Code Generator
This is a simple Python script to interactively generate a QR Code containing a vCard.

## Requirements
- Python 3.x
- [qrcode](https://github.com/lincolnloop/python-qrcode) Python library

## Installation
1. **Clone the repository:**
```console
git clone https://github.com/ll-nick/vcard-qr-code-generator
cd vcard-qrcode-generator
```
2. **Install dependencies:**
Make sure you have Python 3.x installed. Install the required `qrcode` library using pip:
```console
pip install qrcode
```

## Usage
Run the script from the command line:
```
python3 generate_vcard_qr_code.py
```

Follow the prompts to enter the vCard information:

- First Name
- Last Name
- Organization
- URL
- Email
- Phone
- Street + Number
- City
- Postal Code
- Country

Once all information is provided, the script will generate a vCard in QR Code format and save it as `vCardQR.png` in the current directory.

You can then scan `vCardQR.png` using a QR Code scanner app to import the vCard information into your contacts.

## Customization

You can customize the QR code settings by modifying the constants in the script:
- `QR_VERSION`: QR code version (default: 1)
- `QR_ERROR_CORRECTION`: Error correction level (default: qrcode.constants.ERROR_CORRECT_L)
- `QR_BOX_SIZE`: Size of each QR code box (default: 10)
- `QR_BORDER`: Size of the QR code border (default: 4)

Feel free to adjust these settings to suit your requirements.