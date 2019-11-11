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
    name = data['Name'].iloc[i]
        city = data['City'].iloc[i]
        price = data['Price-Night'].iloc[i]
        distance = data['Distance-km'].iloc[i]
        score = str(data['Score'].iloc[i])
        rating = str(data['Rating'].iloc[i])
        pdf.cell(100, 7, '%s' % (name), align='L', border = 1)
        pdf.cell(10, 7, '%s' % (city), align='C', border = 1)
        pdf.cell(30, 7, '%s' % (price), align='C', border = 1)
        pdf.cell(25, 7, '%s' % (distance), align='C', border = 1)
        pdf.cell(10, 7, '%s' % (score), align='C', border = 1)
        pdf.cell(20, 7, '%s' % (rating), align='C', border = 1)
        pdf.ln(7)

createPDF(moviereport)