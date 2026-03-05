"""
validator.py - Lógica central de validação do excel-integrity-validator.
"""

import logging
from pathlib import Path
import pandas as pd

# Logger de nível de módulo: permite rastrear o que acontece no código
logger = logging.getLogger(__name__)

# Colunas que o arquivo PRECISA ter para ser considerado válido
REQUIRED_COLUMNS: tuple[str, ...] = ("ID", "Data")

class DataValidator:
    """Valida a integridade estrutural de arquivos Excel."""

    def __init__(self, file_path: str | Path) -> None:
        """
        Inicializa o validador com o arquivo Excel alvo.
        """
        self.file_path = Path(file_path)

        if not self.file_path.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {self.file_path}")

        self._df: pd.DataFrame | None = None
        logger.info("DataValidator inicializado para '%s'.", self.file_path)

    def _load(self) -> pd.DataFrame:
        """Carrega o DataFrame de forma lazy (apenas quando necessário)."""
        if self._df is None:
            self._df = pd.read_excel(self.file_path)
        return self._df

    def check_columns(self) -> bool:
        """
        Verifica se as colunas 'ID' e 'Data' estão presentes.
        """
        df = self._load()
        all_present = True

        for column in REQUIRED_COLUMNS:
            if column in df.columns:
                logger.info("Coluna '%s' encontrada.", column)
            else:
                logger.error("Coluna '%s' está ausente!", column)
                all_present = False

        return all_present