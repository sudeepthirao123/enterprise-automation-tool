from data_loader import load_data
from processor import process_data
from reporter import generate_report

def main():
    print("Loading data...")
    data = load_data("data/sample_data.csv")

    print("Processing data...")
    processed = process_data(data)

    print("Generating report...")
    generate_report(processed)

    print("Report generated successfully!")

if __name__ == "__main__":
    main()