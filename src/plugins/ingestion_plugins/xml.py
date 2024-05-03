import logging
import lxml.etree as ET
from plugins.base_plugin import BaseIngestor

logger = logging.getLogger(__name__)

class XmlIngestor(BaseIngestor):
    def __init__(self, file_path, metadata):
        super().__init__(file_path)
        self.metadata = metadata

    def ingest(self):
        try:
            tree = ET.parse(self.file_path)
            return {
                "root": tree.getroot(),
                "metadata": self.metadata
            }
        except Exception as e:
            logger.error(f"Failed to ingest XML file at {self.file_path}. Error: {str(e)}. Ensure the XML is well-formed.")
            raise
