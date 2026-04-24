import os
import re

files = ["about.html", "contact.html", "ongoing.html", "portfolio.html", "services.html", "careers.html"]

with open("index.html", "r", encoding="utf-8") as f:
    content_index = f.read()

# Extract footer block
footer_match = re.search(r'(<footer.*?</footer\s*>)', content_index, re.DOTALL)
if not footer_match:
    print("Could not find footer in index.html")
    exit(1)

footer_html = footer_match.group(1)

for file in files:
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Replace the entire footer block
        new_content = re.sub(r'<footer.*?</footer\s*>', lambda x: footer_html, content, flags=re.DOTALL)
        
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated footer in {file}")
