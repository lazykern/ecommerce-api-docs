import click
from rich.console import Console
from rich.table import Table
from pathlib import Path

from ..scrapers import ShopeeScraper, LazadaScraper
from ..exporters import MarkdownExporter, JSONExporter

console = Console()


@click.group()
@click.version_option()
def cli():
    """E-commerce API Documentation Scraper.
    
    Scrape and export API documentation from major e-commerce platforms.
    """
    pass


@cli.command()
@click.option(
    '--platform', 
    type=click.Choice(['shopee', 'tiktok', 'lazada']),
    default='shopee',
    help='Platform to scrape (shopee and lazada are currently supported)'
)
@click.option(
    '--export',
    type=click.Choice(['markdown', 'json', 'all']),
    default='all',
    help='Export format(s)'
)
@click.option(
    '--organization',
    type=click.Choice(['single', 'module', 'endpoint']),
    default='module',
    help='How to organize output files: single (one big file), module (one per module), endpoint (one per endpoint)'
)
@click.option(
    '--output-dir',
    default='output',
    help='Output directory for generated files'
)
def scrape(platform: str, export: str, organization: str, output_dir: str):
    """Scrape API documentation from the specified platform."""
    console.print(f"🚀 Scraping {platform} API documentation...", style="bold blue")
    console.print(f"📂 Organization: {organization}, Export: {export}", style="dim")
    
    try:
        # Choose scraper based on platform
        if platform == 'shopee':
            with ShopeeScraper() as scraper:
                api_doc = scraper.scrape()
        elif platform == 'lazada':
            with LazadaScraper() as scraper:
                api_doc = scraper.scrape()
        else:
            console.print(f"❌ Platform '{platform}' not yet supported", style="bold red")
            return
        
        console.print(f"✅ Successfully scraped {len(api_doc.endpoints)} endpoints", style="bold green")
        
        # Export documentation with organization strategy
        exported_files = []
        
        if export in ['markdown', 'all']:
            md_exporter = MarkdownExporter(output_dir, organization=organization)
            md_files = md_exporter.export(api_doc)
            if isinstance(md_files, list):
                exported_files.extend([('Markdown', f) for f in md_files])
                console.print(f"📝 Markdown exported to {len(md_files)} files", style="green")
            else:
                exported_files.append(('Markdown', md_files))
                console.print(f"📝 Markdown exported to: {md_files}", style="green")
        
        if export in ['json', 'all']:
            json_exporter = JSONExporter(output_dir, organization=organization)
            json_files = json_exporter.export(api_doc)
            if isinstance(json_files, list):
                exported_files.extend([('JSON', f) for f in json_files])
                console.print(f"📄 JSON exported to {len(json_files)} files", style="green")
            else:
                exported_files.append(('JSON', json_files))
                console.print(f"📄 JSON exported to: {json_files}", style="green")
        
        # Show summary table
        table = Table(title="Export Summary", show_header=True, header_style="bold magenta")
        table.add_column("Format", style="cyan")
        table.add_column("File Path", style="green")
        table.add_column("Size", style="yellow")
        
        for format_name, file_path in exported_files:
            file_size = Path(file_path).stat().st_size
            size_str = f"{file_size:,} bytes"
            # Truncate long paths for better display
            display_path = str(file_path)
            if len(display_path) > 50:
                display_path = "..." + display_path[-47:]
            table.add_row(format_name, display_path, size_str)
        
        console.print(table)
        
        # Show organization summary
        if organization == 'module':
            modules = set(endpoint.tags[0] if endpoint.tags else 'unknown' for endpoint in api_doc.endpoints)
            console.print(f"📂 Organized into {len(modules)} modules: {', '.join(sorted(modules))}", style="dim")
        elif organization == 'endpoint':
            console.print(f"📄 {len(api_doc.endpoints)} individual endpoint files created", style="dim")
        
        console.print(f"🎉 Documentation successfully generated for {platform}!", style="bold green")
        
    except Exception as e:
        console.print(f"❌ Error scraping {platform}: {e}", style="bold red")
        raise click.ClickException(str(e))


@cli.command()
@click.argument('directory', default='output')
def list_docs(directory: str):
    """List generated documentation files."""
    output_dir = Path(directory)
    
    if not output_dir.exists():
        console.print(f"❌ Directory '{directory}' does not exist", style="bold red")
        return
    
    files = list(output_dir.glob('*'))
    if not files:
        console.print(f"📁 No files found in '{directory}'", style="yellow")
        return
    
    table = Table(title=f"Documentation Files in {directory}", show_header=True, header_style="bold magenta")
    table.add_column("File Name", style="cyan")
    table.add_column("Type", style="green")
    table.add_column("Size", style="yellow")
    table.add_column("Modified", style="blue")
    
    for file_path in files:
        if file_path.is_file():
            file_type = "Markdown" if file_path.suffix == '.md' else "JSON" if file_path.suffix == '.json' else "Other"
            file_size = f"{file_path.stat().st_size:,} bytes"
            modified_time = file_path.stat().st_mtime
            from datetime import datetime
            modified_str = datetime.fromtimestamp(modified_time).strftime('%Y-%m-%d %H:%M')
            table.add_row(file_path.name, file_type, file_size, modified_str)
    
    console.print(table)


def create_cli():
    """Create and return the CLI application."""
    return cli 