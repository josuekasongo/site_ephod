import os

css_path = r"d:\EPHOD\css\style.css"

overrides = """
/* ==========================================================================
   DARK & BLACK MODE SAFE OVERLAYS
   These rules only apply when body has .theme-dark or .theme-black class.
   They override the original styles safely without modifying the default.
   ========================================================================== */

body.theme-dark {
  background: #121212 !important;
  color: #e0e0e0 !important;
  transition: background-color 0.3s ease, color 0.3s ease;
}
body.theme-black {
  background: #000000 !important;
  color: #ffffff !important;
  transition: background-color 0.3s ease, color 0.3s ease;
}

/* Force text colors on hardcoded inline styles */
body.theme-dark span[style*="color: #111"], body.theme-black span[style*="color: #111"],
body.theme-dark span[style*="color: #111111"], body.theme-black span[style*="color: #111111"],
body.theme-dark span[style*="color: #2c2c2c"], body.theme-black span[style*="color: #2c2c2c"],
body.theme-dark p[style*="color: #2c2c2c"], body.theme-black p[style*="color: #2c2c2c"],
body.theme-dark h1[style], body.theme-black h1[style],
body.theme-dark h2[style], body.theme-black h2[style],
body.theme-dark h3[style], body.theme-black h3[style],
body.theme-dark h4[style], body.theme-black h4[style],
body.theme-dark h5[style], body.theme-black h5[style] {
  color: inherit !important;
}

/* Navbar Overrides */
body.theme-dark .navbar {
  background: rgba(18, 18, 18, 0.9) !important;
}
body.theme-black .navbar {
  background: rgba(0, 0, 0, 0.95) !important;
}

/* Logo CSS Text Overrides */
body.theme-dark .logo-icon-box, body.theme-black .logo-icon-box {
  background: #252525 !important;
}
body.theme-dark .logo-sub-text, body.theme-black .logo-sub-text {
  color: #e0e0e0 !important;
}

/* Cards Overrides */
body.theme-dark .service-card-elite {
  background: #1e1e1e !important;
  border-color: rgba(255,255,255,0.1) !important;
}
body.theme-black .service-card-elite {
  background: #0a0a0a !important;
  border-color: rgba(140,19,56,0.2) !important;
}

body.theme-dark .card, body.theme-black .card {
  background-color: #1e1e1e !important;
  border-color: rgba(255,255,255,0.1) !important;
}
body.theme-dark .card *, body.theme-black .card * {
  color: inherit !important;
}

/* bg-light & section overrides */
body.theme-dark .bg-light { background-color: #181818 !important; }
body.theme-black .bg-light { background-color: #050505 !important; }

body.theme-dark .ephod-partners-section[style] { background-color: #181818 !important; }
body.theme-black .ephod-partners-section[style] { background-color: #050505 !important; }

/* Dropdown Overrides */
body.theme-dark .nav-dropdown, body.theme-black .nav-dropdown {
  background: #1e1e1e !important;
  border-color: rgba(255,255,255,0.1) !important;
}
body.theme-dark .nav-dropdown-item, body.theme-black .nav-dropdown-item {
  color: #e0e0e0 !important;
}
body.theme-dark .nav-dropdown-item:hover, body.theme-black .nav-dropdown-item:hover {
  background: #252525 !important;
  color: var(--primary) !important;
}

/* Modals Overrides */
body.theme-dark .modal-content, body.theme-black .modal-content {
  background-color: #1e1e1e !important;
  color: #e0e0e0 !important;
}

/* Other specific elements */
body.theme-dark .standard-card-elite, body.theme-dark .portfolio-card, body.theme-dark .stat-box {
  background: #1e1e1e !important;
}
body.theme-black .standard-card-elite, body.theme-black .portfolio-card, body.theme-black .stat-box {
  background: #0a0a0a !important;
}
body.theme-dark .hero-slide-frame, body.theme-black .hero-slide-frame {
  background: rgba(0,0,0,0.6) !important;
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(overrides)

print("Safe CSS overlays appended successfully!")
