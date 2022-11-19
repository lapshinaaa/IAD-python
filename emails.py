import re

file = open("кондуит 2022 - Преподаватели и ассистенты.txt", 'r', encoding="utf8")
file_updated = open("updated_email.txt", "w")     # creating a new file


for line in file:   # seeking all the emails
    match = re.findall(r'[\w\\.-]+@[\w\\.-]+\.\w+(?:\.\w+)?', line)  # regex for finding all email addresses
    for email in match:
        print(email)    # printing out all the found email addresses

        pattern = re.compile('^[A-Za-z0-9._%+-]+@(edu\\.)?hse\\.ru')  # regex for hse.ru and edu.hse.ru domains

        if not pattern.match(email):

            file_updated.write(re.sub(email, "Pr1v@cY REstorED", line))  # changing emails to the phrase

        else:

            file_updated.write(line)

file_updated.close()




