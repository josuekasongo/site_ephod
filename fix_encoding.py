import re

# Correspondances des caractères mal encodés (mojibake latin-1 → utf-8)
replacements = {
    'Ã©': 'é', 'Ã¨': 'è', 'Ã ': 'à', 'Ã¢': 'â', 'Ã®': 'î', 'Ã´': 'ô',
    'Ã»': 'û', 'Ã§': 'ç', 'Ã«': 'ë', 'Ã¹': 'ù', 'Ã¼': 'ü', 'Ã¯': 'ï',
    'Ã‰': 'É', 'Ã€': 'À', 'Ã‚': 'Â', 'Ã‡': 'Ç', 'Ã‹': 'Ë', 'ÃŽ': 'Î',
    'Ã"': 'Ô', 'Ã™': 'Ù', 'Ã›': 'Û', 'Å"': 'œ', 'Å½': 'Ž', 'Â°': '°',
    'Â«': '«', 'Â»': '»', 'Ã¦': 'æ', 'Å\x93': 'œ', '\u01f8': 'é',
    'ǸtÃ': 'été', 'Ǹ': 'é', 'â\x80\x99': "'", 'â€™': "'",
    # Variantes restantes
    'rǸalisation': 'réalisation', 'rǸalisations': 'réalisations',
    'StratǸgie': 'Stratégie', 'stratǸgie': 'stratégie',
    'GǸrante': 'Gérante', 'GǸrant': 'Gérant',
    'OpǸration': 'Opération', 'opǸration': 'opération',
    'ConformitǸ': 'Conformité', 'conformitǸ': 'conformité',
    'TolǸrance': 'Tolérance', 'tolǸrance': 'tolérance',
    'mǸcanisme': 'mécanisme', 'dǸtournement': 'détournement',
    'rǸservǸs': 'réservés', 'innovation et': 'innovation et',
    'N\ufffd': 'N°', 'N\ufffd03': 'N°03', 'N\ufffd06': 'N°06',
    'Imp\ufffd': 'Impôt', '\u00c9thique': 'Éthique',
    '\ufffd%thique': 'Éthique',
}

with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content
for bad, good in replacements.items():
    content = content.replace(bad, good)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)

changes = sum(1 for a, b in zip(original, content) if a != b)
print(f'OK - {len(original) - len(content)} caracteres corriges')
