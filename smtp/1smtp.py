import smtplib

# List of email IDs to send the mail
li = ["abhiramchikatla03@gmail.com", "gopicharan7777@gmail.com"]

# Loop through the list of recipients
for dest in li:
    # Establish connection to Gmail SMTP server
    s = smtplib.SMTP('smtp.gmail.com', 587)
    
    # Start TLS for security
    s.starttls()
    
    # Login using the sender's email and app password
    s.login("pushpanthcbit@gmail.com", "tuhz licf tluc uvbc ")
    
    # Define the message
    message = "Hello, my dear friends"
    
    # Send the email
    s.sendmail("pushpanthcbit@gmail.com", dest, message)
    
    # Quit the server connection after sending the email
    s.quit()
