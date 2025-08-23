import os
from datetime import datetime

# Your birth date
BIRTH_DATE = datetime(2002, 10, 13) # Replace with your own birth date

def calculate_age(birth_date):
    today = datetime.now()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def update_readme():
    with open('README.md', 'r') as file:
        content = file.read()

    # Get current time and format it
    now = datetime.now()
    current_time_str = now.strftime("%I:%M %p %Z").replace("UTC", "IST").replace("IST", "IST") # Replace with your timezone if different
    
    # Calculate age
    age = calculate_age(BIRTH_DATE)
    
    # Update content in README using a placeholder
    updated_content = content.replace(
        "",
        f"Time: {current_time_str} | Age: {age}"
    )

    with open('README.md', 'w') as file:
        file.write(updated_content)

if __name__ == "__main__":
    update_readme()