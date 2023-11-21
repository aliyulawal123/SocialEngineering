print("Welcome to Social Engineering")
import random

def generate_fake_phishing_email():
    # List of common phishing email elements
    greetings = ["Dear Customer", "Hello", "Attention", "Dear User"]
    sender_names = ["Your Bank", "Tech Support", "Account Verification", "Customer Service"]
    suspicious_links = ["http://fake-website.com", "http://phishing-site.org", "http://malicious-link.net"]

    # Construct a fake phishing email
    greeting = random.choice(greetings)
    sender_name = random.choice(sender_names)
    subject = f"{greeting}, {sender_name} needs your immediate attention!"
    body = f"Dear user,\n\nWe have noticed suspicious activity on your account. Click the following link to verify your information: {random.choice(suspicious_links)}"

    return f"Subject: {subject}\n\n{body}"

def simulate_phishing_attack():
    # Simulate sending a phishing email to a list of email addresses
    email_addresses = ["user1@example.com", "user2@example.com", "user3@example.com", "user4@example.com"]

    for email_address in email_addresses:
        phishing_email = generate_fake_phishing_email()
        print(f"Sending phishing email to {email_address}:\n\n{phishing_email}\n\n")

# Simulate a phishing attack
simulate_phishing_attack()
