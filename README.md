<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

# Manipulating the MASSIVE Dataset using Python

## Quick Links

- [Introduction](https://github.com/EMMANUELOMONDI/Graphics_CAT1#introduction)

- [Tasks](https://github.com/EMMANUELOMONDI/Graphics_CAT1#tasks)

- [File structure](https://github.com/EMMANUELOMONDI/Graphics_CAT1#file-structure)

- [Project installation](https://github.com/EMMANUELOMONDI/Graphics_CAT1#project-installation)

- [Running the project](https://github.com/EMMANUELOMONDI/Graphics_CAT1#running-the-project)

- [Disclaimer](https://github.com/EMMANUELOMONDI/Graphics_CAT1#disclaimer)

- [Output files](https://github.com/EMMANUELOMONDI/Graphics_CAT1#output-files)

- [Authors](https://github.com/EMMANUELOMONDI/Graphics_CAT1#authors)

## Introduction

This repository contains code that makes use of the MASSIVE dataset by amazon using python. MASSIVE is a parallel dataset of more than 1 million utterances across 52 languages with annotations for the Natural Language Understanding tasks of intent prediction and slot annotation. Utterances span 60 intents and include 55 slot types.

In this project, the dataset's files, which originally come in the .jsonl format, are converted to excel readable .xlsx files. The data from the dataset is also manipulated to generate new .jsonl files and to generate a large .json file showing some translations for utterances made as part of the train partition.

You can read more about the dataset [here](https://github.com/alexa/massive#readme).

## Tasks 
1. Build a Python3 project with the structure of projects in PyCharm then import the MASSIVE Dataset mentioned in the Data File above. 
In this dataset, the pivot language is English, given that all the ids of the languages are matching, generating an en-xx.xlxs file for all the languages.
2. For English (en), Swahili (sw), and German (de), generate separate JSONL files with test, train, and dev respectively. 
3. Generate one large JSON file showing all the translations from en to xx with id and utt for all the train set
4. Upload all the files to your Google Drive Backup Folder. 

## File structure
- `main.py`
- `generate_xlsx.py`- It has the functions to convert JSONL to a data frame
- `generate_jsonl_splits.py`- Function to write data to JSONL file
- `generate_translations.py`- Function to filter data by language and split
  
## Project installation

1. Open your terminal and create a virtual python environment to store all the required dependencies to run this project. The project was created using python version 3.11.5 which can be installed automatically when working with anaconda environments or can be downloaded directly from [here](https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe).

   If you prefer to use python's venv facility:

   ```
   python3 -m venv environment_name
   ```

   You can read more on working with python and pip [here](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

   If you prefer to use anaconda:

   ```
   conda create -n environment_name
   ```

   You can read more on working with anaconda [here](https://docs.anaconda.com/free/navigator/tutorials/index.html).

   You can use pip to install all the project's dependencies into your environment:

   ```
   pip install -r requirements.txt
   ```

2. Fork and clone this repository.

   Run the following command in your terminal to clone the forked repository:

   ```{code}
   git clone <repository link> <folder name>
   ```

3. Download the massive dataset. The massive data set 1.1 which was used for this project can be downloaded <a href="https://amazon-massive-nlu-dataset.s3.amazonaws.com/amazon-massive-dataset-1.1.tar.gz">here</a>. You will need [WinRar](https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-623.exe) to extract the compressed folder.

4. Retrieve the data folder from the extracted folder and import it into your local repository in the src folder.

   The file hierarchy for this should be something like this:

   ```{code}
   C:\Users\username\my_project\src\data
   ```

5. Install git bash which is usually obtained during git installation. You can begin your download of git from [here](https://git-scm.com/downloads).

## Running the project

Upon completing the project installation steps:

1. Open your git bash terminal and navigate to the project's src folder.

2. Run the following commands to execute the bash file and generate the project's output files.

   To make the bash file executable:

   ```{code}
   chmod +x generator.sh
   ```

   To run the bash file and generate the project's output:

   ```{code}
   ./generator.sh
   ```

## Disclaimer

Due to the large number of files being processed and generated, the process of generating the output could take a few minutes.

## Output files

The project's output files were backed up on Google Drive and can be accessed [here](https://drive.google.com/drive/u/1/my-drive).

## Authors
1. 145182 - Omondi Emmanuel
2. 1455369 - Wango Michael
3. 144915 - Mahia Jerome
4. 94230 - Nathan Njonge
5. 146202 - Mugambi Rintaugu
