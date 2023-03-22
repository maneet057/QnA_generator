import easyocr
from tempfile import TemporaryDirectory
from pathlib import Path
from pdf2image import convert_from_path
from PIL import Image

def extractTextFromPdf(file_path):
    text = ""

    # with open(file_path, 'rb') as file:
    #     reader = PyPDF2.PdfReader(file)
    #     for i in range(len(reader.pages)):
    #         page = reader.pages[i]
    #         text = text + page.extract_text()
    #         print(text)
    # return text
    image_file_list = []
    with TemporaryDirectory() as tempdir:
        pdf_pages = convert_from_path(file_path, 500)
        for page_enumeration, page in enumerate(pdf_pages, start=1):
            filename = f"{tempdir}\page_{page_enumeration:03}.jpg"
            page.save(filename, "JPEG")
            image_file_list.append(filename)

        for image_file in image_file_list:
            img = Image.open(image_file)
            text = text + extractTextFromImg(img)
    # print(text)
    return text
    


def extractTextFromImg(file_path):
    reader = easyocr.Reader(['en'], gpu=True)
    result = reader.readtext(file_path)

    textExtracted = ""

    for (bbox, text, prob) in result:
        textExtracted = textExtracted + " " + text
    print(text)
    return textExtracted
