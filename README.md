
# Computer Graphics_CAT1 GROUP 7
## About 
This is a python project with the intention of manipulating data from a massive dataset and also to work with files to carry out tasks assigned. 
## Technologies used
- Pyhton
- Python 3 
- Pyhton libraries e.g pandas ,numpy ,openxyl

## Tasks 
1. Build a Python3 project with the structure of projects in PyCharm then import the MASSIVE Dataset mentioned on the Data File above. 
In this dataset, the pivot language is English, given that all the ids of the languages are matching, generate a en-xx.xlxs file for all the languages.
1. For English (en), Swahili (sw) and German (de), generate separate jsonl files with test, train and dev respectively. 
1. Generate one large json file showing all the translations from en to xx with id and utt for all the train set
1. Upload all the files to your Google Drive Backup Folder. 

Upload all the files to your Google Drive Backup Folder. 

## Python files
- `main.py`
- `generate_xlsx.py`- It has the functions to convert JSONL to a dataframe
- `generate_jsonl_splits.py`- Function to write data to JSONL file
- `generate_translations.py`- Function to filter data by language and split 

## Dependencies Used
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
