import string
from getpass import getpass
def has_weak_pattern(password):
    password = password.lower()

    # Check for repeated characters, e.g. aaaaa
    if len(password) >= 4:
        for i in range(len(password) - 3):
            if len(set(password[i:i + 4])) == 1:
                return True

    # Check for common sequences, e.g. abcd or 1234
    sequences = [
        "abcdefghijklmnopqrstuvwxyz",
        "0123456789",
        "qwertyuiop"
    ]

    for sequence in sequences:
        for i in range(len(sequence) - 3):
            pattern = sequence[i:i + 4]
            if pattern in password:
                return True

    return False

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
    common_patterns = ["password", "qwerty", "admin"]

    if (
        any(pattern in password.lower() for pattern in common_patterns)
        or "123" in password
        or has_weak_pattern(password)
    ):
        score = min(score, 2)
        suggestions.append(
            "Avoid common words, repeated characters, and sequences."
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
    BLUE = "\033[94m"
    CYAN = "\033[96m"
    SILVER = "\033[37m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    RESET = "\033[0m"

    print(f"\n{BLUE}" + "=" * 44)
    print("       PASSWORD SECURITY CHECKER")
    print("          CYBERSECURITY TOOL")
    print("=" * 44 + f"{RESET}")

    print(f"{SILVER}Password input is hidden for privacy.")
    print("Use a fake password for testing.")
    print(f"Type 'exit' to quit.{RESET}\n")

    while True:
        password = getpass(f"{CYAN}Enter test password: {RESET}")

        if password.lower() == "exit":
            print(f"\n{BLUE}Session closed. Stay secure!{RESET}\n")
            break

        if not password:
            print(f"{YELLOW}Please enter a password.{RESET}\n")
            continue

        strength, score, suggestions = check_password(password)

        if strength == "Strong":
            color = GREEN
        elif strength == "Moderate":
            color = YELLOW
        else:
            color = RED

        print(f"\n{BLUE}" + "-" * 44)
        print("              SECURITY REPORT")
        print("-" * 44 + f"{RESET}")

        print(f"Strength : {color}{strength}{RESET}")
        print(f"Score    : {CYAN}{score}/6{RESET}")

        if suggestions:
            print(f"\n{YELLOW}Suggestions:{RESET}")
            for suggestion in suggestions:
                print(f"  - {suggestion}")
        else:
            print(f"{GREEN}All basic character checks passed.{RESET}")

        print(f"{BLUE}" + "-" * 44 + f"{RESET}\n")


if __name__ == "__main__":
    main()