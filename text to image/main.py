import base64
from io import BytesIO
from PIL import Image

# Read the encoded string from the text file
with open("image to text/encoded_image.txt", "r") as file:
    encoded_string = file.read()

# Decode the string
decoded_string = base64.b64decode(encoded_string)

# Create an image object from the decoded bytes
image = Image.open(BytesIO(decoded_string))

# Display or save the image
image.show()
