emails_received = {"john@example.com", "spam1@example.com", "spam2@example.com", "jane@example.com"}
spam_list = {"spam1@example.com", "spam2@example.com"}

# Część wspólna zbiorów (przecięcie).
spam_emails = emails_received & spam_list  # Intersection
print("Spam emails:", spam_emails)
