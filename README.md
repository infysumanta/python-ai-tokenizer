# python-ai-tokenizer

## Overview

This project provides a Python-based tokenizer for processing and encoding text data. It includes functionalities for tokenizing text, encoding and decoding tokens, and managing a vocabulary.

## Features

- Tokenize text into tokens.
- Encode text into token IDs.
- Decode token IDs back into text.
- Manage and print vocabulary.
- Convert between tokens and strings.

## Project Structure

- `tokenizer.py`: Contains the main `Tokenizer` class with methods for text processing.
- `vocab.py`: Manages the vocabulary used by the tokenizer.
- `example.py`: Demonstrates how to use the tokenizer.
- `requirements.txt`: Lists the dependencies (currently empty).

## Setup

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd python-ai-tokenizer
   ```

2. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate   # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the example script to see the tokenizer in action:

   ```bash
   python example.py
   ```

2. Import the `Tokenizer` class in your Python code:

   ```python
   from tokenizer import Tokenizer

   tokenizer = Tokenizer()
   tokens = tokenizer.tokenize("Your text here")
   print(tokens)
   ```

## Contributing

Feel free to submit issues or pull requests to improve the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
