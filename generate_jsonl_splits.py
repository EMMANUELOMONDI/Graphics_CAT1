import os
import json
import argparse


def filter_data(data, partition):
    """
    Function to filter data by locale and partition
    """
    return [item for item in data if item["partition"] == partition]


def write_jsonl(data, output_filename):
    """
    Function to write data to JSONL file
    """
    with open(output_filename, "w", encoding="utf-8") as file:
        for item in data:
            json.dump(item, file, ensure_ascii=False)
            file.write("\n")


def main():
    """
    Define the Arguments
    Create the output directory if it doesn't exist
    Filter the data based on the "partition" key
    Write data to the output JSONL file
    """
    parser = argparse.ArgumentParser(description="Generate separate JSONL files for multiple locales and data splits.")
    parser.add_argument("--data-dir", required=True, help="Directory containing JSONL files")
    parser.add_argument("--output-dir", required=True, help="Directory where JSONL files will be saved")

    args = parser.parse_args()

    data_dir = args.data_dir
    output_dir = args.output_dir

    os.makedirs(output_dir, exist_ok=True)

    locales = ["en-US", "sw-KE", "de-DE"]
    partitions = ["train", "test", "dev"]

    for locale in locales:
        input_filename = os.path.join(data_dir, f"{locale}.jsonl")
        output_base_filename = os.path.join(output_dir, locale)

        if os.path.exists(input_filename):
            with open(input_filename, "r", encoding="utf-8") as file:
                jsonl_data = [json.loads(line) for line in file.readlines()]

            for partition in partitions:
                filtered_data = filter_data(jsonl_data, partition)
                output_filename = f"{output_base_filename}-{partition}.jsonl"

                write_jsonl(filtered_data, output_filename)


if __name__ == "__main__":
    main()

# python generate_jsonl_splits.py --data-dir data --output-dir output_split
