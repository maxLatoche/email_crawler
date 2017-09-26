import email
import getpass
import imaplib

M = imaplib.IMAP4_SSL('imap.gmail.com')

ADDRESS = 'max.latoche@gmail.com'
PASSWORD = ''

def process_emails(M):
    rv, data = M.search(None,'All')
    if rv != 'OK':
        print("No messages found.")
        return

    with open('emails.txt', 'w') as text_file:
        for num in data[0].split():
            rv, data = M.fetch(num, "RFC822")
            if rv != "OK":
                print("Error getting message")
                return
            print(data[0][1])
            # msg = data[0][1].decode("utf-8")
            # msg = email.message_from_string(msg)
            # print('Message {}:{}'.format(num,msg['Subject']), file=text_file)
            # print('Message {}:{}'.format(num,msg['Date']), file=text_file)

try:
    M.login(ADDRESS, getpass.getpass())
except imaplib.IMAP4_SSL.error:
    print('Login Failed')

rv, mailboxes = M.select('INBOX',True)
if rv == "OK":
    process_emails(M)
    print("Processing Mailbox... \n")
else:
    print("ERROR: Unable to open mailbox ")

M.logout()
