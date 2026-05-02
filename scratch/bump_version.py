import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace ?v=7.2 with ?v=7.3
    new_content = re.sub(r'\?v=7\.2', '?v=7.3', content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Bumped version in {file}")
