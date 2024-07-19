import click
from ollama_api import summarize_text

@click.command()
@click.option('--text', '-t', help='Text to summarize')
@click.option('--file', '-f', type=click.File('r'), help='Text file to summarize')
def summarize(text, file):
    """Summarize text from a file or direct input."""
    if text:
        summary = summarize_text(text)
    elif file:
        text_content = file.read()
        summary = summarize_text(text_content)
    else:
        raise click.UsageError("You must provide either --text or --file option.")
    
    click.echo(f"Summary:\n{summary}")

if __name__ == '__main__':
    summarize()
