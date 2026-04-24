import os
import re

files = ["about.html", "services.html", "portfolio.html", "careers.html", "ongoing.html", "contact.html"]

breadcrumb_pattern = re.compile(r'<div class="breadcrumb-nav mb-3">.*?</div>', re.DOTALL)

for filename in files:
    if not os.path.exists(filename):
        print(f"File {filename} not found.")
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove breadcrumb block
    new_content = breadcrumb_pattern.sub('', content)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Removed breadcrumb from {filename}")
    else:
        print(f"Breadcrumb not found in {filename}")
