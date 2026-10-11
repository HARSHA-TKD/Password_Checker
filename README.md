"Python" (https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
"Security" (https://img.shields.io/badge/Cybersecurity-Password%20Analysis-00BFFF?style=for-the-badge)
"Tests" (https://img.shields.io/badge/Tests-Unittest-2E8B57?style=for-the-badge)
"Status" (https://img.shields.io/badge/Status-Learning%20Project-708090?style=for-the-badge)

A beginner-friendly Python tool that evaluates password characteristics, flags some predictable patterns, and provides suggestions for improvement.

✨ Features

- 🔐 Hidden password input using "getpass"
- 🛡️ Password strength classification
- 🔎 Basic detection of repeated characters and predictable sequences
- 💡 Suggestions for improving weak passwords
- 🧪 Automated tests using Python's "unittest"
- 💻 Color-coded terminal output

🧰 Technology

- Python
- "getpass"
- "string"
- "unittest"

⚠️ Limitations

This project uses simple rules and pattern checks. It does not guarantee that a password is secure, detect every common password, or replace a dedicated password-strength estimation tool. Test only with fake passwords; never enter your real password into this learning project.

🎯 Learning outcomes

- Python functions and conditionals
- String processing
- Password hygiene concepts
- Unit testing
- Git and GitHub version control

##Demo
![Password Checker Demo](screenshots/password-checker-demo.png)

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
