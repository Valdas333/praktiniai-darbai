import smtplib # biblioteka susikalbėjimui su pašto serveriu
from email.message import EmailMessage
from slaptazodis import password # importuoju slaptažodį, 
                                 # (galima nurodyti ir tiesiai į parametrus)
from string import Template                                 
import mimetypes
with open('index.html', 'r') as f:
    html = f.read()
    
sablonas = Template(html)

# elementarios email žinutės sukūrimas:
email = EmailMessage()
email['from'] = 'Vardas Pavardė'
email['to'] = 'valdemarasged@gmail.com'
email['subject'] = 'email from python'

email.set_content(sablonas.substitute({'vardas': 'Valdas'}), 'html')

files = ['throtle.jpg', 'yoke.jpg']
for file in files:
    mimetype = mimetypes.guess_type(file)[0]
    subtype = mimetype.split('/')[1]
    with open(file, 'rb') as img:
        content = img.read()
        email.add_attachment(
            content, 
            maintype=mimetype,
            subtype=subtype, 
            filename=file)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo() # žiūrėkite, kaip į pasisveikinimą su serveriu
    smtp.starttls() # inicijuojame šifruotą kanalą
    smtp.login('testinismailas100@gmail.com', password) # nurodome prisijungimo duomenis
    smtp.send_message(email) # išsiunčiame žinutę