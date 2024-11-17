def count_rna_strings(protein):
    # Codon table mapping amino acids to the number of corresponding codons
    codon_table = {
        'A': 4, 'C': 2, 'D': 2, 'E': 2, 'F': 2,
        'G': 4, 'H': 2, 'I': 3, 'K': 2, 'L': 6,
        'M': 1, 'N': 2, 'P': 4, 'Q': 2, 'R': 6,
        'S': 6, 'T': 4, 'V': 4, 'W': 1, 'Y': 2,
        'Stop': 3
    }

    # Initialize total number of RNA strings
    total = 1

    # Compute the total number of RNA strings modulo 1,000,000
    for aa in protein:
        total = (total * codon_table[aa]) % 1_000_000
    
    # Multiply by the number of stop codons
    total = (total * codon_table['Stop']) % 1_000_000

    return total

# Prompt the user for input
protein = input("Enter the protein string: ").strip()

# Calculate and print the total number of RNA strings
result = count_rna_strings(protein)
print(f"The total number of RNA strings that can encode the protein is: {result}")