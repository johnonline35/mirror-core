import logging
from plugins.base_plugin import BaseIngestor

logger = logging.getLogger(__name__)

class TxtIngestor(BaseIngestor):
    def __init__(self, file_path, metadata):
        super().__init__(file_path)
        self.metadata = metadata

    def ingest(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                text = file.readlines()
            return {
                "text": text,
                "metadata": self.metadata
            }
        except Exception as e:
            logger.error(f"Failed to ingest TXT file at {self.file_path}. Error: {str(e)}. Check file permissions and encoding.")
            raise
