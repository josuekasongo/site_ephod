import os
import re

# The new footer content
new_footer = '''  <!-- ========== RMDA INSPIRED FOOTER ========== -->
  <footer class="main-footer">
    <div class="container">
      <div class="row g-5">
        <!-- Brand & Vision -->
        <div class="col-lg-4">
          <a class="logo-wrap mb-4" href="index.html" style="filter: brightness(0) invert(1);">
            <div class="logo-top-row">
              <div class="logo-icon"><span>E</span></div>
              <div class="logo-text-wrap"><span>EPHOD</span></div>
            </div>
            <div class="logo-consulting" style="color:#fff !important;">
              <span>C</span><span>O</span><span>N</span><span>S</span><span>U</span><span>L</span><span>T</span><span>I</span><span>N</span><span>G</span>
            </div>
          </a>
          <p class="footer-contact-info mt-4" data-i18n="footer.desc">
            Expertise internationale et ancrage local pour un impact durable en Afrique Centrale et de l'Est.
          </p>
        </div>

        <!-- Navigation -->
        <div class="col-sm-6 col-lg-2">
          <h6 class="footer-heading" data-i18n="footer.nav_title">Navigation</h6>
          <ul class="footer-links">
            <li><a href="index.html" data-i18n="nav.home">Accueil</a></li>
            <li><a href="about.html" data-i18n="nav.about">Qui sommes-nous</a></li>
            <li><a href="services.html" data-i18n="nav.services">Nos services</a></li>
            <li><a href="portfolio.html" data-i18n="nav.portfolio">Nos réalisations</a></li>
            <li><a href="contact.html">Contact</a></li>
          </ul>
        </div>

        <!-- Offices -->
        <div class="col-lg-6">
          <h6 class="footer-heading">Bureaux & Contact</h6>
          <div class="row footer-contact-info">
            <div class="col-md-6 mb-4">
              <strong>Kinshasa (Siège)</strong>
              Q. Ma Campagne, Av. Kapaya N°03<br>
              Commune de Ngaliema
            </div>
            <div class="col-md-6 mb-4">
              <strong>Goma</strong>
              Q. Kyeshero, Av. Kituku N°13
            </div>
            <div class="col-md-6">
              <strong>Beni</strong>
              RN4, Face ENERA, Entrée KVG<br>
              N°6, Av. Opienge, Q. Mabakanga
            </div>
            <div class="col-md-6">
              <strong>Contact Direct</strong>
              +243 830517419 | +243 975418640<br>
              direction@ephodconsulting.org
            </div>
          </div>
        </div>
      </div>

      <!-- Legal & Footer Bottom -->
      <div class="footer-bottom-rmda">
        <div class="legal-badges-row">
          <span class="legal-tag-rmda">RCCM: CD/KNG/RCCM/25-B-03958</span>
          <span class="legal-tag-rmda">ID NAT: 01-H5300-N88322C</span>
          <span class="legal-tag-rmda">UNGM: 1175536</span>
          <span class="legal-tag-rmda">NIF: A2559012X</span>
          <span class="legal-tag-rmda">INPP: 166976,00</span>
        </div>
        <div class="footer-copyright">
          &copy; 2026 EPHOD Consulting SARL. <span data-i18n="footer.rights">Tous droits réservés.</span>
        </div>
      </div>
    </div>
  </footer>'''

files = ['about.html', 'careers.html', 'contact.html', 'ongoing.html', 'portfolio.html', 'services.html']

for f in files:
    if os.path.exists(f):
        try:
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Use regex to find and replace any footer tag
            new_content = re.sub(r'<footer.*?</footer>', new_footer, content, flags=re.DOTALL)
            
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'Successfully updated {f}')
        except Exception as e:
            print(f'Error updating {f}: {e}')
