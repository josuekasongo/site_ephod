import os
import re

# The EXACT RMDA footer structure based on the image
exact_footer = '''<!-- ========== RMDA GROUP EXACT FOOTER ========== -->
<footer class="main-footer">
    <div class="container">
        <div class="row g-5">
            <!-- Left: Brand -->
            <div class="col-lg-4">
                <div class="footer-brand-title">EPHOD</div>
                <div class="footer-brand-sub">CONSULTING</div>
                <p class="footer-brand-desc mt-4" style="font-size: 0.85rem; line-height: 1.6;">
                    <span data-i18n="footer.desc">Cabinet d'expertise humanitaire et de développement.</span><br>
                    <span style="opacity: 0.7;">RCCM: CD/KNG/RCCM/25-B-03958<br>
                    ID NAT: 01-H5300-N88322C | UNGM: 1175536<br>
                    NIF: A2559012X | INPP: 166976,0</span>
                </p>
            </div>

            <!-- Middle: Navigation -->
            <div class="col-lg-2">
                <div class="footer-col-title" data-i18n="footer.nav_title">NAVIGATION</div>
                <ul class="footer-nav-list">
                    <li><a href="index.html" data-i18n="nav.home">Accueil</a></li>
                    <li><a href="about.html" data-i18n="nav.about">Qui sommes-nous</a></li>
                    <li><a href="services.html" data-i18n="nav.services">Nos services</a></li>
                    <li><a href="portfolio.html" data-i18n="nav.portfolio">Nos réalisations</a></li>
                    <li><a href="contact.html" data-i18n="nav.contact">Contact</a></li>
                </ul>
            </div>

            <!-- Right: Offices & Contact -->
            <div class="col-lg-6">
                <div class="footer-col-title" data-i18n="footer.offices_title">BUREAUX & CONTACT</div>
                <div class="footer-grid-contact">
                    <!-- Kinshasa -->
                    <div class="footer-info-block">
                        <span class="footer-info-label" data-i18n="footer.kin_label">KINSHASA (SIÈGE)</span>
                        <div class="footer-info-value">
                            Q. Ma Campagne, Av. Kapaya N°03<br>
                            Commune de Ngaliema
                        </div>
                    </div>
                    <!-- Goma -->
                    <div class="footer-info-block">
                        <span class="footer-info-label" data-i18n="footer.goma_label">GOMA</span>
                        <div class="footer-info-value">
                            Q. Kyeshero, Av. Kituku N°13
                        </div>
                    </div>
                    <!-- Beni -->
                    <div class="footer-info-block">
                        <span class="footer-info-label" data-i18n="footer.beni_label">BENI</span>
                        <div class="footer-info-value">
                            RN4, Face ENERA, Entrée KVG<br>
                            N°6, Av. Opienge, Q. Mabakanga
                        </div>
                    </div>
                    <!-- Contact Direct -->
                    <div class="footer-info-block">
                        <span class="footer-info-label" data-i18n="footer.direct_label">CONTACT DIRECT</span>
                        <div class="footer-info-value">
                            +243 830517419 | +243 975418640<br>
                            direction@ephodconsulting.org
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <!-- Bottom divider if needed by design -->
        <div class="footer-bottom-divider"></div>
    </div>
</footer>'''

files = ['index.html', 'about.html', 'careers.html', 'contact.html', 'ongoing.html', 'portfolio.html', 'services.html']

for f in files:
    if os.path.exists(f):
        try:
            with open(f, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Replace any existing footer structure
            new_content = re.sub(r'<footer.*?</footer>', exact_footer, content, flags=re.DOTALL)
            
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f'Perfectly updated footer in {f}')
        except Exception as e:
            print(f'Error in {f}: {e}')
