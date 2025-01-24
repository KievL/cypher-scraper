# Cypher Scraper
---
A web scraping program to collect project announcements.

It is divided into two main modules: *Search Module* and *Interpreter Module*

## Search Module

### What is it?

The *Search Module* consists in the part of the application responsible for searching and gathering target websites.

### How it works

Following predefined parameters, the module will search for and gather websites. All websites matching the desired content will be saved in an output CSV file.

## Interpreter Module

### What is it?

The *Interpreter Module* consists in extracting the content (html page and documents) from the websites gathered by the _Search module_.

### How it works

For each website gathered, information like date, prize money and summary are extracted using a NLP model. The results are appended in a CSV file.
