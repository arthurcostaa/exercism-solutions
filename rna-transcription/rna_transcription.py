DNA_COMPLEMENTS = {
    'G': 'C',
    'C': 'G',
    'T': 'A',
    'A': 'U',
}


def to_rna(dna_strand):
    return ''.join(DNA_COMPLEMENTS[nucleotide] for nucleotide in dna_strand)
