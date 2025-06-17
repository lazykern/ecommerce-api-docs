from abc import ABC, abstractmethod
from pathlib import Path
from ..models import APIDocumentation


class BaseExporter(ABC):
    """Base class for all documentation exporters."""
    
    def __init__(self, output_dir: str = "output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
    
    @abstractmethod
    def export(self, api_doc: APIDocumentation) -> str:
        """Export API documentation to target format."""
        pass
    
    def _safe_filename(self, name: str) -> str:
        """Convert a name to a safe filename."""
        # Replace spaces and special characters with underscores
        safe_name = "".join(c if c.isalnum() or c in "._-" else "_" for c in name)
        # Remove multiple consecutive underscores
        safe_name = "_".join(filter(None, safe_name.split("_")))
        return safe_name.lower() 