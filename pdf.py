import pandas as pd
from functions import chooseGenre
from functions import showMovie
from fpdf import FPDF

def createPDF(moviereport):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('Arial', 'B', 20)
    pdf.multi_cell(0, 10, 'Here Is Your Movie Recommendation', align='C')
    pdf.ln(10)
    pdf.image('./images/tomate.png', 33)
    pdf.ln(10)
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(45, 7, 'Title', align='C', border = 1)
    pdf.cell(45, 7, 'Original Title', align='C', border = 1)
    pdf.cell(20, 7, 'Release', align='C', border = 1)
    pdf.cell(20, 7, 'Runtime', align='C', border = 1)
    pdf.cell(30, 7, 'Rate Average', align='C', border = 1)
    pdf.cell(20, 7, 'Language', align='C', border = 1)
    pdf.ln(7)
    pdf.set_font('times', '', 10)
    title = moviereport['title'].iloc[0]
    original_title = moviereport['original_title'].iloc[0]
    releasedate = moviereport['release_date'].iloc[0]
    runtime = moviereport['runtime'].iloc[0]
    voteaverage = moviereport['vote_average'].iloc[0]
    overview = moviereport['overview'].iloc[0]
    originallanguage = moviereport['original_language'].iloc[0]
    pdf.cell(45, 7, '%s' % (title), align='C', border = 1)
    pdf.cell(45, 7, '%s' % (original_title), align='C', border = 1)
    pdf.cell(20, 7, '%s' % (releasedate), align='C', border = 1)
    pdf.cell(20, 7, '%s' % (runtime), align='C', border = 1)
    pdf.cell(30, 7, '%s' % (voteaverage), align='C', border = 1)
    pdf.cell(20, 7, '%s' % (originallanguage), align='C', border = 1)
    pdf.ln(10)
    pdf.set_font('helvetica', 'B', 10)
    pdf.cell(180, 7, 'Overview', align='C', border = 1)
    pdf.ln(7)
    pdf.set_font('times', '', 10)
    pdf.multi_cell(180, 7, '%s' % (overview), align='C', border = 1)
    pdf.output('./recommendation.pdf', 'F')
    return ['./recommendation.pdf']

