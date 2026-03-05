"""
main.py - Script de entrada para testar o DataValidator no Debian.
"""

import logging
from src.validator import DataValidator

# Configura o logging para mostrar as mensagens no terminal
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s",
)

if __name__ == "__main__":
    # Caminho do arquivo que vamos testar (dentro da pasta data)
    FILE_PATH = "data/teste.xlsx"

    try:
        # Instancia o validador
        validator = DataValidator(FILE_PATH)

        # Executa a verificação de colunas
        result = validator.check_columns()

        print("-" * 40)
        if result:
            print("✓ SUCESSO: O arquivo contém as colunas ID e Data!")
        else:
            print("✗ ERRO: O arquivo está incompleto.")
        print("-" * 40)
        
    except FileNotFoundError as e:
        logging.error(e)
    except Exception as e:
        logging.error("Erro inesperado: %s", e)