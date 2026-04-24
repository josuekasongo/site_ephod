import os
import re

files = ["index.html", "about.html", "services.html", "portfolio.html", "careers.html", "ongoing.html", "contact.html"]

for filename in files:
    if not os.path.exists(filename):
        print(f"File {filename} not found, skipping.")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update navbar toggle breakpoint
    content = content.replace('navbar-expand-lg', 'navbar-expand-xl')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename} responsive breakpoints")
