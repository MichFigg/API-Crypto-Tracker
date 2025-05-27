#  API Crypto Tracker

Python project that fetches the latest cryptocurrency prices from CoinMarketCap and saves them to a local CSV file.

---

##  Features

- Fetches live crypto data from [CoinMarketCap API](https://coinmarketcap.com/api/)
- Saves results to `crypto_dataset.csv` with timestamp
- Automatically appends new rows
- Uses `.env` file to hide sensitive API keys

---

##  Technologies Used

- Python
- Jupyter Notebook
- requests
- dotenv
- CoinMarketCap API

---

##  Sample Output

The CSV file will contain:

| Name     | Price (USD) | Timestamp        |
| -------- | ----------- | ---------------- |
| Bitcoin  | 110307.13    | 27-05-2025 19:40 |
| Ethereum | 2673.69     | 27-05-2025 19:40 |
| ...      |             |                  |



##  Example Visualization For Bitcoin

This project includes a simple line chart that tracks real-time changes in cryptocurrency price over time.

![image](https://github.com/user-attachments/assets/0c477a25-7d9a-48d6-a41b-22991fe9f4cc)


- **X-axis**: Timestamp (time of data retrieval)
- **Y-axis**: Price in USD
- The chart updates as new rows are appended to the dataset

## Author
Michał Figwer

