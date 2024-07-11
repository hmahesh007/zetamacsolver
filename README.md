# Zetamac Arithmetic Solver

This project automates the process of solving arithmetic problems on the Zetamac Arithmetic website. The script uses Selenium for web automation and PyAutoGUI for typing the answers.

## Prerequisites

- Python 3.6 or higher
- Google Chrome browser

## Installation

1. Clone the repository or download the script `zetamac.py`.

2. Install the required Python packages using pip:

    ```sh
    pip install selenium webdriver-manager pyautogui
    ```

3. Ensure you have the Chrome browser installed on your machine.

## Usage

1. Run the script:

    ```sh
    python zetamac.py
    ```

2. The script will open a Chrome browser window and navigate to the Zetamac Arithmetic game. It will continuously solve the arithmetic problems presented on the page.

## How It Works

- The script uses Selenium to automate the Chrome browser.
- It locates the arithmetic problem on the page using XPath and replaces symbols to make the expression Python-friendly.
- The script evaluates the expression and types the answer using PyAutoGUI.
- The process repeats for new questions, automating the entire solving process.

## Code Overview

- **Import necessary modules:**
  ```python
  import time
  from selenium import webdriver
  from selenium.webdriver.chrome.service import Service
  from webdriver_manager.chrome import ChromeDriverManager
  from selenium.webdriver.common.by import By
  import pyautogui



**NOTE**: This code can be converted using Javascript so it can run directly in web browser's console. 
