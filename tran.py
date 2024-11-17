def transition_ratio(s1, s2):
    trans = 0
    transv = 0
    trans_pairs = {('A', 'G'), ('G', 'A'), ('C', 'T'), ('T', 'C')}
    
    for b1, b2 in zip(s1, s2):
        if b1 != b2:
            if (b1, b2) in trans_pairs or (b2, b1) in trans_pairs:
                trans += 1
            else:
                transv += 1
    if transv == 0:
        return float('inf')
    return trans / transv

def read_input_from_fasta(file_path):
    seq = []
    with open(file_path, 'r') as file:
        cur_seq = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):  
                if cur_seq:
                    seq.append(cur_seq)
                cur_seq = ""
            else:
                cur_seq += line
        if cur_seq:
            seq.append(cur_seq)
    return seq

if __name__ == "__main__":
    file_path = 'input.fasta' 
    seq = read_input_from_fasta(file_path)
    s1, s2 = seq[0], seq[1]
    result = transition_ratio(s1, s2)
    print(f"{result:.11f}")