[![Join our Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/hidden_coding)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/aero25x)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/aero25x)
[![YouTube](https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@flaming_chameleon)

# Pudgypenguins.com - Claim Checker

![image](https://github.com/user-attachments/assets/c8426fbd-6808-4dd1-b00a-f3c22e78c610)


A Python script to read cryptocurrency wallet addresses from a file, fetch their pending token balances using the [Pudgy Penguins Claim API](https://claim.pudgypenguins.com/), and display the results in a user-friendly format.



## Features

- **Read Wallets from File:** Supports reading multiple wallet addresses from a text file, each on a new line.
- **Fetch Balances:** Retrieves pending token balances for each wallet using the Pudgy Penguins Claim API.
- **Formatted Output:** Displays balances in a human-readable format with appropriate decimal places.
- **Error Handling:** Handles common errors such as network issues, invalid wallet addresses, and malformed API responses.

---

## Prerequisites

- **Python 3.6 or higher**
- **pip** (Python package installer)

---

## Installation

1. **Clone the Repository** (or download the script directly):

    ```bash
    git clone https://github.com/Aero25x/Pudgypenguins-wallets-checker.git
    cd Pudgypenguins-wallets-checker
    ```

2. **Install Required Libraries:**

    The script relies on the `requests` library for making HTTP requests. Install it using pip:

    ```bash
    pip install cloudscraper
    ```

3. **Prepare Wallets File:**

    Create a `wallets.txt` file in the project directory. List each wallet address on a separate line:

    ```
    0x000FIRST000
    0x000SECOND000
    0x000THIRD000
    ```

---

## Usage

1. **Ensure `wallets.txt` is properly formatted** with one wallet address per line.

2. **Run the Script:**

    ```bash
    python pengu-checker.py
    ```

3. **View Output:**

    The script will output each wallet address along with its pending token balance, rounded to four decimal places.

---

## Example

**Given `wallets.txt`:**

```
0x000FIRST000
0x000SECOND000
0x000THIRD000
```

**Running the script:**

```bash
python pengu-checker.py
```

**Sample Output:**

```
0x000FIRST000 -> 1.2345
0x000SECOND000 -> 0.0000
0x000THIRD000 -> 56.7890
```

---

## Error Handling

The script includes error handling for:

- **File Not Found:** If `wallets.txt` is missing, the script will notify the user.
- **Network Issues:** Handles connection errors or timeouts when contacting the API.
- **Invalid Responses:** Checks for correct JSON structure and data types.
- **Invalid Wallet Addresses:** Alerts if the wallet address format is incorrect or not recognized by the API.

---

## License

This project is licensed under the [MIT License](LICENSE).
---

# Contact

Для любых вопросов, пожалуйста, свяжитесь по адресу [your.email@example.com](mailto:your.email@example.com).
