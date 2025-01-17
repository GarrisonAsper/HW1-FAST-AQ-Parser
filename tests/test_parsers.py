# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    test_data = ('tests/bad.fa')
    parsed_fasta = FastaParser(test_data)

    with pytest.raises(ValueError, match=r"File \(.*\) had 0 lines\."):
        for record in parsed_fasta:
            pass



def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    fastq = 'data/test.fq'
    parsed_fasta = FastaParser(fastq)

    fasta_record = []
    for record in parsed_fasta:
        fasta_record.append(record[0])
    
    assert fasta_record[0] == None

    
def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """

    fastq = 'tests/unit_test.fq'
    parsed_fastq = FastqParser(fastq)

    for record in parsed_fastq:
        test_sequence = record[1]

    assert test_sequence == 'TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCG'
    

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """

    fasta = 'data/test.fa'
    parsed_fastq = FastqParser(fasta)

    fastq_record = []
    for record in parsed_fastq:
        fastq_record.append(record[0])
    
    assert fastq_record[0] == None
    