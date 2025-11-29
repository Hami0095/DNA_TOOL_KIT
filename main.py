from dna_tool_kit import *
import random

random_seq = ''.join(random.choices(Nucleotides, k=5))
print("Random DNA Sequence: ", random_seq)
print("Is the sequence valid? ", validateSeq(random_seq))
print("Nucleotide Frequencies: ", countNucleotidesFreq(random_seq))

test = "AGXTTAGC"
print("\nTesting with sequence: ", test)
print("Random DNA Sequence: ", test)
print("Is the sequence valid? ", validateSeq(test))
print("Nucleotide Frequencies: ", countNucleotidesFreq(test))

test = "agtcagta"
print("\nTesting with sequence: ", test)
print("Random DNA Sequence: ", test)
print("Is the sequence valid? ", validateSeq(test))
print("Nucleotide Frequencies: ", countNucleotidesFreq(test))