import pytesseract
import re 
from PIL import Image

class ImageProcessor:

    @staticmethod
    def extract_text_from_image(file):
        """
        Extracts text from the provided image file.

        Parameters:
            file (str): The path to the image file.

        Returns:
            str: The extracted text from the image.
        """
        with Image.open(file) as image:
            if image.mode != "RGB":
                image = image.convert("RGB")
            extracted_text = pytesseract.image_to_string(image)
        return extracted_text
    
    @staticmethod
    def extract_ingredients(text):
        """
        Extracts a list of ingredients from the provided text.

        Parameters:
            text (str): The text containing the ingredient list.

        Returns:
            list : A list of ingredients extracted from the text,
                         or none.
        """
        # Regular expression pattern to extract ingredients
        pattern = r'(?i)\bINGREDIENTS?:?\s*([^.,\n]+(?:[.,]\s*[^.,\n]+)*)'

        # Extract ingredients using regular expression
        matches = re.findall(pattern, text, re.DOTALL | re.IGNORECASE)

        if matches:
            # Strip whitespace and join matches into a single string
            ingredients = ", ".join(matches).strip()
            # Split the string into a list
            ingredient_list = [ingredient.strip() for ingredient in ingredients.split(',')]
            return ingredient_list
        else:
            return None
