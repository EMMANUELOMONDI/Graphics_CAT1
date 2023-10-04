
# Computer Graphics CAT1 GROUP 7
## About 
This is a Python project with the intention of manipulating data from a massive dataset and also working with files to carry out tasks assigned. 
## Technologies used
- Python
- Python 3 
- Python libraries e.g. pandas, numpy, openxyl

## Tasks 
1. Build a Python3 project with the structure of projects in PyCharm then import the MASSIVE Dataset mentioned in the Data File above. 
In this dataset, the pivot language is English, given that all the ids of the languages are matching, generating an en-xx.xlxs file for all the languages.
1. For English (en), Swahili (sw), and German (de), generate separate JSONL files with test, train, and dev respectively. 
1. Generate one large JSON file showing all the translations from en to xx with id and utt for all the train set
1. Upload all the files to your Google Drive Backup Folder. 

Upload all the files to your Google Drive Backup Folder. 

## Python files
- `main.py`
- `generate_xlsx.py`- It includes the functions to convert JSONL to a data frame
- `generate_jsonl_splits.py`- Function to write data to JSONL file
- `generate_translations.py`- Function to filter data by language and split 

## Dependencies
- `os`: module provides a way of using operating system-dependent functionality, such as working with files and directories 
- `json`:module is used for working with JSON (JavaScript Object Notation) data
- `openpyxl`: for reading and writing Excel (XLSX) files.
- `pandas`:data manipulation library in Python
- `argparse`: module is used for parsing command-line arguments in Python scripts.

## Usage

## Authors
1. 145182 - Omondi Emmanuel
1. 145369 - Wango Michael
1. 144915 - Mahia Jerome
1. 94230 - Nathan Njonge
1. 146202 - Mugambi Rintaugu
