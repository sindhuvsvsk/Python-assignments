def extract_usernames_domains(emails=None):
    usernames = []
    for emails in emails:
        usernames.append(emails.split('@')[0])
    return usernames


emails = ["apple@gmail.com", "orange@yahoo.com", "grape@abc.net"]
usernames = extract_usernames_domains(emails)
print(usernames)
