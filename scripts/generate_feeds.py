import os
from single import RaiParser

SCRIPT_PATH = os.path.abspath("scripts/single.py")
PROGRAMS = {
    
    "ungiornodapecora": "https://www.raiplaysound.it/programmi/ungiornodapecora",
    
    
    "gr1": "https://www.raiplaysound.it/programmi/gr1",
    "gr2": "https://www.raiplaysound.it/programmi/gr2",
    "gr3": "https://www.raiplaysound.it/programmi/gr3",
    
    
    "lapennicanza": "https://www.raiplaysound.it/programmi/lapennicanza",
    "caterpillar": "https://www.raiplaysound.it/programmi/radio2caterpillar",
    "ilruggitodelconiglio": "https://www.raiplaysound.it/programmi/ilruggitodelconiglio",
    "rock and roll circus": "https://www.raiplaysound.it/programmi/rockandrollcircus",
    
}
for name, url in PROGRAMS.items():
    print(f"Generazione feed per {name}...")
    try:
        rai_parser = RaiParser(url, ".")
        rai_parser.process()
        original_file = f"{name}.xml"
        if not os.path.exists(original_file):
            print(f"Errore: Il file {original_file} non è stato generato correttamente!")
            continue
        new_file = f"feed_{name}.xml"
        os.rename(original_file, new_file)
        print(f"Feed XML salvato correttamente: {new_file}")
    except Exception as e:
        print(f"Errore generico per {name}: {e}")
