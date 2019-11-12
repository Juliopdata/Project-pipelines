# <p align="center"> Project Pipelines</p>


  <p align="center"> <img  src="https://github.com/Juliopdata/project-pipelines/blob/master/images/tomate.png"></p>


<p align="center">Choose a movie genre, get a top recommendation</p>


---

## Overview

The goal of this project is for me to practice what I have learned in the Intermediate Python and Data Engineering chapter of the Ironhack program. For this project, I start with [The Movies Dataset](https://www.kaggle.com/rounakbanik/the-movies-dataset) and web scraping [Rotten Tomatos Top Movies](https://www.rottentomatoes.com/top/). I import it and use my newly-acquired skills to build a data pipeline that processes the data and produces a report that can be sent to a given email. I try demonstrate my proficiency with the tools we covered (functions, list comprehensions, string operations and web scraping) in my pipeline.

---

## Project Structure

The project folder is structured in the following way:

* __main.py__ : that contains the code of my data pipeline.

* __INPUT__ : Folder where the dataset should be placed in csv format.

* __OUTPUT__ : Folder that contains the cleaned datasets and the output of my data pipeline.

* __SRC__: Images and resources.

### 1 - Clean and Analysis

1. I acquire the data from the dataset CSV and the web scrapping.
2. Clean the data and generate 2 new datasets to work with it

### 2 - Data Processing

1. Create the functions explore the datasets with the parameters given.
2. Returns movie recommendations according to the parameters and metadata from the films.
3. Generates a PDF document with all the info of the movie.
4. Sends the PDF attached to a email address given.

### 3 - Start the Query

1. Run the __main.py__ file and work with the 2 parameters, 'Genre' and 'Email.
2. You can choose one of this genres: comedy, romance, drama, horror or thriller.
2. Shows the movie recommendation and shows you when the report and email has been sent.

To run the program the user needs to introduce two arguments:
- A genre: comedy, romance, drama, horror or thriller
- A valid email

>Example: *Python3 main.py horror youremail@mail.com* or *./main.py horror youremail@mail.com*
