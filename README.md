# Cypher Scraper
A web scraping program to collect project announcements.

It is divided into two main modules: *Searcher Module* and *Interpreter Module*

## Searcher Module

### What is it?

The *Searcher Module* consists in the part of the application responsible for searching and gathering target websites.

### How it works

Following predefined parameters, the module will search for and gather websites. All websites matching the desired content will be saved in an output CSV file.

This module will use [googlesearch-py](https://pypi.org/project/googlesearch-python/) library. Any better idea can also be tested. The main challenge is to implement multiple queries that can efficiently gather the desired websites.

### Useful links:
- [Performing Google Search using Python code - Geeks 4 Geeks](https://www.geeksforgeeks.org/performing-google-search-using-python-code/)
- [Google Search in Python: A Beginner’s Guide - Medium](https://medium.com/@sagarydv002/google-search-in-python-a-beginners-guide-742472fec9cc)
- [Scrape Google Search Results With Python (2025) - Medium](https://medium.com/@darshankhandelwal12/scrape-google-with-python-2023-86cda73ffb16)

## Interpreter Module

### What is it?

The *Interpreter Module* consists in extracting the content (html page and documents) from the websites gathered by the _Searcher module_.

### How it works

For each website gathered, information like date, prize money and summary are extracted using a NLP model. The results are appended in a CSV file.

Objectives:
- To extract texts searching for them on .pdfs, HTML and drive documents.
- To extract text blocks with datetime and prizemoney information.
- To extract a text block with the main text information.
- To build pipelines in order to extract information of selected blocks using openAI API.

# Project Setup

Here are the steps needed to setup the development environment.

## Requirements

In _requirements.txt_ are the libs used in the project. In order to load them, make sure you're using **Python 3.10.12**. Then, create a virtual venv ([How to Set Up a Virtual Environment in Python](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/)). With virtual env activated, run:
```bash
pip install -r requirements.txt
```

If the installation of any lib is required, you can install it using **pip**. But remember to update the __requirement.txt__ right after:
```bash
pip freeze > requirements.txt
```