import easyocr
import os

def extract_text_easyocr(image_path):
    if not os.path.exists(image_path):
        return f"Error: The file '{image_path}' does not exist."

    try:
        reader = easyocr.Reader(['en'])  # Initialize EasyOCR reader for English
        results = reader.readtext(image_path)
        if not results:
            return "No text detected in the image."
        
        # Join all detected text parts into a single string
        extracted_text = " ".join([text for _, text, _ in results])
        return extracted_text
    
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    path = input("Please enter the full path to the image: ").strip()
    text = extract_text_easyocr(path)
    print("\n--- Extracted Text ---")
    print(text)
