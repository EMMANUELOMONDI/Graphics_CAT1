# CGCATO1
- QUESTION 1 - Python3 Development Environment					         10 Marks

 Set up a new Python3 Development environment for this assessment. Install all the dependencies that you think will be relevant. 

 Build a Python3 project with the structure of projects in PyCharm then import the MASSIVE Dataset mentioned on the Data File above. 

 In this dataset, the pivot language is English, given that all the ids of the languages are matching, generate a en-xx.xlxs file for all the languages. In this question use the id, utt and the annot_utt.  Do not use Recursive algorithms in this solution as they have a time complexity of O(n2), which is bad for memory. 

 Have a look at Flags to help you run this on your generator.sh file

 - SOLUTION
The first solution was implemented using flag. It was executed using the generate_xlsx.py script which is run using the( python generate_xlsx.py --input-dir data --output-dir output_flag)command on the terminal

The --input-dir points to the directory with our dataset containing JSONL files, the --output-dir points to the directory where Excel files will be saved

