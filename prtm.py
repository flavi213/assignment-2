def tot_protein(prots):
    mass_table = {
        'A': 71.03711, 'C': 103.00919, 'D': 115.02694, 'E': 129.04259,
        'F': 147.06841, 'G': 57.02146, 'H': 137.05891, 'I': 113.08406,
        'K': 128.09496, 'L': 113.08406, 'M': 131.04049, 'N': 114.04293,
        'P': 97.05276, 'Q': 128.05858, 'R': 156.10111, 'S': 87.03203,
        'T': 101.04768, 'V': 99.06841, 'W': 186.07931, 'Y': 163.06333
    }
    tot_wt = 0
    for amino_acid in prots:
        tot_wt += mass_table[amino_acid] 
    return tot_wt
def read_input_from_file(file_path):
        with open(file_path, 'r') as file:
            prots = file.readline().strip()  
        return prots
   
if __name__ == "__main__":
    file_path = 'input.txt' 
    prots = read_input_from_file(file_path)
    result = tot_protein(prots)
    print(f"{result:.3f}")