# DNA_TOOL_KIT

A lightweight Python toolkit for DNA sequence validation and analysis.

## Features

- **Sequence Validation**: Validate DNA sequences to ensure they contain only valid nucleotides (A, T, C, G)
- **Nucleotide Frequency Analysis**: Count the occurrences of each nucleotide in a DNA sequence

## Installation

Clone the repository:

```bash
git clone https://github.com/Hami0095/DNA_TOOL_KIT.git
cd DNA_TOOL_KIT
```

## Usage

### Validate a DNA Sequence

```python
from dna_tool_kit import validateSeq

sequence = "ATCGATCG"
result = validateSeq(sequence)
print(result)  # Returns the uppercase sequence if valid
```

The `validateSeq()` function checks if a sequence contains only valid nucleotides (A, T, C, G) and returns the uppercase sequence if valid, or `False` if invalid.

### Count Nucleotide Frequency

```python
from dna_tool_kit import countNucleotidesFreq

sequence = "ATCGATCGATCG"
freq = countNucleotidesFreq(sequence)
print(freq)  # {'A': 3, 'T': 3, 'C': 3, 'G': 3}
```

The `countNucleotidesFreq()` function returns a dictionary with the count of each nucleotide. It raises an exception if the sequence is invalid.

## API Reference

### `validateSeq(dna_seq)`

Validates a DNA sequence.

**Args:**
- `dna_seq` (str): The DNA sequence to validate

**Returns:**
- `str`: The uppercase sequence if valid
- `bool`: `False` if the sequence contains invalid nucleotides

### `countNucleotidesFreq(dna_seq)`

Counts the occurrences of each nucleotide in a DNA sequence.

**Args:**
- `dna_seq` (str): The DNA sequence

**Returns:**
- `dict`: A dictionary with counts for A, T, C, G

**Raises:**
- `Exception`: If the DNA sequence is invalid

## License

See LICENSE file for details.