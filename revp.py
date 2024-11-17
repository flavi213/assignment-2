def read_fasta():
    # Prompt user for FASTA input directly in the terminal
    print("Enter the FASTA format data (end with an empty line):")
    fasta_input = []
    while True:
        line = input().strip()
        if not line:  # Break if an empty line is entered
            break
        fasta_input.append(line)
    # Extract the DNA string (ignoring the header line)
    return ''.join(fasta_input[1:])  # Combine lines after the header

def reverse_complement(dna):
    # Define the complement of each base
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Create the reverse complement string
    return ''.join(complement[base] for base in reversed(dna))

def find_reverse_palindromes(dna):
    result = []
    n = len(dna)
    
    # Check substrings of lengths from 4 to 12
    for length in range(4, 13):
        for i in range(n - length + 1):
            substring = dna[i:i + length]
            rev_comp = reverse_complement(substring)
            
            # Check if the substring is a reverse palindrome
            if substring == rev_comp:
                result.append((i + 1, length))  # Store 1-based index and length
    
    # Sort results by starting position (first element of the tuple)
    result.sort(key=lambda x: x[0])
    
    return result

# Main program
if __name__ == "__main__":
    # Parse the input DNA sequence
    dna = read_fasta()

    # Find reverse palindromes
    palindromes = find_reverse_palindromes(dna)

    # Output the results in the correct order
    for position, length in palindromes:
        print(position, length)