# PDF Extractor and Algorithm Comparison

This repository contains scripts to extract text from PDF files and compare algorithm performance on benchmark functions.

## extract_text.py

This script finds the first occurrence of a specified PDF file, extracts text from it, and either displays the text or saves it to a `.txt` file.

### Usage

1. Ensure the PDF file you want to extract text from is available.
2. Run the script:
    ```bash
    python extract_text.py
    ```

### Features

- Finds the first PDF file matching the specified name in the given directory.
- Option to start extracting text from a specified section.
- Option to display extracted text or save it to a `.txt` file.

## compare_algorithms.py

This script loads data from CSV files and generates comparison plots for algorithm performance on benchmark functions.

### Usage

1. Ensure the CSV files (`fss_data.csv`, `pso_data.csv`, `salto_quantic_data.csv`) are available.
2. Run the script:
    ```bash
    python compare_algorithms.py
    ```

### Features

- Loads algorithm performance data from CSV files.
- Generates comparison plots for Rastrigin, Ackley, Rosenbrock, and Sphere functions.

## License

This project is licensed under the MIT License.

