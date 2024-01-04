# Account Knocker

The Account Knocker is a Python script that uses Selenium and BeautifulSoup to check the presence of an email address in various online platforms such as Pinterest, Spotify, and Quora. The script interacts with the web pages, captures relevant information, and writes the results to an output file.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Customization](#customization)
- [Closing Notes](#closing-notes)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.x
- Selenium
- ChromeDriver
- BeautifulSoup

Install the required dependencies using:

pip install selenium beautifulsoup4

Download ChromeDriver from https://sites.google.com/chromium.org/driver/ and ensure it's in your system's PATH.

Installation
Clone the repository:
https://github.com/GowthamS7/account-knocker-.git

Navigate to the project directory:
cd account-knocker

Usage
1.Specify the email addresses to be checked by modifying the email_list in the script.
2.Run the script:
python account_knocker v1.0.py

The script will open a Chrome browser, perform checks on the specified email addresses, and write the results to the output.txt file.

Results
The script will generate an output.txt file containing the results of the account checks. Each line in the file corresponds to the status of an email address for a specific platform.

