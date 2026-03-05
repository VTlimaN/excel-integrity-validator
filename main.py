import logging
from src.validator import DataValidator

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s",
)

if __name__ == "__main__":
    FILE_PATH = "data/teste.xlsx"
    try:
        validator = DataValidator(FILE_PATH)
        result = validator.check_columns()
        print("-" * 40)
        if result:
            print("✓ SUCESSO: O arquivo contém as colunas ID e Data!")
        else:
            print("✗ ERRO: O arquivo está incompleto.")
        print("-" * 40)
    except Exception as e:
        logging.error(e)
