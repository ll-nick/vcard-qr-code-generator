#!/usr/bin/env python3

import qrcode

def get_vcard_data():
    print("Please enter the following information for the vCard:")
    
    # Input collection with basic validation
    first_name = input("First Name: ").strip()
    last_name = input("Last Name: ").strip()
    organization = input("Organization: ").strip()
    url = input("URL: ").strip()
    email = input("Email: ").strip()
    phone = input("Phone: ").strip()
    street = input("Street + number: ").strip()
    city = input("City: ").strip()
    postal_code = input("Postal Code: ").strip()
    country = input("Country: ").strip()

    # Ensure required fields are not empty
    if not (first_name and last_name and email and phone and street and city and postal_code and country):
        print("Error: Required fields cannot be empty.")
        return None

    # Construct vCard data
    vcard_data = f"""BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name}
FN:{first_name} {last_name}
ORG:{organization}
URL:{url}
EMAIL;TYPE=work:{email}
TEL;TYPE=work:{phone}
ADR;TYPE=intl,work,postal,parcel:;;{street};{city};;{postal_code};{country}
END:VCARD"""

    return vcard_data

def generate_qr_code(data):
    try:
        # Create the QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("vCardQR.png")
        print("vCard QR code generated and saved as 'vCardQR.png'.")
    except Exception as e:
        print(f"Error generating QR code: {e}")

if __name__ == "__main__":
    # Generate the vCard data
    data = get_vcard_data()

    if data:
        # Create the QR code
        generate_qr_code(data)
