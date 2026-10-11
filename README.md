🔐 Password Strength Checker

🛡️ A Python-Based Cybersecurity Project

A lightweight, beginner-friendly password analysis tool that evaluates basic password characteristics, identifies selected common patterns, and provides actionable suggestions to improve password strength.

Built as part of my Cybersecurity Internship at CodeOrbit.

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python%203-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3"/>
  <img src="https://img.shields.io/badge/Category-Cybersecurity-0B6E99?style=for-the-badge&logo=hackthebox&logoColor=white" alt="Cybersecurity"/>
  <img src="https://img.shields.io/badge/Level-Beginner-2E8B57?style=for-the-badge" alt="Beginner level"/>
  <img src="https://img.shields.io/badge/Dependencies-None-lightgrey?style=for-the-badge" alt="No external dependencies"/>
</p>---

📌 Table of Contents

- "Overview" (#-overview)
- "Features" (#-features)
- "How It Works" (#-how-it-works)
- "Technology Stack" (#-technology-stack)
- "Getting Started" (#-getting-started)
- "Usage" (#-usage)
- "Running Tests" (#-running-tests)
- "Project Structure" (#-project-structure)
- "Limitations" (#-limitations)
- "Future Improvements" (#-future-improvements)
- "Learning Outcomes" (#-learning-outcomes)
- "Author" (#-author)

---

🎯 Overview

Weak and predictable passwords can put accounts at risk. This project demonstrates the fundamentals of password-strength checking using Python.

The program examines password length, character variety, and selected common patterns. It then generates a basic strength rating and suggestions to help users improve their password choices.

Project goals:

- Understand fundamental password-security concepts.
- Practise Python functions, loops, conditions, and string operations.
- Learn automated testing with Python's "unittest" module.
- Develop good coding and documentation habits.

✨ Features

Feature| Description
📏 Length analysis| Rewards longer passwords according to the program's rules.
🔠 Uppercase detection| Checks for uppercase letters.
🔡 Lowercase detection| Checks for lowercase letters.
🔢 Number detection| Checks for numeric characters.
🔣 Special-character detection| Checks for punctuation characters.
🚩 Pattern detection| Flags selected patterns such as "password", "qwerty", "admin", and "123".
📊 Strength rating| Displays Weak, Moderate, or Strong.
💡 Improvement tips| Suggests which basic checks need attention.
🔁 Repeated testing| Allows multiple checks in one session.
🧪 Automated tests| Tests expected behaviour using Python's built-in testing framework.

⚙️ How It Works

The checker follows a simple workflow:

      START
        |
        v
 Enter a test password
        |
        v
 Check length and character types
        |
        v
 Look for selected common patterns
        |
        v
 Calculate rule-based score
        |
        v
 Assign a strength rating
        |
        v
 Display suggestions and report
        |
        v
 Repeat or exit

Scoring logic

The current implementation awards:

- 2 points for a length of 12 or more characters.
- 1 point for a length of 8–11 characters.
- 1 point each for uppercase letters, lowercase letters, digits, and punctuation.

The maximum score is 6 points.

The program limits the score when selected common patterns are detected. A password shorter than eight characters is always rated Weak.

The rating thresholds are defined in the source code. The score is a simplified educational metric, not a measurement of true password entropy.

🧰 Technology Stack

- Python 3 — core programming language.
- "string" — standard-library punctuation characters.
- "unittest" — automated tests.
- Git and GitHub — version control and project hosting.
- Visual Studio Code — development environment.

No third-party Python packages are required.

🚀 Getting Started

Prerequisites

Install Python 3 and Git. A code editor such as Visual Studio Code is recommended.

Check your installations:

python --version
git --version

Installation

1. Clone the repository

Replace "YOUR_GITHUB_USERNAME" with your GitHub username.

git clone https://github.com/YOUR_GITHUB_USERNAME/password-strength-checker.git

2. Enter the project directory

cd password-strength-checker

3. Run the program

python password_checker.py

On Windows, if the "python" command is unavailable, try "py password_checker.py".

💻 Usage

When the program starts, enter a fictional test password.

Example:

======================================
      PASSWORD STRENGTH CHECKER
======================================
Use a fake password for testing.
Type 'exit' to quit.

Enter a test password: hello

--- SECURITY REPORT ---
Strength : Weak
Score    : 0/6

Suggestions:
- Use at least 8 characters; 12 or more is better.
- Add an uppercase letter (A-Z).
- Add a number (0-9).
- Add a special character (e.g. !, @, #).

Example output is illustrative; exact formatting depends on the current implementation.

To exit, type "exit".

🧪 Running Tests

The project includes automated tests for weak passwords, strong passwords, common patterns, missing special characters, and short passwords.

Run the test suite from the project directory:

python -m unittest -v test_password_checker

A successful run ends with "OK". If a test fails, inspect the failure message and update the code or test expectation as appropriate.

📁 Project Structure

password-strength-checker/
│
├── password_checker.py       # Main application
├── test_password_checker.py  # Automated unit tests
├── README.md                 # Project documentation
├── .gitignore                # Excludes generated and local files
└── __pycache__/              # Generated locally; not committed

⚠️ Limitations

This project is designed for learning and demonstration.

- The scoring method is rule-based and cannot reliably determine true password strength.
- Only selected common patterns are checked; the list is not comprehensive.
- The program does not check passwords against breached-password databases.
- It does not use a password manager or store passwords.
- A Strong rating does not guarantee that a password is safe or unpredictable.

Privacy reminder: Do not enter real account passwords into this educational tool. Use fictional examples for testing.

🔮 Future Improvements

Potential improvements include:

- Add more unit tests and edge-case validation.
- Improve detection of predictable sequences and repeated characters.
- Support long passphrases without unfairly penalising spaces.
- Add a graphical user interface.
- Improve the rating system using a more reliable password-strength estimation method.
- Add screenshots of program execution and test results.

🧠 Learning Outcomes

Through this project, I practised:

- Python variables, functions, conditions, and loops.
- String operations and character classification.
- Basic cybersecurity and password hygiene.
- Writing automated tests with "unittest".
- Debugging Python import and test-discovery issues.
- Using Git for version control and GitHub for project hosting.

👨‍💻 Author

Harsha Vardhan V G

First-year Computer Science Engineering student specialising in Cybersecurity.

- GitHub: "HARSHA-TKD" (https://github.com/HARSHA-TKD)

📄 Disclaimer

This project is intended for educational purposes. It is not a substitute for professional password-security tools or a guarantee of account security.

---

<p align="center">
  <i>Learn. Build. Test. Secure.</i>
</p>