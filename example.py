import csv
from dateutil import parser
import openai

# Set your OpenAI API key
openai.api_key = "sk-proj-fTbu4jkJWirOmIvINkL4T3BlbkFJbZL0pzrDvC1ForgtiNRd"

def format_date(date):
    # Parse the date string using dateutil.parser
    parsed_date = parser.parse(date)
    # Format the parsed date as 'YYYY-MM-DD'
    formatted_date = parsed_date.strftime("%Y-%m-%d")
    return formatted_date

def format_dates_in_csv(input_file, output_file):
    try:
        # Read CSV file
        with open(input_file, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            rows = list(reader)

        # Add formatted dates to rows
        for row in rows:
            date = row['Dates']  # Assuming the column name is 'Date'
            formatted_date = format_date(date)
            row['Formatted Date'] = formatted_date

        # Write updated CSV file
        fieldnames = list(rows[0].keys()) + ['Formatted Date']
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames)
            writer.writeheader()
            writer.writerows(rows)

        print(f"Output CSV file saved at: {output_file}")

    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")

if __name__ == "__main__":
    input_file = "sample_dates.csv"  # Replace with your input CSV file
    output_file = "output.csv"  # Replace with the desired output file name

    format_dates_in_csv(input_file, output_file)

