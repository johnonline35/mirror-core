import logging
import pdfplumber
import layoutparser as lp
from plugins.base_plugin import BaseIngestor

logger = logging.getLogger(__name__)

class PdfIngestor(BaseIngestor):
    def __init__(self, file_path, metadata):
        super().__init__(file_path)
        self.metadata = metadata

    def detect_layout(self, page):
        """ Placeholder for layout detection logic.
            Currently, just logs the bounding box of extracted text.
        """
        text = page.extract_text()
        if text:
            logger.info(f"Text found with bounding box: {page.bbox}")
        else:
            logger.info("No text found, possible complex layout or image-based page.")

    def ingest(self):
        try:
            with pdfplumber.open(self.file_path) as pdf:
                full_text = [page.extract_text() for page in pdf.pages if page.extract_text()]
            return {"text": full_text, "metadata": self.metadata}
        except Exception as e:
            logger.error(f"Failed to ingest data from PDF: {e}")
            raise
