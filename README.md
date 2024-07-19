# Text Summarizer CLI

A command-line tool to summarize text into crisp, bullet-point format using the OpenAI-compatible API with the Qwen2 0.5B model and the Click library.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/text_summarizer.git
    cd text_summarizer
    ```

2. Create a virtual environment and install dependencies:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. Ensure Ollama is running locally:
    ```sh
    ollama serve
    ```

4. Prepare the model checkpoint:
    ```sh
    ollama run qwen2:0.5b
    ```



5. Activate the Virtual Environment:
    ```sh
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

6. Run the CLI Tool:

    - To summarize direct text input:
        ```sh
        python summarize_tool.py --text "This is an example text that needs to be summarized."
        ```

    - To summarize text from a file:
        ```sh
        python summarize_tool.py --file path/to/your/textfile.txt
        ```

### Summary

This setup includes all the necessary steps to create and run a CLI tool for text summarization. It uses `Click` for argument handling and integrates with the Ollama API for summarization. Adjust the `README.md` with any additional instructions specific to your setup or usage.
# text-summarizer
