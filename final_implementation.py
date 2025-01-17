from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """

    # Create instance of FastaParser
    fasta_file = 'data/test.fa'
    parsed_fasta = FastaParser(fasta_file)

    # Create instance of FastqParser
    fastq_file = 'data/test.fq'
    parsed_fastq = FastqParser(fastq_file)
        
    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    print('Transcribed Fasta')
    for record in parsed_fasta:
        print(transcribe(record[1]))
       
    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    print('Transcribed Fastq')
    for record in parsed_fastq:
        print(transcribe(record[1]))

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    print('Reverse Transcribed Fasta')
    for record in parsed_fasta:
        print(reverse_transcribe(record[1]))
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    print('Reverse Transcribed Fastq')
    for record in parsed_fastq:
        print(reverse_transcribe(record[1]))

"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
