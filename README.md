# Startups Analysis

This project is a combination of Web scraping and Data analysis.

## Pre-Requisites:
* Python 3.x
* Pandas
* Plotly
* Beautiful Soup

## Installing packages
```python
pip install -r requirements.txt
```
If you have both python2 and python3 installed:
```python
pip3 install -r requirements.txt
```

## How it works
1. data.py has the python script to scrape the data from The Technology Headlines - 100 Startups (Page allowed to be scraped for robots -- check its '/robots.txt')
2. The scraped data is stored as tth.csv file
3. analyse.py uses pandas and plotly to analyse the data and visualize the insights.
4. The number of startups founded in years between 2000 and 2018 is analysed along with the number of companies in different industries.
5. tth\_pie\_chart and tth\_bar\_chart are the output visualizations of the analysis results.
