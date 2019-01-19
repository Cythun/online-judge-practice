def to_rna(dna_strand):
    translator = {
        'C': 'G',
        'G': 'C',
        'T': 'A',
        'A': 'U'
    }
    result = ''
    
    for letter in dna_strand:
        result += translator[letter]

    return result
