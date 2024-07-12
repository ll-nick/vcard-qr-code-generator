# vCard QR Code Generator
This is a simple Python script to interactively generate a QR Code containing vCard information. It utilizes the qrcode library to create the QR Code image.

## Requirements
- Python 3.x
- qrcode Python library

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

## Example
Here's a sample interaction when running the script:

```console
$ python3 generate_vcard_qr_code.py
Please enter the following information for the vCard:
First Name: John
Last Name: Doe
Organization: Example Inc.
URL: https://example.com
Email: john.doe@example.com
Phone: +1234567890
Street + number: 123 Main St
City: Anytown
Postal Code: 12345
Country: USA
vCard QR code generated and saved as 'vCardQR.png'.
```

You can then scan `vCardQR.png` using a QR Code scanner app to import the vCard information into your contacts.