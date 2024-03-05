import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

def create_qr_code(url, save_path, title,save_path2):
    # Create instance of QRCode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=5,
    )

    # Add data to the QRCode instance
    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QRCode instance
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(save_path)

    titled_img = Image.open(save_path)
    img = img.convert('RGB')
    draw = ImageDraw.Draw(titled_img)
    my_font = ImageFont.truetype('TitilliumWeb-SemiBold.ttf', 50)
    text_width, text_height = draw.textsize(title, font=my_font)
    image_width, image_height = titled_img.size
    x = (image_width - text_width) // 2
    y =image_height - 90
    print("image height: ", image_height)

    print(x, y)
    draw.text((x, y), title, font=my_font)
    # Save the image
    titled_img.save(save_path2)

    # delete the image without a title
    try:
        os.remove(save_path)
    except OSError as e:
        print(f"Error deleting file {save_path}: {e}")


links = {"something":"https://forms.gle/TMmugZ6oZPAumVJm8",
         "somethingw":"https://forms.gle/TMmugZ6oZPAumVJm8"}

for key, value in links.items():
    # Example usage-----------------------------------------
    url = value
    title = key
    save_path = f"C:/Users/asoom/Desktop/Programing/QR-CODE-maker-main/images/{key}.png"
    save_path2 = f"C:/Users/asoom/Desktop/Programing/QR-CODE-maker-main/images/{key}2.png"
    create_qr_code(url, save_path, title,save_path2)
    print(f"QR code generated and saved to {save_path}")