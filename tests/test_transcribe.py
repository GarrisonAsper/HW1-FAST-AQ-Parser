# write tests for transcribe functions

from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    test_sequence = 'ATGC'
    correct_output = 'AUGC'
    test_output = transcribe(test_sequence)

    assert test_output == test_output

def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    test_sequence = 'ATGC'
    correct_output = 'GCAU'
    test_output = reverse_transcribe(test_sequence)

    assert test_output == correct_output