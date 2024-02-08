import unicodedata
import pyperclip

def remover_acentos(texto):
    texto_sem_acentos = ''.join(c for c in unicodedata.normalize('NFD', texto)
                                if unicodedata.category(c) != 'Mn')
    return texto_sem_acentos

texto_com_acentos = "Olá, mundo! Está é uma frase com acentuação."
texto_sem_acentos = remover_acentos(texto_com_acentos)

# Copiar o texto para a área de transferência
pyperclip.copy(texto_sem_acentos)

print(texto_sem_acentos)
