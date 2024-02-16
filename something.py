import streamlit as st

from PIL import Image

def combine_images(background, overlay):
    # Resize the overlay image to a smaller size (adjust as needed)
    overlay = overlay.resize((100,150))

    # Calculate the position to center the overlay on the background
    x_position = (background.width - overlay.width) // 2
    y_position = (background.height - overlay.height) // 3

    # Create a copy of the background image
    combined_image = background.copy()



    # Paste the overlay on top of the background with the mask
    combined_image.paste(overlay, (x_position, y_position))

    return combined_image

st.markdown("<h1 style='color: pink; background-color: brown; text-align: center; font-size:40px; font-family: 'Helvetica', sans-serif;'>UPLOAD YOUR IMAGE TO CUSTOMIZE THIS T-SHIRT</h1>", unsafe_allow_html=True)
# Predefined image (replace with your own image path)
predefined_image_path = "Imagess/Isolated_black_t-shirt_front_prev_ui.png"
predefined_image = Image.open(predefined_image_path)

# Display the predefined image
st.image(predefined_image, caption="Predefined Image", use_column_width=True)

uploaded_logo = st.file_uploader("Choose your image", type=["png", "jpg", "jpeg"])
if uploaded_logo is not None:
        st.success("Image successfully uploaded!")

        # Display the uploaded logo on top of the predefined image
        combined_image = combine_images(predefined_image, Image.open(uploaded_logo))
        st.image(combined_image, caption="Combined Image", use_column_width=True)







