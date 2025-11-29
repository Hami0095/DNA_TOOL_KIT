
Nucleotides = ['A', 'T', 'C', 'G']
Complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def validateSeq(dna_seq):
    """Validate a DNA sequence.

    Args:
        dna_seq (str): The DNA sequence to validate.

    Returns:
        bool: True if the sequence is valid, False otherwise.
    """
    tmp = dna_seq.upper()
    for nucleotide in tmp:
        if nucleotide not in Nucleotides:
            return False
    return tmp

def countNucleotidesFreq(dna_seq):
    """Count the occurrences of each nucleotide in a DNA sequence.

        Args:
            dna_seq (str): The DNA sequence.
    """
    tmp = {'A':0, 'T':0, 'C':0, 'G':0}
    if(not validateSeq(dna_seq)):
        raise Exception
    for nucleotide in dna_seq.upper():
        if nucleotide in tmp:
            tmp[nucleotide] += 1
    return tmp

        
def transcribeDNAtoRNA(dna_seq):
    """Transcribe a DNA sequence into an RNA sequence.

        Args:
            dna_seq (str): The DNA sequence.
    """
    if(not validateSeq(dna_seq)):
        raise Exception("Invalid DNA Sequence")
    return dna_seq.upper().replace('T', 'U')    

def reverse_complementDNA(dna_seq):
    """Get the reverse complement of a DNA sequence.

        Args:
            dna_seq (str): The DNA sequence.
    """
    if(not validateSeq(dna_seq)):
        raise Exception("Invalid DNA Sequence")
    tmp = dna_seq.upper()[::-1]
    rev_comp = ''.join([Complement[nuc] for nuc in tmp])
    return rev_comp

def complementDna(dna_seq):
    """Get the complement of a DNA sequence.

        Args:
            dna_seq (str): The DNA sequence.
    """
    if(not validateSeq(dna_seq)):
        raise Exception("Invalid DNA Sequence")
    comp = ''.join([Complement[nuc] for nuc in dna_seq.upper()])
    return comp


