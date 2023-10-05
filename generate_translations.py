import json
import os


def filter_data(data, language, split):
    """ Function to filter data by language and split """
    return [item for item in data if item["locale"] == language and item["partition"] == split]


def write_json(data, output_filename):
    """ Function to write data to JSON file """
    with open(output_filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    """
    The function does the following:
    Initialize a dictionary to store translations
    Iterate through all JSONL files in the data directory
    """

    data_dir = "data"  # Path to your data directory
    output_filename = "translations.json"

    translations = {"en": []}

    for filename in os.listdir(data_dir):
        if filename.endswith(".jsonl"):
            file_path = os.path.join(data_dir, filename)

            """
            Open and read the JSONL file
            Filter the data for the "train" sets and English (en-US)
            Extract id and utt and store in the translations dictionary
            """
            with open(file_path, "r", encoding="utf-8") as file:
                jsonl_data = [json.loads(line) for line in file.readlines()]

            filtered_data = filter_data(jsonl_data, "en-US", "train")

            translations["en"].extend([{"id": item["id"], "utt": item["utt"]} for item in filtered_data])

    """
    Write the translations to the output JSON file and pretty print """
    write_json(translations, output_filename)


if __name__ == "__main__":
    main()

# python generate_translations.py
