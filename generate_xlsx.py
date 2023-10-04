import os
import json
import argparse
from openpyxl import Workbook
import pandas as pd


# Function to convert JSONL to a DataFrame
def jsonl_to_dataframe(jsonl_data):
    data = [json.loads(line) for line in jsonl_data]
    df = pd.json_normalize(data)
    return df


# Function to generate an Excel file
def generate_excel(language, data, output_dir):
    excel_filename = os.path.join(output_dir, f"en-{language}.xlsx")

    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Data"

    # Add headers to the Excel sheet
    headers = ["id", "utt", "annot_utt"]
    sheet.append(headers)

    # Add data to the Excel sheet
    for _, row in data.iterrows():
        sheet.append([row["id"], row["utt"], row["annot_utt"]])

    # Save the Excel file
    workbook.save(excel_filename)


def main():
    parser = argparse.ArgumentParser(description="Generate Excel files from JSONL data for multiple languages.")
    parser.add_argument("--input-dir", required=True, help="Directory containing JSONL files")
    parser.add_argument("--output-dir", required=True, help="Directory where Excel files will be saved")

    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    # Create the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # List all JSONL files in the input directory
    jsonl_files = [f for f in os.listdir(input_dir) if f.endswith(".jsonl")]

    # Process each JSONL file
    for jsonl_file in jsonl_files:
        language = jsonl_file.split(".")[0]  # Extract language code from filename

        # Read the JSONL file
        with open(os.path.join(input_dir, jsonl_file), "r", encoding="utf-8") as file:
            jsonl_data = file.readlines()

        # Convert JSONL data to a DataFrame
        data = jsonl_to_dataframe(jsonl_data)

        # Generate and save the Excel file
        generate_excel(language, data, output_dir)


if __name__ == "__main__":
    main()

# python generate_xlsx.py --input-dir data --output-dir output_flag
