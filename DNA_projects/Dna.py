#DNA PROCESSING PROJECT


def get_length(dna):
    """ (str) -> int

    Return the length of the DNA sequence dna.


    """
    return len(dna)


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.


    """
    return len(dna1) > len(dna2)


def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.


    """
    return dna.count(nucleotide)


def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.


    False

    """
    return dna1.find(dna2) >= 0


def is_valid_sequence(dna):
    """(str) -> bool
         Return True if and only if the sequence is a valid dna sequence that is having only
         'A','T','G','C' nucleotides.


         """
    count = 0
    for check in dna:
        if not check in 'ATGC':
            count = count + 1
    if count > 0:
        return False
    else:
        return True


def insert_sequence(dna1, dna2, pos):
    """
    (str,str,int)->str
     Return the DNA sequence obtained by inserting the second DNA sequence into the first DNA sequence at the given index


     """
    if pos > len(dna1):
        return False
    elif pos < 0:
        return False
    else:
        x = dna1[:pos]
        y = dna1[pos:]
        return x + dna2 + y


def get_complement(nucleo):
    """
    (str) -> str
    Return the nucleotide's complement.


    """
    if nucleo == 'A':
        return 'T'
    if nucleo == 'T':
        return 'A'
    if nucleo == 'G':
        return 'C'
    if nucleo == 'C':
        return 'G'


def get_complementary_sequence(nucleo):
    """
        (str)->str
        Return the DNA sequence that is complementary to the given DNA sequence.

    """
    nucleo2 = ""
    for char in nucleo:
        nucleo2 = nucleo2 + get_complement(char)
    return nucleo2












































