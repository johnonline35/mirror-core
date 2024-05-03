import logging
import orjson
from plugins.base_plugin import BaseIngestor

logger = logging.getLogger(__name__)

class JsonIngestor(BaseIngestor):
    def __init__(self, file_path, metadata):
        super().__init__(file_path)
        self.metadata = metadata

    def ingest(self):
        try:
            with open(self.file_path, 'rb') as jsonfile:
                return {
                    "data": orjson.loads(jsonfile.read()),
                    "metadata": self.metadata
                }
        except Exception as e:
            logger.error(f"Failed to ingest JSON file at {self.file_path}. Error: {str(e)}. Check that the file is valid JSON.")
            raise
