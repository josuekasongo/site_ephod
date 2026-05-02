import os

css_path = r"d:\EPHOD\css\style.css"

overrides = """
/* Force inline styles and specific components to obey themes */
body.theme-dark span[style*="color: #111"], body.theme-black span[style*="color: #111"],
body.theme-dark span[style*="color: #111111"], body.theme-black span[style*="color: #111111"],
body.theme-dark span[style*="color: #2c2c2c"], body.theme-black span[style*="color: #2c2c2c"],
body.theme-dark p[style*="color: #2c2c2c"], body.theme-black p[style*="color: #2c2c2c"],
body.theme-dark h1[style], body.theme-black h1[style],
body.theme-dark h2[style], body.theme-black h2[style],
body.theme-dark h3[style], body.theme-black h3[style],
body.theme-dark h4[style], body.theme-black h4[style],
body.theme-dark h5[style], body.theme-black h5[style] {
  color: var(--text-main) !important;
}

body.theme-dark .card *, body.theme-black .card * {
  color: inherit !important;
}
body.theme-dark .card p[style*="color"], body.theme-black .card p[style*="color"] {
  color: var(--text-main) !important;
}
body.theme-dark .nav-dropdown, body.theme-black .nav-dropdown {
  background: var(--bg-surface) !important;
  border-color: var(--border-color) !important;
}
body.theme-dark .nav-dropdown-item, body.theme-black .nav-dropdown-item {
  color: var(--text-main) !important;
}
body.theme-dark .nav-dropdown-item:hover, body.theme-black .nav-dropdown-item:hover {
  background: var(--bg-surface-2) !important;
  color: var(--primary) !important;
}
body.theme-dark .standard-card-elite, body.theme-black .standard-card-elite {
  background: var(--bg-surface) !important;
}
body.theme-dark .hero-slide-frame, body.theme-black .hero-slide-frame {
  background: rgba(0,0,0,0.6) !important;
}
body.theme-dark .portfolio-card, body.theme-black .portfolio-card {
  background: var(--bg-surface) !important;
}
body.theme-dark .stat-box, body.theme-black .stat-box {
  background: var(--bg-surface) !important;
}
body.theme-dark .bg-light, body.theme-black .bg-light {
  background-color: var(--bg-surface-2) !important;
}
"""

with open(css_path, "a", encoding="utf-8") as f:
    f.write(overrides)

print("CSS overrides appended successfully!")
