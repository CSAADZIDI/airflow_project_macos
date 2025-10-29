from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def send_email_via_smtp():
    """
    Send email using SMTP with SSL/TLS configuration
    """
    # Email configuration
    sender_email = "zidisaad.chaima@gmail.com"
    receiver_email = "zidisaad.chaima@gmail.com"
    password = "kcze qjeh wsxb qyjg"
    
    # Create message
    message = MIMEMultipart("alternative")
    message["Subject"] = "Test Airflow Email"
    message["From"] = sender_email
    message["To"] = receiver_email
    
    # HTML content
    html_content = """
    <html>
      <body>
        <h3>Airflow Email Test</h3>
        <p>This email was sent successfully using PythonOperator with SMTP!</p>
      </body>
    </html>
    """
    
    # Add HTML content
    message.attach(MIMEText(html_content, "html"))
    
    # SMTP configuration for Gmail
    smtp_server = "smtp.gmail.com"
    port = 587  # For STARTTLS
    
    try:
        # Create secure connection
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()  # Can be omitted
        server.starttls()  # Secure the connection
        server.ehlo()  # Can be omitted
        
        # Login and send email
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
        
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise
    finally:
        server.quit()
