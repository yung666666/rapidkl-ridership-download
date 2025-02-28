# RapidKL Ridership Data Downloader (generated by AI)
This script downloads ridership data from the data.gov.my, processes it, and stores the results in Parquet format. It handles both daily and monthly ridership data, ensuring that duplicate entries are removed while maintaining the latest values.

## Features
- Downloads ridership data from the government data source [https://storage.data.gov.my/dashboards/prasarana_timeseries.parquet}](https://storage.data.gov.my/dashboards/prasarana_timeseries.parquet)
- Parses and processes the Parquet file.
- Aggregates ridership data to remove duplicate entries.
- Separates daily and monthly ridership data.
- Appends new data to existing Parquet files while preventing duplicate records.

## Installation (Run the commands below on "Anaconda Prompt" or "Command Prompt")
1. **Clone the Repository:** (or download the script directly):
   ```bash
   git clone https://github.com/yung666666/rapidkl-ridership-download.git
   cd rapidkl-ridership-download
   ```
2. **Install Dependencies:**
The script requires a few Python libraries. Install them using the provided requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```
The required libraries are:
- requests: For making HTTP requests to fetch web pages.
- beautifulsoup4: For parsing HTML content.
- pandas: For data manipulation and CSV handling.

## Usage
- Run the commnads on "Anaconda Prompt" or "Command Prompt":
   ```bash
   python rapidkl_ridership_download.py
   ```
## File Structure
- daily_ridership.parquet – Stores processed daily ridership data.
- monthly_ridership.parquet – Stores processed monthly ridership data.

## Error Handling
- If the data download fails, the script will print an error message with the HTTP status code.

## Key Additions
-  You can set up Windows Task Scheduler to run the script monthly, ensuring you always obtain the latest ridership data.

## Acknowledgments
- Data provided by data.gov.my.
- Built with Python and open-source libraries.
