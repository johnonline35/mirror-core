import logging
import pandas as pd
from plugins.base_plugin import BaseIngestor

logger = logging.getLogger(__name__)

class CsvIngestor(BaseIngestor):
    def __init__(self, file_path, metadata):
        super().__init__(file_path)
        self.metadata = metadata

    def ingest(self):
        try:
            return {
                "data": pd.read_csv(self.file_path),
                "metadata": self.metadata
            }
        except Exception as e:
            logger.error(f"Failed to ingest CSV file at {self.file_path}. Error: {str(e)}. Ensure the file is correctly formatted.")
            raise
