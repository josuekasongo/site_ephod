import glob
import re

html_files = glob.glob('*.html')

search_toggler = '''      <button class="navbar-toggler border-0 shadow-none" type="button" data-bs-toggle="collapse"
        data-bs-target="#navMenu" aria-controls="navMenu" aria-expanded="false" aria-label="Menu">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navMenu">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-lg-center">'''

replace_toggler = '''      <div class="d-flex align-items-center gap-2 order-lg-last ms-auto">
        <button class="lang-btn" onclick="toggleLanguage()" id="langBtn"><i class="bi bi-globe"></i><span id="lang-toggle-text">FR</span></button>
        <button class="lang-btn theme-toggle-btn" onclick="cycleTheme()" id="themeBtn" title="Changer le thème" style="padding: 10px 15px;"><i class="bi bi-moon-stars" id="themeIcon"></i></button>
        
        <button class="navbar-toggler border-0 shadow-none ms-1 px-2" type="button" data-bs-toggle="collapse"
          data-bs-target="#navMenu" aria-controls="navMenu" aria-expanded="false" aria-label="Menu">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
      <div class="collapse navbar-collapse" id="navMenu">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-lg-center me-lg-3">'''

search_bottom = '''        </ul>
        <div class="d-flex align-items-center gap-2">
          <button class="lang-btn" onclick="toggleLanguage()" id="langBtn"><i class="bi bi-globe"></i><span id="lang-toggle-text">FR</span></button>
          <button class="lang-btn theme-toggle-btn" onclick="cycleTheme()" id="themeBtn" title="Changer le thème" style="padding: 10px 15px;"><i class="bi bi-moon-stars" id="themeIcon"></i></button>
        </div>
      </div>'''

replace_bottom = '''        </ul>
      </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if the file needs updating
    if search_toggler in content and search_bottom in content:
        content = content.replace(search_toggler, replace_toggler)
        content = content.replace(search_bottom, replace_bottom)
        
        # Also bump version to force cache refresh
        content = re.sub(r'\?v=7\.3', '?v=7.4', content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed mobile layout in {file}")
    else:
        print(f"Skipped {file} (pattern not found or already updated)")
