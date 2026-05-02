import os
import glob

html_files = glob.glob('*.html')

search_str = '<button class="lang-btn" onclick="toggleLanguage()" id="langBtn"><i class="bi bi-globe"></i><span id="lang-toggle-text">FR</span></button>'

replace_str = '''<div class="d-flex align-items-center gap-2">
          <button class="lang-btn" onclick="toggleLanguage()" id="langBtn"><i class="bi bi-globe"></i><span id="lang-toggle-text">FR</span></button>
          <button class="lang-btn theme-toggle-btn" onclick="cycleTheme()" id="themeBtn" title="Changer le thème" style="padding: 10px 15px;"><i class="bi bi-moon-stars" id="themeIcon"></i></button>
        </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if search_str in content:
        content = content.replace(search_str, replace_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
    else:
        print(f"Could not find exact string in {file}, checking for variations...")
        # Fallback if there are spaces
        if 'id="langBtn"' in content and 'toggleLanguage()' in content:
            print(f"  Found ID in {file}, but string mismatch.")
