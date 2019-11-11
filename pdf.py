import pandas as pd
from functions import chooseGenre
from functions import showMovie
from fpdf import FPDF

def start(genre):
    print("Looking for "+genre+" movie!\n")
    selectedGenre = chooseGenre(genre)
    print("I have a movie for you: -->"+selectedGenre+ "<-- It's my choice")
    return showMovie(selectedGenre)

moviereport = start('Drama')
print (moviereport)

def create_pdf(moviereport):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 16)
    pdf.multi_cell(0, 10, 'Here is your movie recommendation', align='C')
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 8)
    pdf.cell(50, 10, 'Title', align='C', border = 1)
    pdf.cell(50, 10, 'Original Title', align='C', border = 1)
    pdf.cell(30, 10, 'Release Date', align='C', border = 1)
    pdf.cell(25, 10, 'Runtime', align='C', border = 1)
    pdf.cell(35, 10, 'Vote Average', align='C', border = 1)
    
    pdf.ln(10)
    pdf.set_font('times', '', 10)

    Title = moviereport['title'].iloc[0]
    OriginalTitle = moviereport['original_title'].iloc[0]
    ReleaseDate = str(moviereport['release_date'].iloc[0])
    Runtime = str(moviereport['runtime'].iloc[0])
    VoteAverage = str(moviereport['vote_average'].iloc[0])
    Overview = str(moviereport['overview'].iloc[0])

    pdf.cell(50, 10, '%s' % (Title), align='C', border = 1)
    pdf.cell(50, 10, '%s' % (OriginalTitle), align='C', border = 1)
    pdf.cell(30, 10, '%s' % (ReleaseDate), align='C', border = 1)
    pdf.cell(25, 10, '%s' % (Runtime), align='C', border = 1)
    pdf.cell(35, 10, '%s' % (VoteAverage), align='C', border = 1)
    pdf.set_font('arial', '', 20)
    pdf.ln(10)
    pdf.cell(0, 10, 'Overview', align='C', border = 1)
    pdf.ln(10)
    pdf.multi_cell(0, 10, '%s' % (Overview), align='C', border = 1)

    pdf.output('pruebo.pdf', 'F')

create_pdf(moviereport)