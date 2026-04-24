import os

def fix_active_nav():
    for root, dirs, files in os.walk('d:\\EPHOD'):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                new_content = content.replace('class="nav-link active"', 'class="nav-link"')
                
                if content != new_content:
                    with open(path, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Fixed {file}")

if __name__ == "__main__":
    fix_active_nav()
