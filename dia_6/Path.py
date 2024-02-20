
from pathlib import Path

guia = Path('Barcelona', 'Safgrada_familia')
print(guia)

# ruta absoluta

base = Path.home()
print(base)

guia = Path(base, 'europa', 'espania')
print(guia)

base = Path.home()

guia = Path(base, 'europa', 'espania', Path('barcelona', 'sagrada_familia.py'))
print(guia)

