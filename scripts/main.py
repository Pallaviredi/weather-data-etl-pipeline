from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():
    print("Step 1: Extracting...")
    raw_data = extract_data()

    print("Step 2: Transforming...")
    df = transform_data(raw_data)

    print("Step 3: Loading...")
    load_data(df)

    print("Pipeline completed!")

if __name__ == "__main__":
    run_pipeline()