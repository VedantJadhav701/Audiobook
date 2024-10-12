# Importing necessary libraries
from gtts import gTTS
import PyPDF2
import re


# Open the PDF file
pdf_File = open(r"C:\Users\HP\Downloads\Python_Future_Prospects.pdf", 'rb')

# Create a PDF Reader Object
pdf_Reader = PyPDF2.PdfReader(pdf_File)
count = len(pdf_Reader.pages)  # Get the number of pages in the PDF
textList = []

# Extract text data from each page of the pdf file
for i in range(count):
   try:
       page = pdf_Reader.pages[i]
       textList.append(page.extract_text())
   except:
       pass

# Converting multiline text to single line text
textString = " ".join(textList)

# Clean the text by removing non-alphabetical characters and excess whitespace
cleaned_text = re.sub(r'[^A-Za-z0-9\s]+', '', textString)  # Remove special characters
cleaned_text = re.sub(r'\s+', ' ', cleaned_text)  # Remove extra whitespaces

print(cleaned_text)  # For debugging, check the cleaned text output

# Set language to English (en)
language = 'en'

# Call GTTS (Text-to-Speech) with the cleaned text
myAudio = gTTS(text=cleaned_text, lang=language, slow=False)

# Save the output as an mp3 file
myAudio.save("audio.mp3")
