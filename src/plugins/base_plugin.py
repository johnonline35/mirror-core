# Base class for all plugins, Template method pattern

from abc import ABC, abstractmethod
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)  

class BaseIngestor(ABC):
    def __init__(self, file_path):
        self.file_path = file_path
        logger.info(f"Initialized BaseIngestor with file path: {file_path}")

    @abstractmethod
    def ingest(self):
        """Method to ingest data from a file."""
        pass
