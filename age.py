from datetime import datetime
import re

# Your details
BIRTH_DATE = datetime(2002, 10, 13)
NAME = "Gautam Rana" 

def calculate_age(birth_date):
    today = datetime.now()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def update_readme():
    with open('README.md', 'r') as file:
        content = file.read()

    # Get current time and format it
    now = datetime.now()
    current_time_str = now.strftime("%I:%M %p")

    # Calculate age
    age = calculate_age(BIRTH_DATE)

    updated_content = re.sub(
        r"Name: .* \| Time: .* \| Age: \d+",
        f"Name: {NAME} | Time: {current_time_str} | Age: {age}",
        content
    )

    with open('README.md', 'w') as file:
        file.write(updated_content)

if __name__ == "__main__":
    update_readme()
