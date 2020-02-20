import os

def email_cleanup(list_of_email):
    #Remove newline characters
    clean_email_list = []
    for email in list_of_email:
        clean_email_list.append(email.rstrip().lower())
        clean_email_list = set(clean_email_list)
        clean_email_list = list(clean_email_list)

    return clean_email_list


def write_a_file(list, filename):
    if os.path.exists(filename):
        os.rename(filename, filename + ".yesterday")

    f = open(filename, "w")
    f.write("\n".join(list))
    f.close()


def check_for_dupes(todays_list): 
    with open('clean-emails.txt.yesterday') as emails:
        yesterdays_list = []
        for email in emails:
            yesterdays_list.append(email)

    clean_yesterday = email_cleanup(yesterdays_list)

    new_email_list = []
    x =0
    while x < len(todays_list):
        if todays_list[x] in clean_yesterday:
            x += 1
            print(len(todays_list))
            print("You''ve got a match BUDDY!")
        else:
            new_email_list.append(todays_list[x])
            x += 1

    write_a_file(new_email_list, "our_new_subscribers.txt")
