import getpass
import colorama
from colorama import Fore
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


print(Fore.BLUE+'       ####      ##     ##              ', Fore.RED+'####       ######      ####       ######')
print(Fore.BLUE+'       ##  ##     ##   ##               ', Fore.RED+'##  ##     ##          ##  ##     ##    ')
print(Fore.BLUE+'       ####         ##                  ', Fore.RED+'####       ######      ####       ######')
print(Fore.BLUE+'       ##  ##       ##                  ', Fore.RED+'##         ##          ##         ##    ')
print(Fore.BLUE+'       ####         ##                  ', Fore.RED+'##         ######      ##         ######')


while True:
    msg = MIMEMultipart()

    from_email = input('[*]From email:')
    password = getpass.getpass('[*]Password:')
    to_email = input('[*]To email:')
    message = input('[*]Message:')
    col = int(input('[*]Col of messages:'))


    if to_email == 'farafonovegor0707@gmail.com':
        print('Error')
    else:
        i = 1
        while col >= 1:
            msg.attach(MIMEText(message, 'plain'))
            server = smtplib.SMTP('smtp.gmail.com: 587')
            server.starttls()
            server.login(from_email, password)
            server.sendmail(from_email, to_email, msg.as_string())
            server.quit()
            print('[+]Sending message ' + i)
            i = i + 1

    while True:  
        if input('[*]Restart [y/n]:') in ('n','y'):
            print(Fore.RESET)
            break