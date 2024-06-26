# Robocorp RPA - News Data Extraction

## Description

This project aims to automate the process of extracting data from a news website, specifically Al Jazeera. The robot is capable of searching for news based on a search phrase, news category, and specific period, storing the results in an Excel file.

## Challenges

- Automate data extraction from the Al Jazeera news website.
- Process three parameters via Robocloud work item:
  - `search_phrase`: search term.
  - `news_category`: news category/section/topic.
  - `months`: number of months of news to retrieve.
- Store the results in an Excel file, including information such as title, date, description, image filename, count of search terms in the title and description, and an indicator of the presence of monetary values.

## Project Structure

```plaintext
├── tasks/
│   └── main.py         # Main robot script
├── resources/
│   └── config.yaml     # Configuration file (optional)
├── output/             # Folder to store results
├── conda.yaml          # Dependency configuration file
└── README.md           # This file
