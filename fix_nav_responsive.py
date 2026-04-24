import os
import re

def fix_navbar(content):
    # Check if navMenu already exists
    if 'id="navMenu"' in content and '<div class="collapse navbar-collapse"' in content:
        # Just ensure it wraps correctly if it's already there
        return content

    # Look for the toggler button
    pattern = r'(<button class="navbar-toggler[^>]*data-bs-target="#navMenu"[^>]*>.*?</button>)\s*(<ul class="navbar-nav)'
    replacement = r'\1\n      <div class="collapse navbar-collapse" id="navMenu">\n        \2'
    
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    if new_content != content:
        # Now find the end of the lists/buttons and close the div
        # Usually it's before the </div> that closes the container
        # The container is inside the nav.
        # We look for the last part of the nav which is usually the lang button or the end of the ul
        
        # Try to find the lang-btn or the last ul and put </div> after it
        if 'id="langBtn"' in new_content:
            new_content = re.sub(r'(<button class="lang-btn"[^>]*>.*?</button>)(\s*</div>\s*</div>\s*</nav>)', r'\1\n      </div>\2', new_content, flags=re.DOTALL)
        else:
            # If no lang btn, close after ul
            new_content = re.sub(r'(</ul>)(\s*</div>\s*</div>\s*</nav>)', r'\1\n      </div>\2', new_content, flags=re.DOTALL)
            
    return new_content

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    fixed = fix_navbar(content)
    
    if fixed != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed)
        print(f"Fixed {file_path}")
    else:
        print(f"Skipped {file_path} (already correct or pattern not found)")
