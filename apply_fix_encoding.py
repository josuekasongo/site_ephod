import os
import re

# Comprehensive map of corrupted patterns to correct French strings
# Order by length (descending) to avoid partial matches
REPLACEMENTS = [
    ('identit\uFFFD', 'identité'),
    ('Strat\uFFFDgie', 'Stratégie'),
    ('strat\uFFFDgique', 'stratégique'),
    ('strat\uFFFDgiques', 'stratégiques'),
    ('\uFFFDtudes', 'Études'),
    ('\uFFFDvaluations', 'Évaluations'),
    ('valuations', 'évaluations'),
    ('ralisation', 'réalisation'),
    ('ralisations', 'réalisations'),
    ('\uFFFDquipe', 'équipe'),
    ('quipe', 'équipe'),
    ('d\uFFFDdi\uFFFDs', 'dédiés'),
    ('dedies', 'dédiés'),
    ('num\uFFFDrique', 'numérique'),
    ('op\uFFFDrationnelle', 'opérationnelle'),
    ('rf\uFFFDrentiels', 'référentiels'),
    ('p\uFFFDrennes', 'pérennes'),
    ('in\uFFFDgale', 'inégalée'),
    ('op\uFFFDrations', 'opérations'),
    ('g\uFFFDrants', 'gérants'),
    ('conformit\uFFFD', 'conformité'),
    ('conformit', 'conformité'),
    ('Pr\u00eat \uFFFD', 'Prêt à'),
    ('d\uFFFDfi', 'défi'),
    ('pluridisciplinaire \uFFFD', 'pluridisciplinaire à'),
    (' \uFFFD ', ' à '),
    ('d\uFFFDs', 'dès'),
    ('b\uFFFDn\uFFFDficiaires', 'bénéficiaires'),
    ('qualit\uFFFD', 'qualité'),
    ('donn\uFFFDes', 'données'),
    ('r\uFFFDunion', 'réunion'),
    ('r\uFFFDseau', 'réseau'),
    ('m\uFFFDthodes', 'méthodes'),
    ('capacit\uFFFDs', 'capacités'),
    ('Int\uFFFDgrit\uFFFD', 'Intégrité'),
    ('Tol\uFFFDrance', 'Tolérance'),
    ('z\uFFFDro', 'zéro'),
    ('mati\uFFFDre', 'matière'),
    ('r\uFFFDussite', 'réussite'),
    ('G\uFFFDrante', 'Gérante'),
    ('G\uFFFDrant', 'Gérant'),
    ('D\uFFFDploiements', 'Déploiements'),
    ('Cin\uFFFDmatiques', 'Cinématiques'),
    ('Imp\uFFFDt', 'Impôt'),
    ('N\uFFFD', 'N°'),
    ('rǸalisations', 'réalisations'),
    ('stratǸgie', 'stratégie'),
    ('stratǸgiques', 'stratégiques'),
    ('Ǹcoute', 'écoute'),
    ('\uFFFD', 'é'), # Catch-all 
    ('Ǹ', 'é'),
    ('â€”', '—'),
]

HTML_FILES = [
    'index.html', 'about.html', 'services.html', 'portfolio.html', 
    'careers.html', 'ongoing.html', 'contact.html'
]

def fix_file(filename):
    if not os.path.exists(filename):
        return

    print(f"Processing {filename}...")
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filename, 'r', encoding='iso-8859-1') as f:
            content = f.read()

    original_content = content

    # Apply replacements in order
    for bad, good in REPLACEMENTS:
        content = content.replace(bad, good)
    
    # Fix corrupted Google Fonts URLs
    content = content.replace('fonts.googleapis.com/css2\u2014family', 'fonts.googleapis.com/css2?family')
    content = content.replace('fonts.googleapis.com/css2â€”family', 'fonts.googleapis.com/css2?family')
    content = content.replace('fonts.googleapis.com/css2—family', 'fonts.googleapis.com/css2?family')

    # Cleanup double accents and artifacts from multiple runs
    while 'éé' in content: content = content.replace('éé', 'é')
    while 'ÉÉ' in content: content = content.replace('ÉÉ', 'É')
    while 'eé' in content: content = content.replace('eé', 'é')
    while 'EÉ' in content: content = content.replace('EÉ', 'É')
    while 'eé' in content: content = content.replace('eé', 'é')
    
    # Specific cleanup for the "études & évaluations" double accent seen
    content = content.replace('éévaluations', 'évaluations')
    content = content.replace('ÉÉvaluations', 'Évaluations')

    if content != original_content:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  Fixed {filename}")
    else:
        print(f"  No changes needed.")

if __name__ == "__main__":
    for html_file in HTML_FILES:
        fix_file(html_file)
    print("All files processed.")
