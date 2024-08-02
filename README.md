# 2-in-1 Email Tool

## Overview

The 2-in-1 Email Tool is a Python script designed to help users manage and process large lists of email-password pairs or email lists. It provides two main features:
1. **Email Extractor**: Extracts emails from email-password pairs and saves them to a file.
2. **Email Sorter**: Sorts emails by their domain and saves them into separate files.

## Features

1. **Email Extractor**: 
   - Reads a file containing email-password pairs.
   - Extracts the email addresses.
   - Saves the extracted emails into a file named `email.txt` in a folder called `Extracted Emails`.

2. **Email Sorter**:
   - Reads a file containing a list of emails.
   - Sorts the emails by their domain.
   - Saves the sorted emails into separate files named after their respective domains in a folder called `Sorted Emails`.

## Prerequisites

- Python 3.x
- Tkinter library (usually included with Python)

## Installation

1. Clone the repository or download the script file.

2. Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. Install the required libraries if not already installed:
   ```bash
   pip install tk
