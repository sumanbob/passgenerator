import random
import string

def generate_password(length):
    if length < 4:
        return "Password too short! Try at least 4 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Random Password Generator")

    while True:
        try:
            length = int(input("Enter password length: "))
            password = generate_password(length)
            print(f"Generated Password: {password}")
        except ValueError:
            print("⚠️ Please enter a valid number.")

        again = input("Generate another password? (y/n): ").lower()
        if again != 'y':
            print("Goodbye! 🔒")
            break

if __name__ == "__main__":
    main()