def to_rna(strand):
    genes = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rnacomplement = ''
    if len(strand)==0:
        return ''
    else:
        for letter in strand:
            if letter not in genes:
                return ''
            else:
                rnacomplement+=genes[letter]
    return rnacomplement
