import base64

# Read image file
with open("earth.jpg", "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode("utf-8")

# Save the encoded string in a text file
with open("encoded_image.txt", "w") as file:
    file.write(encoded_string)

print("Encoded string saved in 'encoded_image.txt'.")
