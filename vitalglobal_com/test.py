import smtplib

# Set up the connection to the SMTP server
s = smtplib.SMTP(
    "mail.vitelglobal.com", 465
)  # Replace 'your_smtp_server.com' with your SMTP server address
s.starttls()  # If your SMTP server requires TLS

# Login to the SMTP server (replace 'your_username' and 'your_password' with your credentials)
s.login("no-reply", "82z1GRC#*0eN")

# Compose the email
sender_email = "no-reply@varundigitalmedia.com"
recipient_email = "aman.k@pranathiss.com"
# cc_email = "suresh@vitelglobal.com", "mukhtiyar@vitelglobal.com"
subject = "From NOC Python Test Email"
body = "Hello, this is a test email sent from Python. \n From NOC"

# Construct the email message
message = f"""Subject: {subject}

{body}"""

# Send the email
s.sendmail(sender_email, recipient_email, message)
# s.sendmail(sender_email, cc_email, message)

# Quit the SMTP server connection
s.quit()
