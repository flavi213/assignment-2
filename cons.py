def read_fasta(file_path):
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

def gen_matrix(seq):
    n = len(seq[0])
    p_mat = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}
    for s in seq:
        for j in range(n):
            base = s[j]
            p_mat[base][j] += 1
    return p_mat

def gen_string(p_mat, n):
    consensus = []
    for j in range(n):
        max_count = -1
        max_base = ''
        
        for base in 'ACGT':
            if p_mat[base][j] > max_count:
                max_count = p_mat[base][j]
                max_base = base
                
        consensus.append(max_base)
    
    return ''.join(consensus)

def print_matrix(p_mat):
    for base in 'ACGT':
        print(f"{base}: {' '.join(map(str, p_mat[base]))}")

if __name__ == "__main__":
    file_path = 'input.fasta'  
    seq = read_fasta(file_path)
    p_mat = gen_matrix(seq)
    consensus_string = gen_string(p_mat, len(seq[0]))
    print(consensus_string)
    print_matrix(p_mat)