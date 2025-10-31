from json import JSONDecodeError
import json

def leer(ARCHIVO):
    try:
        with open(ARCHIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, JSONDecodeError):
        return []

def escribir(nuevo, ARCHIVO):
    with open(ARCHIVO, "w", encoding="utf-8") as f:
        json.dump(nuevo, f, ensure_ascii=False, indent=4)