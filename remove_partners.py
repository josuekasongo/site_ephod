import re

files = ['about.html', 'services.html', 'careers.html', 'contact.html', 'portfolio.html', 'ongoing.html']

for fname in files:
    for enc in ['utf-8', 'utf-8-sig', 'latin-1']:
        try:
            with open(fname, 'r', encoding=enc) as f:
                content = f.read()
            break
        except UnicodeDecodeError:
            continue
    
    # Remove the partners section block
    cleaned = re.sub(
        r'\s*<!-- =+ PARTNERS[^>]*=+ -->\s*<section class="partners-section".*?</section>',
        '',
        content,
        flags=re.DOTALL
    )
    
    if cleaned != content:
        with open(fname, 'w', encoding=enc) as f:
            f.write(cleaned)
        print(f'OK: {fname}')
    else:
        print(f'NON TROUVE: {fname}')
