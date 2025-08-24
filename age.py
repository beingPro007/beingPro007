from datetime import datetime
import re

BIRTH_DATE = datetime(2002, 10, 13)
NAME = "Gautam Rana"

def calculate_age(birth_date):
    """Calculates the current age based on a birth date."""
    today = datetime.now()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def update_readme():
    """Reads the README, updates dynamic content, and writes it back."""
    try:
        with open('README.md', 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print("Error: README.md not found in the current directory.")
        return

    now = datetime.now()
    current_time_str = now.strftime("%I:%M %p") # e.g., 08:57 AM
    age = calculate_age(BIRTH_DATE)

    content = re.sub(
        r"Name: .* \| Time: .*",
        f"Name: {NAME} | Time: {current_time_str}",
        content
    )

    content = re.sub(
        r"(Overclocking the Brilliance, currently at )\d+( MHz)",
        rf"\g<1>{age}\g<2>",
        content
    )

    with open('README.md', 'w') as file:
        file.write(content)
    
    print("README.md has been successfully updated.")

if __name__ == "__main__":
    update_readme()
