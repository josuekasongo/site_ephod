# -*- coding: utf-8 -*-
import codecs

filename = r'd:\EPHOD\css\style.css'
with codecs.open(filename, 'a', encoding='utf-8') as f:
    f.write("\n\n/* High-Impact Automatic Color Cycle */\n")
    f.write("@keyframes cardBgCycle {\n")
    f.write("  0% { background: #000000; }\n")
    f.write("  50% { background: #8C1338; }\n")
    f.write("  100% { background: #000000; }\n")
    f.write("}\n")
    
    f.write(".service-card {\n")
    # We use animation on background-color/background to be extremely obvious
    f.write("  animation: cardBgCycle 12s ease-in-out infinite !important;\n")
    f.write("  border: 1px solid rgba(140, 19, 56, 0.4) !important;\n")
    f.write("  color: white !important;\n")
    f.write("}\n")
    
    # Also animate the border to match the cycle
    f.write("@keyframes borderRadiusPulse {\n")
    f.write("  0%, 100% { border-color: rgba(140, 19, 56, 0.4); }\n")
    f.write("  50% { border-color: #ffffff; }\n")
    f.write("}\n")
    f.write(".service-card { animation: cardBgCycle 12s ease-in-out infinite, borderRadiusPulse 6s infinite !important; }\n")

    # Ensure text stays readable by adding a subtle permanent dark overlay for the content if needed
    # but the user wants the WHOLE card to change color.
print('Done!')
