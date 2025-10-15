import yagmail

def send_email(content):
    # Confirmation prompt for sending email
    confirmation = input("Do you want to send this email? (y/n): ")
    if confirmation.lower() == 'y':
        receiver = 'euniceadewusic@gmail.com'
        message = content
        sender = yagmail.SMTP('climiradiroberts@gmail.com', 'your_app_password')  # To whomever forks this: Replace with your Gmail account password
        sender.send(to=receiver, subject="Automated mail from Asiri", contents=message)
        print("Email sent successfully!")
    else:
        print("Email cancelled.")
        print ("Exiting...")
        exit(0)

# if __name__ == '__main__':
#     send_email()  Call the send_email function