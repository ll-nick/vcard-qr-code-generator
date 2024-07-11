#!/usr/bin/env python3

import qrcode


def get_vcard_data():
    print("Please enter the following information for the vCard:")

    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    organization = input("Organization: ")
    url = input("URL: ")
    email = input("Email: ")
    phone = input("Phone: ")
    street = input("Street + number: ")
    city = input("City: ")
    postal_code = input("Postal Code: ")
    country = input("Country: ")

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


# Generate the vCard data
data = get_vcard_data()

# Create the QR code
img = qrcode.make(data)
img.save("vCardQR.png")

print("vCard QR code generated and saved as 'vCardQR.png'.")
