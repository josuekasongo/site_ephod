import os
import re

files = ["about.html", "contact.html", "ongoing.html", "portfolio.html", "services.html", "careers.html"]

with open("index.html", "r", encoding="utf-8") as f:
    content_index = f.read()

# Extract navbar block
navbar_match = re.search(r'(<!-- ========== NAVBAR ========== -->\s*<nav.*?</nav>)', content_index, re.DOTALL)
if not navbar_match:
    print("Could not find navbar in index.html")
    exit(1)

navbar_html = navbar_match.group(1)

for file in files:
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            content = f.read()
            
        new_content = re.sub(r'<!-- ========== NAVBAR ========== -->\s*<nav.*?</nav>', lambda x: navbar_html, content, flags=re.DOTALL)
        
        with open(file, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated navbar in {file}")

