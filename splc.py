def read_fasta_input():
    print("Enter the FASTA input (end input with an empty line):")
    fasta_data = []
    while True:
        line = input().strip()
        if not line:
            break
        fasta_data.append(line)
    return parse_fasta("\n".join(fasta_data))

def parse_fasta(fasta_string):
    sequences = {}
    current_label = None
    for line in fasta_string.splitlines():
        if line.startswith(">"):
            current_label = line[1:]  # Remove '>'
            sequences[current_label] = ""
        else:
            sequences[current_label] += line
    return sequences

# Main program
fasta_sequences = read_fasta_input()

# Print the parsed sequences
for label, sequence in fasta_sequences.items():
    print(f"{label}: {sequence}")