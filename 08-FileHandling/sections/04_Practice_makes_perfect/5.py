# emails.py
import re

# odczyt
def read(path="email.txt"):
    with open(path, encoding="utf-8") as f:
        return f.read()
# wyznaczenie elementu header
def header(name, text):
    # headers can be "From: Name <a@b.c>" or "From: a@b.c"
    m = re.search(rf"^{name}:\s*(.+)$", text, re.MULTILINE | re.IGNORECASE)
    return m.group(1).strip() if m else None

# wyznaczenie adresu
def extract_address(value):
    if value is None:
        return None
    m = re.search(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+", value)
    return m.group(0) if m else None

# zwrocenie adresu email
def email_sender(path="email.txt"):
    return extract_address(header("From", read(path)))

# zwrocenie odbiorcy
def email_recipient(path="email.txt"):
    return extract_address(header("To", read(path)))

# zwrocenie tytulu
def email_subject(path="email.txt"):
    return header("Subject", read(path))

# zwrocenie elementu body maila (tresc)
def email_body(path="email.txt"):
    text = read(path)
    # body starts after the first blank line (end of headers)
    m = re.split(r"\r?\n\r?\n", text, maxsplit=1)
    return m[1].strip() if len(m) == 2 else None



print("Sender:   ", email_sender())
print("Recipient:", email_recipient())
print("Subject:  ", email_subject())
print("Body:\n" + (email_body() or ""))