import smtplib
import ssl
import time

# Gmail SMTP server configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465  # SSL Port

# Your Gmail credentials (App Password, not regular password)
EMAIL_ADDRESS = "mattloki7@gmail.com"
APP_PASSWORD = "hlnwlyaitdborwbq"

# Email details
recipient_email = "seehouse@gmail.com"
subject = "Congratulations!! You're a Winner!"
message_body = "Congratulations, You are the Grand Prize Winner! Reply to Collect Your $$$"

# Create the email message
def create_message(subject, body, recipient):
    return f"Subject: {subject}\n\n{body}"

# Sending multiple emails in quick succession
def send_emails(num_emails, delay=1):
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(EMAIL_ADDRESS, APP_PASSWORD)
        
        for i in range(num_emails):
            # Create the email content
            message = create_message(subject, f"{message_body} - Message {i + 1}", recipient_email)
            
            # Send the email
            server.sendmail(EMAIL_ADDRESS, recipient_email, message)
            print(f"Sent email {i + 1}")

            # Optional delay between emails to avoid getting flagged
            time.sleep(delay)

# Customize the number of emails and delay between them
num_emails_to_send = 50  # Number of emails to send
delay_between_emails = 5  # Delay in seconds between emails

# Start sending emails
send_emails(num_emails_to_send, delay_between_emails)
