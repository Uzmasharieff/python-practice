import string
import getpass


def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add symbols like !, @, or #.")

    if score >= 6 and len(password) >= 12:
        strength = "Strong"
    elif score >= 4:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, suggestions


def main():
    print("=" * 38)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 38)

    password = getpass.getpass("Enter a test password: ")

    strength, suggestions = check_password_strength(password)

    print(f"\nPassword strength: {strength}")

    if suggestions:
        print("\nSuggestions to improve:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("Good! Your password meets these checks.")


if __name__ == "__main__":
    main()
