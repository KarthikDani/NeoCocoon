import fitz  # PyMuPDF
import numpy as np
from fpdf import FPDF  # To create the output PDF
from datetime import datetime

def extract_purple_highlighted_text(pdf_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    highlighted_sentences_by_page = {}

    # Iterate through each page
    for page_num, page in enumerate(doc, start=1):
        print(f"\n[DEBUG] Processing Page {page_num}")

        # Extract the full text of the page
        words = page.get_text("words")  # Get words with their bounding boxes
        words.sort(key=lambda w: (w[1], w[0]))  # Sort by vertical position, then horizontal

        sentence = []
        last_y = None

        # Iterate through words to detect purple highlights
        for word in words:
            bbox = fitz.Rect(word[:4])  # The bounding box of the word
            # print(f"[DEBUG] Word: '{word[4]}' | Bounding Box: {bbox}")

            pixmap = page.get_pixmap(clip=bbox)  # Extract pixmap of the word area

            # Compute the average color in the region
            avg_color = get_average_color(pixmap)
            # print(f"[DEBUG] Average Color (RGB): {avg_color}")

            if is_purple_highlight(avg_color):
                if last_y is None or abs(last_y - word[1]) < 5:
                    sentence.append(word[4])  # Append word to the sentence
                else:
                    # Store the previous sentence with page number
                    if page_num not in highlighted_sentences_by_page:
                        highlighted_sentences_by_page[page_num] = []
                    highlighted_sentences_by_page[page_num].append(" ".join(sentence))
                    sentence = [word[4]]  # Start a new sentence
                last_y = word[1]  # Update last y-coordinate

        # Store the last sentence of the page
        if sentence:
            if page_num not in highlighted_sentences_by_page:
                highlighted_sentences_by_page[page_num] = []
            to_append = " ".join(sentence)
            highlighted_sentences_by_page[page_num].append(to_append)
            print(f"[HIGHLIGHTED Page {page_num}] {to_append}")

    print(f"\n[DEBUG] Total highlighted sentences found: {sum(len(sentences) for sentences in highlighted_sentences_by_page.values())}")
    return highlighted_sentences_by_page

def get_average_color(pixmap):
    # Convert pixmap to a numpy array
    img = np.frombuffer(pixmap.samples, dtype=np.uint8).reshape(pixmap.height, pixmap.width, pixmap.n)
    # Calculate the average color (RGB) across all pixels
    avg_color = img.mean(axis=(0, 1))[:3]  # Only take RGB channels, ignore alpha if present
    return avg_color

def is_purple_highlight(color):
    # Define a threshold for purple highlight colors
    r, g, b = color
    # Purple typically has high red and blue values with lower green
    return r > 200 and b < 200 and g < 200

def save_highlighted_text_to_pdf(highlighted_sentences_by_page, output_pdf_path, title, author_name, doi=None):
    # Create a PDF document to store the highlighted sentences
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.set_auto_page_break(auto=True, margin=10)
    pdf.add_page()

    # Set title and metadata
    pdf.set_font("Times", "B", 20)
    pdf.cell(0, 10, title, align="C")
    pdf.ln(5)  # Add some space

    # Add optional DOI link at the bottom
    if doi:
        pdf.set_font("Times", "I", 12)
        pdf.cell(0, 10, f"DOI: {doi}", align="C")
        pdf.ln(5)  # Add some space

    # Add date below title
    pdf.set_font("Times", "I", 12)
    current_date = datetime.now().strftime("%B %d, %Y")
    pdf.cell(0, 10, current_date, align="C")
    pdf.ln(5)  # Add some space

    # Add author name
    pdf.set_font("Times", "I", 12)
    pdf.cell(0, 10, f"Author: {author_name}", align="C")
    pdf.ln(10)  # Add some space before content

    # Add highlighted text content by page
    pdf.set_font("Times", size=12)
    for page_num, sentences in highlighted_sentences_by_page.items():
        pdf.set_font("Times", "B", 14)
        pdf.cell(0, 10, f"Page {page_num}:", align="L")
        pdf.ln(5)  # Add space before sentences
        pdf.set_font("Times", size=12)

        for sentence in sentences:
            # Replace smart quotes and other problematic characters
            clean_sentence = sentence.replace("‘", "'").replace("’", "'")
            pdf.multi_cell(0, 10, clean_sentence)
            pdf.ln(2)  # Add some space between entries

    pdf.output(output_pdf_path)

# Usage example:
pdf_file = "/Users/karthik/Desktop/Infant Incubator/Literature/AK-Health-19SP-FinalReport_HIGHLIGHTED.pdf"
output_pdf = "/Users/karthik/Desktop/Infant Incubator/Notes Extractor/highlighted_sentences.pdf"
title = "Highlighted Notes from Research Paper"
author_name = "Karthik Dani"
doi_link = "https://doi.org/10.1234/example"  # Optional

highlighted_sentences_by_page = extract_purple_highlighted_text(pdf_file)
save_highlighted_text_to_pdf(highlighted_sentences_by_page, output_pdf, title, author_name, doi=doi_link)

print(f"Highlighted text saved to {output_pdf}")
