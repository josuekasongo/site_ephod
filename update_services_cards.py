import re

file_path = 'services.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# adding card-rouge-noir to any card missing it
html = html.replace('class="service-card text-center h-100 pillar-card"', 'class="service-card text-center h-100 pillar-card card-rouge-noir"')

def replace_desc(match):
    i18n_key = match.group(1)
    inner = match.group(2)
    clean_text = ' '.join(inner.split())
    # avoid escaping double quotes by using &quot; if any
    clean_text = clean_text.replace('"', '&quot;')
    return f'<p class="service-desc typewriter-scroll" data-i18n="{i18n_key}" data-text="{clean_text}" data-speed="15">{inner}</p>'

html = re.sub(r'<p\s+class="service-desc"\s+data-i18n="(srv\.s\d_desc)">([\s\S]*?)</p>', replace_desc, html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print("services.html modified successfully")
