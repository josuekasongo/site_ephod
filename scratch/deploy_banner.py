import os

def deploy_universal_banner():
    target_files = [
        'about.html', 'services.html', 'portfolio.html', 
        'ongoing.html', 'careers.html', 'contact.html'
    ]
    
    # The new Universal Refined Banner Structure
    banner_html = """
  <!-- ========== BANNER (REFINED ELITE) ========== -->
  <section class="noir-rouge-elite-banner">
    <div class="orb-1"></div>
    <div class="orb-2"></div>
    <div class="container banner-content-elite typewriter-group">
      <div class="brand-identity-stack chained">
        <div class="brand-main">EPHOD</div>
        <div class="brand-sub">CONSULTING</div>
        <div class="brand-accent-line"></div>
      </div>
      <div class="institutional-manifesto chained">
        <p data-i18n="about.banner_desc">EPHOD Consulting s'appuie sur une expertise multidisciplinaire pour accompagner ses partenaires dans la réalisation d'impacts durables. Notre méthodologie rigoureuse, alignée sur les meilleurs standards mondiaux, garantit une performance optimale même en contextes fragiles.</p>
      </div>
    </div>
  </section>
"""

    for filename in target_files:
        path = os.path.join('d:\\EPHOD', filename)
        if not os.path.exists(path):
            continue
            
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the standard banner markers or the noir-rouge block if already there
        # We look for section with class noir-rouge-elite-banner or srv-banner-animated or banner section comments
        
        # Pattern matching for replacement
        new_content = content
        
        # Case 1: Replace old srv-banner-animated or noir-rouge blocks
        patterns = [
            r'<!-- ========== BANNER ========== -->\s*<section class="srv-banner-animated.*?</section>',
            r'<!-- ========== BANNER ========== -->\s*<section class="noir-rouge-elite-banner.*?</section>',
            r'<!-- ========== BANNER \(REFINED ELITE\) ========== -->\s*<section class="noir-rouge-elite-banner.*?</section>'
        ]
        
        import re
        for pattern in patterns:
            if re.search(pattern, new_content, re.DOTALL):
                new_content = re.sub(pattern, banner_html.strip(), new_content, flags=re.DOTALL)
                break
        
        if content != new_content:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Deployed banner to {filename}")
        else:
            print(f"Could not find banner marker in {filename}")

if __name__ == "__main__":
    deploy_universal_banner()
