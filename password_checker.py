import string


def check_password(password):
    score = 0
    suggestions = []

    # Check password length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters; 12 or more is better.")

    # Check character variety
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter (A-Z).")

    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter (a-z).")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append("Add a number (0-9).")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        suggestions.append("Add a special character (e.g. !, @, #).")

    # Check for common weak patterns
    common_patterns = ["123", "password", "qwerty", "admin"]
    if any(pattern in password.lower() for pattern in common_patterns):
        score = min(score, 2)
        suggestions.append(
            "Avoid common words and predictable sequences."
        )

    # Assign a strength rating
    if len(password) < 8 or score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength, score, suggestions


def main():
    print("=" * 38)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 38)
    print("Use a fake password for testing.")
    print("Type 'exit' to quit.\n")

    while True:
        password = input("Enter a test password: ")

        if password.lower() == "exit":
            print("Thanks for using the checker!")
            break

        if not password:
            print("Please enter a password to check.\n")
            continue

        strength, score, suggestions = check_password(password)

        print("\n--- SECURITY REPORT ---")
        print("Strength :", strength)
        print("Score    :", str(score) + "/6")

        if suggestions:
            print("\nSuggestions:")
            for suggestion in suggestions:
                print("-", suggestion)
        else:
            print("All basic character checks passed.")

        print("-" * 38 + "\n")


if __name__ == "__main__":
    main()