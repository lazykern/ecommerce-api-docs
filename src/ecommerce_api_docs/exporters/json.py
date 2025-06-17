import json
from pathlib import Path
from datetime import datetime
from typing import List, Union, Dict
from pydantic import HttpUrl
from ..models import APIDocumentation, APIEndpoint
from .base import BaseExporter


class JSONExporter(BaseExporter):
    """Export API documentation to JSON format with flexible organization."""
    
    def __init__(self, output_dir: str = "output", organization: str = "module"):
        super().__init__(output_dir)
        self.organization = organization
    
    def export(self, api_doc: APIDocumentation) -> Union[str, List[str]]:
        """Export API documentation based on organization strategy."""
        if self.organization == "single":
            return self._export_single(api_doc)
        elif self.organization == "module":
            return self._export_by_module(api_doc)
        elif self.organization == "endpoint":
            return self._export_by_endpoint(api_doc)
        else:
            raise ValueError(f"Unknown organization strategy: {self.organization}")
    
    def _export_single(self, api_doc: APIDocumentation) -> str:
        """Export all documentation to a single JSON file."""
        filename = f"{self._safe_filename(api_doc.platform)}_{self._safe_filename(api_doc.title)}.json"
        filepath = self.output_dir / filename
        
        api_dict = api_doc.model_dump()
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(api_dict, f, indent=2, default=self._custom_serializer, ensure_ascii=False)
        
        return str(filepath)
    
    def _export_by_module(self, api_doc: APIDocumentation) -> List[str]:
        """Export documentation organized by modules (one file per module)."""
        # Group endpoints by module
        modules: Dict[str, List[APIEndpoint]] = {}
        for endpoint in api_doc.endpoints:
            module_name = endpoint.tags[0] if endpoint.tags else 'general'
            if module_name not in modules:
                modules[module_name] = []
            modules[module_name].append(endpoint)
        
        exported_files = []
        
        # Create main index file
        index_file = self._create_index_json(api_doc, modules)
        exported_files.append(index_file)
        
        # Create module files
        for module_name, module_endpoints in modules.items():
            module_file = self._create_module_json(api_doc, module_name, module_endpoints)
            exported_files.append(module_file)
        
        return exported_files
    
    def _export_by_endpoint(self, api_doc: APIDocumentation) -> List[str]:
        """Export documentation with one file per endpoint, organized in module directories."""
        exported_files = []
        
        # Group endpoints by module
        modules: Dict[str, List[APIEndpoint]] = {}
        for endpoint in api_doc.endpoints:
            module_name = endpoint.tags[0] if endpoint.tags else 'general'
            if module_name not in modules:
                modules[module_name] = []
            modules[module_name].append(endpoint)
        
        # Create main index file
        index_file = self._create_index_json(api_doc, modules)
        exported_files.append(index_file)
        
        # Create individual endpoint files in module directories
        for module_name, module_endpoints in modules.items():
            module_dir = self.output_dir / self._safe_filename(module_name.lower())
            module_dir.mkdir(exist_ok=True)
            
            # Create module index
            module_index = self._create_module_index_json(api_doc, module_name, module_endpoints, module_dir)
            exported_files.append(module_index)
            
            # Create individual endpoint files
            for endpoint in module_endpoints:
                endpoint_file = self._create_endpoint_json(endpoint, module_dir)
                exported_files.append(endpoint_file)
        
        return exported_files
    
    def _create_index_json(self, api_doc: APIDocumentation, modules: Dict[str, List[APIEndpoint]]) -> str:
        """Create main index JSON file."""
        filename = f"{self._safe_filename(api_doc.platform)}_index.json"
        filepath = self.output_dir / filename
        
        index_data = {
            "title": api_doc.title,
            "platform": api_doc.platform,
            "version": api_doc.version,
            "base_url": api_doc.base_url,
            "source_url": api_doc.source_url,
            "description": api_doc.description,
            "scraped_at": api_doc.scraped_at,
            "statistics": {
                "total_endpoints": len(api_doc.endpoints),
                "total_modules": len(modules),
                "endpoints_by_module": {name: len(endpoints) for name, endpoints in modules.items()}
            },
            "modules": [
                {
                    "name": module_name,
                    "endpoint_count": len(endpoints),
                    "file_reference": f"{self._safe_filename(module_name.lower())}.json" if self.organization == "module" else f"{self._safe_filename(module_name.lower())}/",
                    "endpoints": [{"name": ep.name, "method": ep.method.value, "path": ep.path} for ep in endpoints]
                }
                for module_name, endpoints in modules.items()
            ]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2, default=self._custom_serializer, ensure_ascii=False)
        
        return str(filepath)
    
    def _create_module_json(self, api_doc: APIDocumentation, module_name: str, endpoints: List[APIEndpoint]) -> str:
        """Create a JSON file for a single module."""
        filename = f"{self._safe_filename(module_name.lower())}.json"
        filepath = self.output_dir / filename
        
        module_data = {
            "module_name": module_name,
            "platform": api_doc.platform,
            "version": api_doc.version,
            "base_url": api_doc.base_url,
            "endpoint_count": len(endpoints),
            "endpoints": [endpoint.model_dump() for endpoint in endpoints]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(module_data, f, indent=2, default=self._custom_serializer, ensure_ascii=False)
        
        return str(filepath)
    
    def _create_module_index_json(self, api_doc: APIDocumentation, module_name: str, endpoints: List[APIEndpoint], module_dir: Path) -> str:
        """Create an index JSON file for a module directory."""
        filename = "index.json"
        filepath = module_dir / filename
        
        module_index_data = {
            "module_name": module_name,
            "platform": api_doc.platform,
            "endpoint_count": len(endpoints),
            "endpoints": [
                {
                    "name": endpoint.name,
                    "method": endpoint.method.value,
                    "path": endpoint.path,
                    "description": endpoint.description,
                    "file_reference": f"{self._safe_filename(endpoint.name.lower().replace(' ', '_'))}.json"
                }
                for endpoint in endpoints
            ]
        }
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(module_index_data, f, indent=2, default=self._custom_serializer, ensure_ascii=False)
        
        return str(filepath)
    
    def _create_endpoint_json(self, endpoint: APIEndpoint, module_dir: Path) -> str:
        """Create a JSON file for a single endpoint."""
        filename = f"{self._safe_filename(endpoint.name.lower().replace(' ', '_'))}.json"
        filepath = module_dir / filename
        
        endpoint_data = endpoint.model_dump()
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(endpoint_data, f, indent=2, default=self._custom_serializer, ensure_ascii=False)
        
        return str(filepath)
    
    def _custom_serializer(self, obj):
        """Custom serialization for datetime and HttpUrl objects."""
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, HttpUrl):
            return str(obj)
        raise TypeError(f"Object of type {type(obj)} is not JSON serializable")
    
    def export_compact(self, api_doc: APIDocumentation) -> str:
        """Export API documentation to compact JSON file."""
        filename = f"{self._safe_filename(api_doc.platform)}_{self._safe_filename(api_doc.title)}_compact.json"
        filepath = self.output_dir / filename
        
        api_dict = api_doc.model_dump()
        
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(api_dict, f, separators=(',', ':'), default=self._custom_serializer)
        
        return str(filepath) 