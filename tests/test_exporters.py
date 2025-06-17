import pytest
import json
import tempfile
from pathlib import Path

from ecommerce_api_docs.exporters import MarkdownExporter, JSONExporter
from ecommerce_api_docs.scrapers import ShopeeScraper


@pytest.fixture
def sample_api_doc():
    """Create a sample API documentation for testing."""
    with ShopeeScraper() as scraper:
        return scraper.scrape()


def test_markdown_exporter_single(sample_api_doc):
    """Test markdown export functionality with single file organization."""
    with tempfile.TemporaryDirectory() as temp_dir:
        exporter = MarkdownExporter(temp_dir, organization="single")
        output_file = exporter.export(sample_api_doc)
        
        # Check file was created
        assert isinstance(output_file, str)
        assert Path(output_file).exists()
        
        # Check content
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "# Shopee Open Platform API v2" in content
            assert "## API Endpoints" in content


def test_markdown_exporter_module(sample_api_doc):
    """Test markdown export functionality with module organization."""
    with tempfile.TemporaryDirectory() as temp_dir:
        exporter = MarkdownExporter(temp_dir, organization="module")
        output_files = exporter.export(sample_api_doc)
        
        # Check multiple files were created
        assert isinstance(output_files, list)
        assert len(output_files) > 1
        
        # Check all files exist
        for file_path in output_files:
            assert Path(file_path).exists()
        
        # Check index file content
        index_file = [f for f in output_files if "index" in f][0]
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
            assert "# Shopee Open Platform API v2" in content
            assert "## Modules" in content


def test_json_exporter_single(sample_api_doc):
    """Test JSON export functionality with single file organization."""
    with tempfile.TemporaryDirectory() as temp_dir:
        exporter = JSONExporter(temp_dir, organization="single")
        output_file = exporter.export(sample_api_doc)
        
        # Check file was created
        assert isinstance(output_file, str)
        assert Path(output_file).exists()
        
        # Check content is valid JSON
        with open(output_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            assert data['platform'] == 'shopee'
            assert data['title'] == 'Shopee Open Platform API v2'
            assert len(data['endpoints']) > 0


def test_json_exporter_module(sample_api_doc):
    """Test JSON export functionality with module organization."""
    with tempfile.TemporaryDirectory() as temp_dir:
        exporter = JSONExporter(temp_dir, organization="module")
        output_files = exporter.export(sample_api_doc)
        
        # Check multiple files were created
        assert isinstance(output_files, list)
        assert len(output_files) > 1
        
        # Check all files exist
        for file_path in output_files:
            assert Path(file_path).exists()
        
        # Check index file content
        index_file = [f for f in output_files if "index" in f][0]
        with open(index_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            assert data['platform'] == 'shopee'
            assert data['title'] == 'Shopee Open Platform API v2'


def test_json_compact_export(sample_api_doc):
    """Test compact JSON export functionality."""
    with tempfile.TemporaryDirectory() as temp_dir:
        exporter = JSONExporter(temp_dir, organization="single")
        output_file = exporter.export_compact(sample_api_doc)
        
        # Check file was created
        assert isinstance(output_file, str)
        assert Path(output_file).exists()
        
        # Check file size is smaller (compact format)
        regular_file = exporter.export(sample_api_doc)
        compact_size = Path(output_file).stat().st_size
        regular_size = Path(regular_file).stat().st_size
        assert compact_size < regular_size


if __name__ == "__main__":
    pytest.main([__file__]) 