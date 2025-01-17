# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()


def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """
    '''for Justin: To turn a perfectly reasonable sequence into RNA'''
    """
    Assumes that the sequence of to be transcribed into mRNA is the coding strand. Becaue transcription
    uses the reverse complement of the coding strand, the mRNA sequence is identical to DNA expect for U replacing T. 
    """
    rna_sequence = ''

    if len(seq) == 0:
        print('Invalid Input: No Sequence')
    
    elif len(seq) > 0:
        for base in seq:
            if base in ALLOWED_NUC:
                if base == 'T':
                    rna_sequence += 'U'
                if base != 'T':
                    rna_sequence += base
            
            else:
                rna_sequence = 'Invalid Input: Non-nucleotide character'
                break

    return rna_sequence

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """

    """Generates the reverse complement mRNA from the DNA of interest. If the FAST-A/Q 
    sequence is the non coding strand, then this is the function to call.."""

    rna_sequence = ''

    if len(seq) == 0:
        print('Invalid Input: No Sequence')

    elif len(seq) > 0: 
        for base in seq:
            if base in ALLOWED_NUC:
                rna_sequence += TRANSCRIPTION_MAPPING[base]
            else:
                #super silly, but if error output is reversed to begin with then the reverse will be legible
                rna_sequence = ('Invalid Input: Non-nucleotide character')[::-1] 
                break


    reverse_complement = rna_sequence[::-1] #slicing syntax to reverse string

    return reverse_complement

   