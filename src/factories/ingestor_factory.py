import os
import logging
from typing import Type
from plugins.base_plugin import BaseIngestor
from plugins.ingestion_plugins.csv import CsvIngestor
from plugins.ingestion_plugins.json import JsonIngestor
from plugins.ingestion_plugins.xml import XmlIngestor
from plugins.ingestion_plugins.txt import TxtIngestor
from plugins.ingestion_plugins.pdf import PdfIngestor
from utils.extract_metadata import extract_metadata

logger = logging.getLogger(__name__)

class IngestorFactory:
    file_type_mapping: dict[str, Type[BaseIngestor]] = {
        '.txt': TxtIngestor,
        '.csv': CsvIngestor,
        '.json': JsonIngestor,
        '.xml': XmlIngestor,
        '.pdf': PdfIngestor
    }

    mime_type_mapping: dict[str, Type[BaseIngestor]] = {
        'text/plain': TxtIngestor,
        'text/csv': CsvIngestor,
        'application/json': JsonIngestor,
        'application/xml': XmlIngestor,  
        'application/pdf': PdfIngestor
    }

    @staticmethod
    def create_ingestor(file_path: str) -> BaseIngestor:
        if not os.path.exists(file_path):
            logger.error(f"File does not exist: {file_path}")
            raise FileNotFoundError(f"File not found: {file_path}")

        metadata = extract_metadata(file_path)
        mime_type = metadata.get('Content-Type', None)

        if not mime_type:
            logger.error("Failed to determine file MIME type")
            raise ValueError("Failed to determine file MIME type")

        # Splitting to handle possible MIME type parameters like charset, etc.
        base_mime_type = mime_type.split(';')[0].strip()
        ingestor_class = IngestorFactory.mime_type_mapping.get(base_mime_type)

        if not ingestor_class:
            logger.error(f"No ingestor available for MIME type {mime_type}")
            raise ValueError(f"Unsupported MIME type {mime_type}")

        return ingestor_class(file_path, metadata)
