import qrcode
from PIL import Image, ImageDraw, ImageFont
import os
import streamlit as st
from streamlit_extras import add_vertical_space as avs

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

def generate(links):

    for key, value in links.items():
        # Example usage-----------------------------------------
        url = value
        title = key
        save_path = f"{key}.png"
        save_path2 = f"images/{key}2.png"
        create_qr_code(url, save_path, title,save_path2)


def streamlit_api():
    st.set_page_config(page_title='PC | QR-Code', layout='centered')
    
    # TITLES AND HEADERS
    st.title("QR-code Maker")
    st.markdown('> **Free!**')
    st.markdown('> **Fast!**')
    st.markdown('> **Imortal!**')
    st.markdown('---')

    avs.add_vertical_space(2)
    num = st.number_input("How many codes you want to generate? ", step=1, min_value=1, max_value=10)
    st.caption("**Fields with missing name or link will not be generated.")
    links = {}
    avs.add_vertical_space(2)
    c1, c2 = st.columns(2, gap='large')

    for i in range(num):
        with c1:
            name = st.text_input("Enter name" , key=i)
        with c2:
            l = st.text_input("Enter link",key='linkK'+str(i))

        links[name] = l

    links_cleaned = links.copy()

    for k,v in links.items():
        if k == '' or v == '':
            del links_cleaned[k]

    avs.add_vertical_space(2)

        
    if st.button('GENERATE', use_container_width=True):
        if len(links_cleaned) > 0:
            generate(links_cleaned)
            for i in links_cleaned.keys():
                st.image(f'images/{k}2.png')
                st.download_button(f"Save {k}.png Code", data='PNG', use_container_width=True, file_name=f'images/{k}2.png')
                avs.add_vertical_space(1)

        else:
            st.warning("Data Missing.. make sure to add the name/link correctly.")


streamlit_api()