import os
from collections import defaultdict
from tkinter import Tk, filedialog

def extract_email(email_password):
    try:
        email, _ = email_password.split(":", 1)
        return email
    except ValueError:
        print(f"Invalid format, skipping: {email_password}")
        return None

def sort_emails_by_domain(emails):
    domain_dict = defaultdict(list)
    for email in emails:
        try:
            domain = email.split('@', 1)[1]
            domain_dict[domain].append(email)
        except IndexError:
            print(f"Invalid email format, skipping: {email}")
    return domain_dict

def get_file_path():
    root = Tk()
    root.withdraw()  # Close the root window
    file_path = filedialog.askopenfilename(title="Select the file containing email-password pairs or email list")
    return file_path

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def sanitize_filename(name):
    # Replace invalid characters with an underscore
    return name.replace(':', '_').replace('/', '_').replace('\\', '_')

def email_extractor():
    input_file = get_file_path()
    if not input_file:
        print("No file selected. Exiting.")
        return

    emails = []
    with open(input_file, 'r') as file:
        for line in file:
            email_password = line.strip()
            email = extract_email(email_password)
            if email:
                emails.append(email)

    output_dir = 'Extracted Emails'
    ensure_directory_exists(output_dir)
    email_file = os.path.join(output_dir, 'email.txt')
    with open(email_file, 'a') as file:  # Open file in append mode
        file.write('\n'.join(emails) + '\n')
    
    print(f"Emails have been extracted and saved to {email_file}")

def email_sorter():
    input_file = get_file_path()
    if not input_file:
        print("No file selected. Exiting.")
        return

    emails = []
    with open(input_file, 'r') as file:
        for line in file:
            email = line.strip()
            if "@" in email:  # Ensure the line is an email
                emails.append(email)

    sorted_emails = sort_emails_by_domain(emails)

    output_dir = 'Sorted Emails'
    ensure_directory_exists(output_dir)
    for domain, emails in sorted_emails.items():
        sanitized_domain = sanitize_filename(domain)
        domain_file = os.path.join(output_dir, f'{sanitized_domain}.txt')
        with open(domain_file, 'a') as file:  # Open file in append mode
            file.write('\n'.join(emails) + '\n')
    
    print(f"Emails have been sorted and saved by domain in {output_dir}")

def main():
    print("Welcome to the 2-in-1 Email Tool!")
    print("Please select a feature:")
    print("1. Email Extractor")
    print("2. Email Sorter")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        email_extractor()
    elif choice == '2':
        email_sorter()
    else:
        print("Invalid choice. Exiting.")

if __name__ == "__main__":
    main()
