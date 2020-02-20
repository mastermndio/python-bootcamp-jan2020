import utilities

with open('raw_emails.txt') as emails:
    email_list = []
    for email in emails:
        email_list.append(email)

clean_email_list = utilities.email_cleanup(email_list)

utilities.write_a_file(clean_email_list, "clean-emails.txt")

utilities.check_for_dupes(clean_email_list)
