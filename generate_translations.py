import json
import os


"""
   1.Function to filter data by language and split(filter_data)
   2.Function to write data to JSON file(write_json)
   3.Inside the main function
   4.Replace with the path to your data directory
   5.Initialize a dictionary to store translations
   6.In the for loop,Iterate through all JSONL files in the data directory
   7.Open and read the JSONL file
   8.Filter the data for the "train" sets and English (en-US)
   9.Extract id and utt and store in the translations dictionary
   10.Write the translations to the output JSON file and pretty print
   11.Generate a translations.json file
   12.Run on terminal python generate_translations.py
   """

"""Function to filter data by language and split"""
def filter_data(data, language, split):
    return [item for item in data if item["locale"] == language and item["partition"] == split]


"""Function to write data to JSON file"""
def write_json(data, output_filename):
    with open(output_filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    data_dir = "data"  """Replace with the path to your data directory"""
    output_filename = "translations.json"

    """Initialize a dictionary to store translations"""
    translations = {"en": []}

    """Iterate through all JSONL files in the data directory"""
    for filename in os.listdir(data_dir):
        if filename.endswith(".jsonl"):
            file_path = os.path.join(data_dir, filename)

            """Open and read the JSONL file"""
            with open(file_path, "r", encoding="utf-8") as file:
                jsonl_data = [json.loads(line) for line in file.readlines()]

            """Filter the data for the "train" sets and English (en-US)"""
            filtered_data = filter_data(jsonl_data, "en-US", "train")

            """Extract id and utt and store in the translations dictionary"""
            translations["en"].extend([{"id": item["id"], "utt": item["utt"]} for item in filtered_data])

    """Write the translations to the output JSON file and pretty print"""
    write_json(translations, output_filename)


if __name__ == "__main__":
    main()

"""python generate_translations.py"""