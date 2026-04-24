import os

def fix_fr_key():
    f = 'js/lang.js'
    with open(f, 'r', encoding='utf-8') as fr:
        c = fr.read()
    
    # Correcting the missing French key due to case sensitivity
    if '"srv.modal_close": "Fermer"' not in c:
        # Check for both cases just in case
        c = c.replace('"srv.modal_value": "Valeur Ajoutée"', '"srv.modal_value": "Valeur Ajoutée",\n        "srv.modal_close": "Fermer"')
        c = c.replace('"srv.modal_value": "Valeur ajoutée"', '"srv.modal_value": "Valeur ajoutée",\n        "srv.modal_close": "Fermer"')
        
        with open(f, 'w', encoding='utf-8') as fw:
            fw.write(c)
        print("Fixed French key for srv.modal_close")
    else:
        print("Key already exists")

if __name__ == "__main__":
    fix_fr_key()
