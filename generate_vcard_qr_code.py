import qrcode

# QR Code settings
QR_VERSION = 1
QR_ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_L
QR_BOX_SIZE = 10
QR_BORDER = 4

class ValidationError(Exception):
    pass

def get_vcard_data():
    print("Please enter the following information for the vCard:")
    
    # Input collection with basic validation
    try:
        first_name = input("First Name: ").strip()
        last_name = input("Last Name: ").strip()
        organization = input("Organization: ").strip()

        # Ensure required fields are not empty
        if not (first_name and last_name and organization):
            raise ValidationError("Error: First Name, Last Name, and Organization are required fields.")

        email = input("Email (optional): ").strip()
        phone = input("Phone (optional): ").strip()
        street = input("Street + number (optional): ").strip()
        city = input("City (optional): ").strip()
        postal_code = input("Postal Code (optional): ").strip()
        country = input("Country (optional): ").strip()
        url = input("URL (optional): ").strip()

        # Construct vCard data
        vcard_data = f"""BEGIN:VCARD
VERSION:3.0
N:{last_name};{first_name}
FN:{first_name} {last_name}
ORG:{organization}\n"""
        
        if email:
            vcard_data += f"EMAIL;TYPE=work:{email}\n"
        if phone:
            vcard_data += f"TEL;TYPE=work:{phone}\n"
        if street or city or postal_code or country:
            vcard_data += f"ADR;TYPE=intl,work,postal,parcel:;;{street};{city};;{postal_code};{country}\n"
        if url:
            vcard_data += f"URL:{url}\n"

        vcard_data += "END:VCARD"

        return vcard_data

    except ValidationError as ve:
        print(str(ve))
        return None

def generate_qr_code(data):
    try:
        # Create the QR code with defined settings
        qr = qrcode.QRCode(
            version=QR_VERSION,
            error_correction=QR_ERROR_CORRECTION,
            box_size=QR_BOX_SIZE,
            border=QR_BORDER,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("vCardQR.png")
        print("vCard QR code generated and saved as 'vCardQR.png'.")
    except Exception as e:
        print(f"Error generating QR code: {e}")

if __name__ == "__main__":
    try:
        # Generate the vCard data
        data = get_vcard_data()

        if data:
            # Create the QR code
            generate_qr_code(data)

    except Exception as e:
        print(f"Error: {e}")
