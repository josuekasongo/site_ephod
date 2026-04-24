import os
import re

files = ["index.html", "about.html", "services.html", "portfolio.html", "careers.html", "ongoing.html", "contact.html"]

navbar_item = '          <li class="nav-item">\n            <a class="nav-link" href="contact.html"><span data-i18n="footer.contact_title">Contact</span></a>\n          </li>'

footer_item = '            <li><a href="contact.html" data-i18n="footer.contact_title">Contact</a></li>'

for filename in files:
    if not os.path.exists(filename):
        print(f"File {filename} not found, skipping.")
        continue
        
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update Navbar
    # Search for the careers nav item closure to append Contact after it
    if 'href="contact.html"' not in content:
         # Find the end of the careers li or the last li before the </ul>
         nav_pattern = r'(<li class="nav-item has-dropdown">\s*<a class="nav-link" href="careers.html">.*?</li>)'
         if re.search(nav_pattern, content, re.DOTALL):
             content = re.sub(nav_pattern, r'\1\n' + navbar_item, content, flags=re.DOTALL)
         else:
             # Fallback: find </ul> and insert before
             content = content.replace('</ul>', navbar_item + '\n        </ul>', 1)

    # Update Footer
    if footer_item not in content:
        # Find the footer navigation list
        # It usually follows <h6 ... data-i18n="footer.nav_title">Navigation</h6>
        footer_pattern = r'(<h6 class="footer-heading" data-i18n="footer.nav_title">Navigation</h6>\s*<ul class="footer-links">.*?)(</ul>)'
        if re.search(footer_pattern, content, re.DOTALL):
            content = re.sub(footer_pattern, r'\1' + footer_item + r'\n          \2', content, flags=re.DOTALL)

    # Update CTA buttons pointing to mailto
    content = content.replace('href="mailto:contact@ephode-consulting.com"', 'href="contact.html"')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filename}")
