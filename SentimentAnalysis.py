from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
import imaplib
import email
from email.header import decode_header

#Change file name to config.samlpe.txt and input gmail credentials there
f = open("PythonProjects\config.private.txt", "r")
USER = f.readline()
PASSWORD = f.readline()
f.close()

#logging into gmail account
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(USER, PASSWORD)

#getting email subjects
#from https://www.thepythoncode.com/article/reading-emails-in-python
status, messages = mail.select("INBOX")
#number of emails fetched
N = 3
messages = int(messages[0])

subjectList = []

for i in range(messages, messages-N, -1):
    # fetch the email message by ID
    res, msg = mail.fetch(str(i), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode(encoding = encoding)
            subjectList.append(subject)

#download NLTK vader lexicon           
nltk.download('vader_lexicon')

#iterate through subjects and analyse it through prebuilt NLTK model
for sub in subjectList:
    print(sub)
    analysis = SentimentIntensityAnalyzer()
    print(analysis.polarity_scores(sub))

mail.close()
mail.logout()