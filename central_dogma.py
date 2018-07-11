import random


def dna_generation(size):
    return "".join([random.choice('ATGC') for _ in range(size)])


def dna_reverse_compliment(dna):
    mapping = {'A': 'T', 'C': 'G', 'T': 'A', 'G': 'C'}
    return "".join([mapping[base] for base in dna])


def rna_reverse_compliment(dna_rev):
    mapping = {'A': 'U', 'C': 'G', 'T': 'A', 'G': 'C'}
    return "".join([mapping[base] for base in dna_rev])


if __name__ == '__main__':
    size = int(input('Enter size of the DNA: '))

    # TRANSCRIPTION STARTS

    # step 1
    dna = dna_generation(size)
    print(dna)

    # step 2
    dna_rev = dna_reverse_compliment(dna)
    print(dna_rev)

    # step 3
    rna = rna_reverse_compliment(dna_rev)
    print(rna)

    # TRNASCRIPTION ENDS
