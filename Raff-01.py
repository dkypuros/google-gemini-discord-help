import pathlib
import textwrap
from dotenv import load_dotenv
import google.generativeai as genai  # Assuming the correct name of the package
import PIL
import io
import os

# Load environment variables from .env file
load_dotenv()
print("Environment variables loaded.")

def to_markdown(text):
    # Since we're running in a terminal, we'll return plain text instead of Markdown
    text = text.replace('.', ' *')
    return textwrap.indent(text, ' ')

# Use the loaded environment variable
api_ku = os.getenv('geminiai')
if api_ku:
    print("API key found.")
else:
    print("API key not found. Please check your .env file.")

# Configure the API with the key
genai.configure(api_key=api_ku)
print("AI configuration set.")

# Initialize the model
model = genai.GenerativeModel('gemini-pro-vision')
print("Generative model loaded.")

# Set the file name of your image
file_name = 'me.jpg'  # Make sure this image is in the current directory.
try:
    img = PIL.Image.open(file_name)
    print(f"Image {file_name} loaded successfully.")
except FileNotFoundError:
    print(f"Image {file_name} not found. Please check the file path.")
except Exception as e:
    print(f"An error occurred while loading the image: {e}")

# Generate the content based on the image
try:
    print("Generating content...")
    response = model.generate_content(['What color is the shirt in the image', img], stream=True)
    response.resolve()
    print("Content generated.")
except Exception as e:
    print(f"An error occurred while generating content: {e}")

# Process and print the response
try:
    markdown_text = to_markdown(response.text)
    print("Markdown text created.")
    print(markdown_text)  # Print the response as plain text
except Exception as e:
    print(f"An error occurred while creating markdown text: {e}")
