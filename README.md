# CGCATO1
- QUESTION 1 - Python3 Development Environment					         10 Marks

 Set up a new Python3 Development environment for this assessment. Install all the dependencies that you think will be relevant. 

 Build a Python3 project with the structure of projects in PyCharm then import the MASSIVE Dataset mentioned on the Data File above. 

 In this dataset, the pivot language is English, given that all the ids of the languages are matching, generate a en-xx.xlxs file for all the languages. In this question use the id, utt and the annot_utt.  Do not use Recursive algorithms in this solution as they have a time complexity of O(n2), which is bad for memory. 

 Have a look at Flags to help you run this on your generator.sh file

 - SOLUTION
   
The first solution was implemented using flag. It was executed using the generate_xlsx.py script which is run using the( python generate_xlsx.py --input-dir data --output-dir output_flag)command on the terminal

The --input-dir points to the directory with our dataset containing JSONL files, the --output-dir points to the directory where Excel files will be saved

- QUESTION 2 - Working with Files							         10 Marks
  
For English (en), Swahili (sw) and German (de), generate separate jsonl files with test, train and dev respectively. 

- SOLUTION

The second solution was implemented using flags. It was executed using the generate_jsonl_splits.py script which is run using the(python generate_jsonl_splits.py --data-dir data --output-dir output_split) command on the terminal

The --data-dir points to the directory where our data is located , the --outout-dir points to the directory where the outputs will be saved in the output_split folder

- QUESTION 3 - Generate one large json file showing all the translations from en to xx with id and utt for all the train sets.
  
- a ) Pretty print your json file structure.

- SOLUTION

- The third solution was implemented in the generate_transactions.py script which is run using the (python generate_translations.py). On running this it outputs a file named translations.json which shows all the transactions from en to xx with id and utt for all the train sets.
