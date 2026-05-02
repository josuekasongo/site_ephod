import glob
import re

html_files = glob.glob('*.html')

search_top = '''      <div class="d-flex align-items-center gap-2 order-lg-last ms-auto">
        <button class="lang-btn" onclick="toggleLanguage()" id="langBtn"><i class="bi bi-globe"></i><span id="lang-toggle-text">FR</span></button>
        <button class="lang-btn theme-toggle-btn" onclick="cycleTheme()" id="themeBtn" title="Changer le thème" style="padding: 10px 15px;"><i class="bi bi-moon-stars" id="themeIcon"></i></button>
        
        <button class="navbar-toggler border-0 shadow-none ms-1 px-2" type="button" data-bs-toggle="collapse"
          data-bs-target="#navMenu" aria-controls="navMenu" aria-expanded="false" aria-label="Menu">
          <span class="navbar-toggler-icon"></span>
        </button>
      </div>
      <div class="collapse navbar-collapse" id="navMenu">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-lg-center me-lg-3">'''

replace_top = '''      <button class="navbar-toggler border-0 shadow-none ms-auto" type="button" data-bs-toggle="collapse"
        data-bs-target="#navMenu" aria-controls="navMenu" aria-expanded="false" aria-label="Menu">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navMenu">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0 align-items-lg-center">'''

search_bottom = '''        </ul>
      </div>'''

replace_bottom = '''        </ul>
        <div class="d-flex align-items-center gap-2 mt-3 mt-lg-0 mb-3 mb-lg-0">
          <button class="lang-btn m-0" onclick="toggleLanguage()" id="langBtn"><i class="bi bi-globe"></i><span id="lang-toggle-text">FR</span></button>
          <button class="lang-btn m-0 theme-toggle-btn" onclick="cycleTheme()" id="themeBtn" title="Changer le thème" style="padding: 10px 15px;"><i class="bi bi-moon-stars" id="themeIcon"></i></button>
        </div>
      </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if search_top in content:
        content = content.replace(search_top, replace_top)
        
        # Replace only the FIRST occurrence of search_bottom after navMenu
        # Since search_bottom is just `</ul>\n      </div>`, we need to be careful.
        # But wait, the previous structure was exactly that for the end of the navMenu.
        # Let's use regex to replace the specific closing tags of navMenu.
        
        # We know navMenu ends with </ul>\n      </div> right before </nav>
        # Let's just do a string replace, but it might match footer lists if they look like that.
        # Let's do a more targeted replace:
        content = re.sub(r'        </ul>\n      </div>\n    </div>\n  </nav>', 
                         r'        </ul>\n        <div class="d-flex align-items-center gap-2 mt-3 mt-lg-0 mb-3 mb-lg-0">\n          <button class="lang-btn m-0" onclick="toggleLanguage()" id="langBtn"><i class="bi bi-globe"></i><span id="lang-toggle-text">FR</span></button>\n          <button class="lang-btn m-0 theme-toggle-btn" onclick="cycleTheme()" id="themeBtn" title="Changer le thème" style="padding: 10px 15px;"><i class="bi bi-moon-stars" id="themeIcon"></i></button>\n        </div>\n      </div>\n    </div>\n  </nav>', 
                         content)
                         
        # Bump version to 7.5
        content = re.sub(r'\?v=7\.4', '?v=7.5', content)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Reverted mobile layout in {file}")
    else:
        print(f"Skipped {file}")
