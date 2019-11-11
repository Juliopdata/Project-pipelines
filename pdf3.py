import pandas as pd
from functions import chooseGenre
from functions import showMovie
from fpdf import FPDF

def start(genre):
    print("Looking for "+genre+" movie!\n")
    selectedGenre = chooseGenre(genre)
    print("I have a movie for you: -->"+selectedGenre+ "<-- It's my choice")
    moviereport = showMovie(selectedGenre)
    return moviereport
moviereport = start('Drama')
print (moviereport)
def createPDF(moviereport):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(0, 10, 'Movie Recommendation', align='C')
    pdf.ln(10)
    pdf.set_font('Arial', '', 12)
    text="No sé que es esto."

    pdf.multi_cell(0, 5, text.format(moviereport.genres,moviereport.original_language,moviereport.original_title,moviereport.release_date,moviereport.runtime,moviereport.vote_average),align='L')
    pdf.ln(10)
    pdf.output('pruebo.pdf', 'F')

createPDF(moviereport)