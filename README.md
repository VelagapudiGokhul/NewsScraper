# NewsScrapper

This project fetches news headlines from various categories and reads them using Python. It utilizes `requests` to fetch the HTML content, `BeautifulSoup` to parse the HTML, and `pyttsx3` for text-to-speech.

## Features

- Fetches news headlines from the following categories:
  - Technology
  - Sports
  - Education
  - Business
  - Political
  - Entertainment
- Reads the headlines
- Prints the headline and the corresponding link

## Web Scraping

The headlines are scraped from the [Indian Express](https://indianexpress.com/) website using `requests` and `BeautifulSoup`. The script fetches the HTML content of the specified section and extracts the headlines along with their links.
![image](https://github.com/user-attachments/assets/34ec5042-458b-4390-b0ed-fe91dd43ca33)



## Requirements

- Python 3.x
- `requests` library
- `beautifulsoup4` library
- `pyttsx3` library

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/NewsScrapper.git

