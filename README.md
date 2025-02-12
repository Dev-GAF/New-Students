# Project - New-Students

This project is a simple Python application that automates the process of sending welcome emails to students who were approved in an entrance exam. The goal is to apply the concepts of the pyautogui library, which I learned in a tutorial video, to simulate sending automated emails.

The program simulates actions like opening a web browser, logging into Gmail, filling in the required fields, and sending a personalized email to each approved student. The data for this simulation is read from a CSV file, and the program interacts with the screen using pyautogui to automate the entire emailing process.

## 📝 Description

The program provides the following features:

* Login to Gmail: Automatically opens the browser, goes to Gmail, and logs in with pre-set credentials.
* Send Welcome Email: Sends a personalized email to approved students, congratulating them on their admission.
* Data Import: Reads data from a CSV file containing student information like names, emails, and their admission status.
* Automation with pyautogui: The entire email-sending process is automated using pyautogui, simulating mouse clicks, typing, and keyboard shortcuts.

## 👨‍💻 Technologies Used:

* Python: Used for developing the logic and handling file I/O.
* pyautogui: A library that allows you to control the mouse and keyboard to automate interactions with the computer's graphical user interface (GUI). It's useful for automating repetitive tasks, such as sending emails or filling out forms in a browser.
  
The program is run directly in the terminal and uses only Python with no external databases, relying on a CSV file to store student

## 📋 License

### This project is licensed under the MIT License. See the LICENSE file for more details.
