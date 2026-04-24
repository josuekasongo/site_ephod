import os
import re

files = ["about.html", "services.html", "portfolio.html", "careers.html", "ongoing.html", "contact.html"]

breadcrumb_pattern = re.compile(r'<div class="breadcrumb-nav.*?</div>', re.DOTALL)
nav_breadcrumb_pattern = re.compile(r'<nav class="breadcrumb-nav.*?</nav>', re.DOTALL)

for filename in files:
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Apply light-elite to banner
    new_content = content.replace('class="srv-banner-animated"', 'class="srv-banner-animated light-elite"')
    # just in case it was already replaced and now says light-elite light-elite, fix it
    new_content = new_content.replace('class="srv-banner-animated light-elite light-elite"', 'class="srv-banner-animated light-elite"')
    
    # 2. Remove breadcrumbs
    new_content = breadcrumb_pattern.sub('', new_content)
    new_content = nav_breadcrumb_pattern.sub('', new_content)
    
    if new_content != content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"No changes for {filename}")

