from pathlib import Path
from typing import List, Union, Dict
from jinja2 import Template
from ..models import APIDocumentation, APIEndpoint
from .base import BaseExporter


class MarkdownExporter(BaseExporter):
    """Export API documentation to Markdown format with flexible organization."""
    
    def __init__(self, output_dir: str = "output", organization: str = "module"):
        super().__init__(output_dir)
        self.organization = organization
        self.single_template = self._create_single_template()
        self.module_template = self._create_module_template()
        self.endpoint_template = self._create_endpoint_template()
    
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
        """Export all documentation to a single file."""
        filename = f"{self._safe_filename(api_doc.platform)}_{self._safe_filename(api_doc.title)}.md"
        filepath = self.output_dir / filename
        
        content = self.single_template.render(api_doc=api_doc)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return str(filepath)
    
    def _export_by_module(self, api_doc: APIDocumentation) -> List[str]:
        """Export documentation organized by modules (one file per module)."""
        # Group endpoints by module (using first tag as module name)
        modules: Dict[str, List[APIEndpoint]] = {}
        for endpoint in api_doc.endpoints:
            module_name = endpoint.tags[0] if endpoint.tags else 'general'
            if module_name not in modules:
                modules[module_name] = []
            modules[module_name].append(endpoint)
        
        exported_files = []
        
        # Create main index file
        index_file = self._create_index_file(api_doc, modules)
        exported_files.append(index_file)
        
        # Create module files
        for module_name, module_endpoints in modules.items():
            module_file = self._create_module_file(api_doc, module_name, module_endpoints)
            exported_files.append(module_file)
        
        return exported_files
    
    def _export_by_endpoint(self, api_doc: APIDocumentation) -> List[str]:
        """Export documentation with one file per endpoint, organized in module directories."""
        exported_files = []
        
        # Group endpoints by module for directory organization
        modules: Dict[str, List[APIEndpoint]] = {}
        for endpoint in api_doc.endpoints:
            module_name = endpoint.tags[0] if endpoint.tags else 'general'
            if module_name not in modules:
                modules[module_name] = []
            modules[module_name].append(endpoint)
        
        # Create main index file
        index_file = self._create_index_file(api_doc, modules)
        exported_files.append(index_file)
        
        # Create individual endpoint files in module directories
        for module_name, module_endpoints in modules.items():
            module_dir = self.output_dir / self._safe_filename(module_name.lower())
            module_dir.mkdir(exist_ok=True)
            
            # Create module index
            module_index = self._create_module_index(api_doc, module_name, module_endpoints, module_dir)
            exported_files.append(module_index)
            
            # Create individual endpoint files
            for endpoint in module_endpoints:
                endpoint_file = self._create_endpoint_file(endpoint, module_dir)
                exported_files.append(endpoint_file)
        
        return exported_files
    
    def _create_index_file(self, api_doc: APIDocumentation, modules: Dict[str, List[APIEndpoint]]) -> str:
        """Create main index file."""
        filename = f"{self._safe_filename(api_doc.platform)}_index.md"
        filepath = self.output_dir / filename
        
        content = f"""# {api_doc.title}

**Platform:** {api_doc.platform.title()}  
**Version:** {api_doc.version}  
**Base URL:** {api_doc.base_url or 'N/A'}  
**Source:** {api_doc.source_url or 'N/A'}  
**Scraped:** {api_doc.scraped_at.strftime('%Y-%m-%d %H:%M:%S')}

## Description

{api_doc.description or 'No description available.'}

## Modules Overview

{'| Module | Endpoints | Description |' if modules else 'No modules found.'}
{'|--------|-----------|-------------|' if modules else ''}
"""
        
        for module_name, endpoints in modules.items():
            module_link = f"{self._safe_filename(module_name.lower())}.md" if self.organization == "module" else f"{self._safe_filename(module_name.lower())}/"
            content += f"| [{module_name}]({module_link}) | {len(endpoints)} | {module_name} API endpoints |\n"
        
        content += f"""
## Statistics

- **Total Endpoints:** {len(api_doc.endpoints)}
- **Total Modules:** {len(modules)}
- **Documentation Generated:** {api_doc.scraped_at.strftime('%Y-%m-%d')}

## Usage

This documentation was automatically generated from the {api_doc.platform} API documentation. Use it for local development reference.

### Authentication

Most endpoints require authentication. Please refer to the official {api_doc.platform} documentation for authentication setup.

### Rate Limiting

Please respect the rate limits specified for each endpoint to avoid being blocked.
"""
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return str(filepath)
    
    def _create_module_file(self, api_doc: APIDocumentation, module_name: str, endpoints: List[APIEndpoint]) -> str:
        """Create a file for a single module."""
        filename = f"{self._safe_filename(module_name.lower())}.md"
        filepath = self.output_dir / filename
        
        content = self.module_template.render(
            api_doc=api_doc,
            module_name=module_name,
            endpoints=endpoints
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return str(filepath)
    
    def _create_module_index(self, api_doc: APIDocumentation, module_name: str, endpoints: List[APIEndpoint], module_dir: Path) -> str:
        """Create an index file for a module directory."""
        filename = "index.md"
        filepath = module_dir / filename
        
        content = f"""# {module_name} API

**Module:** {module_name}  
**Endpoints:** {len(endpoints)}  
**Platform:** {api_doc.platform.title()}

## Endpoints

{'| Endpoint | Method | Description |' if endpoints else 'No endpoints found.'}
{'|----------|--------|-------------|' if endpoints else ''}
"""
        
        for endpoint in endpoints:
            endpoint_link = f"{self._safe_filename(endpoint.name.lower().replace(' ', '_'))}.md"
            content += f"| [{endpoint.name}]({endpoint_link}) | {endpoint.method.value} | {endpoint.description or 'No description'} |\n"
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return str(filepath)
    
    def _create_endpoint_file(self, endpoint: APIEndpoint, module_dir: Path) -> str:
        """Create a file for a single endpoint."""
        filename = f"{self._safe_filename(endpoint.name.lower().replace(' ', '_'))}.md"
        filepath = module_dir / filename
        
        content = self.endpoint_template.render(endpoint=endpoint)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return str(filepath)
    
    def _create_single_template(self) -> Template:
        """Create template for single file export."""
        template_str = """# {{ api_doc.title }}

**Platform:** {{ api_doc.platform | title }}  
**Version:** {{ api_doc.version }}  
**Base URL:** {{ api_doc.base_url if api_doc.base_url else 'N/A' }}  
**Source:** {{ api_doc.source_url if api_doc.source_url else 'N/A' }}  
**Scraped:** {{ api_doc.scraped_at.strftime('%Y-%m-%d %H:%M:%S') }}

{% if api_doc.description %}
## Description

{{ api_doc.description }}
{% endif %}

## API Endpoints

{% for endpoint in api_doc.endpoints %}
### {{ endpoint.name }}

**Method:** `{{ endpoint.method.value }}`  
**Path:** `{{ endpoint.path }}`  
{% if endpoint.summary %}**Summary:** {{ endpoint.summary }}{% endif %}  
{% if endpoint.description %}**Description:** {{ endpoint.description }}{% endif %}  
{% if endpoint.tags %}**Tags:** {{ endpoint.tags | join(', ') }}{% endif %}  
{% if endpoint.rate_limit %}**Rate Limit:** {{ endpoint.rate_limit }}{% endif %}  
**Authentication Required:** {{ 'Yes' if endpoint.authentication_required else 'No' }}

{% if endpoint.parameters %}
#### Parameters

| Name | Type | Location | Required | Description | Default | Example |
|------|------|----------|----------|-------------|---------|---------|
{% for param in endpoint.parameters %}| {{ param.name }} | {{ param.type.value }} | {{ param.location.value }} | {{ 'Yes' if param.required else 'No' }} | {{ param.description or 'N/A' }} | {{ param.default_value or 'N/A' }} | {{ param.example or 'N/A' }} |
{% endfor %}
{% endif %}

{% if endpoint.responses %}
#### Responses

{% for response in endpoint.responses %}
**{{ response.status_code }}** - {{ response.description or 'No description' }}

{% if response.example %}
```json
{{ response.example | tojson(indent=2) }}
```
{% endif %}
{% endfor %}
{% endif %}

{% if endpoint.examples %}
#### Examples

{% for example in endpoint.examples %}
##### {{ example.title }}
{% if example.description %}
{{ example.description }}
{% endif %}

{% if example.request %}
**Request:**
```json
{{ example.request | tojson(indent=2) }}
```
{% endif %}

{% if example.response %}
**Response:**
```json
{{ example.response | tojson(indent=2) }}
```
{% endif %}
{% endfor %}
{% endif %}

{% if endpoint.error_codes %}
#### Error Codes

| Code | Message | HTTP Status | Description |
|------|---------|-------------|-------------|
{% for error in endpoint.error_codes %}| {{ error.code }} | {{ error.message }} | {{ error.http_status or 'N/A' }} | {{ error.description or 'N/A' }} |
{% endfor %}
{% endif %}

---

{% endfor %}

## Summary

- **Total Endpoints:** {{ api_doc.endpoints | length }}
- **Platforms Covered:** {{ api_doc.platform }}
- **Documentation Generated:** {{ api_doc.scraped_at.strftime('%Y-%m-%d') }}
"""
        return Template(template_str)
    
    def _create_module_template(self) -> Template:
        """Create template for module files."""
        template_str = """# {{ module_name }} API

**Module:** {{ module_name }}  
**Platform:** {{ api_doc.platform | title }}  
**Endpoints:** {{ endpoints | length }}

## Overview

This module contains {{ endpoints | length }} endpoints for {{ module_name }} related operations.

## Endpoints

{% for endpoint in endpoints %}
### {{ endpoint.name }}

**Method:** `{{ endpoint.method.value }}`  
**Path:** `{{ endpoint.path }}`  
{% if endpoint.description %}**Description:** {{ endpoint.description }}{% endif %}  
{% if endpoint.rate_limit %}**Rate Limit:** {{ endpoint.rate_limit }}{% endif %}  
**Authentication Required:** {{ 'Yes' if endpoint.authentication_required else 'No' }}

{% if endpoint.parameters %}
#### Parameters

| Name | Type | Location | Required | Description | Default | Example |
|------|------|----------|----------|-------------|---------|---------|
{% for param in endpoint.parameters %}| {{ param.name }} | {{ param.type.value }} | {{ param.location.value }} | {{ 'Yes' if param.required else 'No' }} | {{ param.description or 'N/A' }} | {{ param.default_value or 'N/A' }} | {{ param.example or 'N/A' }} |
{% endfor %}
{% endif %}

{% if endpoint.responses %}
#### Responses

{% for response in endpoint.responses %}
**{{ response.status_code }}** - {{ response.description or 'No description' }}

{% if response.example %}
```json
{{ response.example | tojson(indent=2) }}
```
{% endif %}
{% endfor %}
{% endif %}

---

{% endfor %}
"""
        return Template(template_str)
    
    def _create_endpoint_template(self) -> Template:
        """Create template for individual endpoint files."""
        template_str = """# {{ endpoint.name }}

**Method:** `{{ endpoint.method.value }}`  
**Path:** `{{ endpoint.path }}`  
{% if endpoint.tags %}**Module:** {{ endpoint.tags[0] }}{% endif %}  
{% if endpoint.rate_limit %}**Rate Limit:** {{ endpoint.rate_limit }}{% endif %}  
**Authentication Required:** {{ 'Yes' if endpoint.authentication_required else 'No' }}

## Description

{{ endpoint.description or 'No description available.' }}

{% if endpoint.summary %}
## Summary

{{ endpoint.summary }}
{% endif %}

{% if endpoint.parameters %}
## Parameters

| Name | Type | Location | Required | Description | Default | Example |
|------|------|----------|----------|-------------|---------|---------|
{% for param in endpoint.parameters %}| {{ param.name }} | {{ param.type.value }} | {{ param.location.value }} | {{ 'Yes' if param.required else 'No' }} | {{ param.description or 'N/A' }} | {{ param.default_value or 'N/A' }} | {{ param.example or 'N/A' }} |
{% endfor %}
{% else %}
No parameters required.
{% endif %}

{% if endpoint.responses %}
## Responses

{% for response in endpoint.responses %}
### {{ response.status_code }} - {{ response.description or 'No description' }}

{% if response.example %}
```json
{{ response.example | tojson(indent=2) }}
```
{% endif %}
{% endfor %}
{% else %}
No response information available.
{% endif %}

{% if endpoint.examples %}
## Examples

{% for example in endpoint.examples %}
### {{ example.title }}
{% if example.description %}
{{ example.description }}
{% endif %}

{% if example.request %}
**Request:**
```json
{{ example.request | tojson(indent=2) }}
```
{% endif %}

{% if example.response %}
**Response:**
```json
{{ example.response | tojson(indent=2) }}
```
{% endif %}
{% endfor %}
{% endif %}

{% if endpoint.error_codes %}
## Error Codes

| Code | Message | HTTP Status | Description |
|------|---------|-------------|-------------|
{% for error in endpoint.error_codes %}| {{ error.code }} | {{ error.message }} | {{ error.http_status or 'N/A' }} | {{ error.description or 'N/A' }} |
{% endfor %}
{% endif %}
"""
        return Template(template_str) 