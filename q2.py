from PIL import Image
import pytesseract

print(pytesseract.image_to_string(Image.open(r"C:\Users\aades\OneDrive\Desktop\internship\t.png")))
