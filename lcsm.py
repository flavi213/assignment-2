def read_fasta(file_path):
    seqs = []
    with open(file_path, 'r') as file:
        cur_seq = ""
        for l in file:
            l = l.strip()
            if l.startswith(">"):  
                if cur_seq:
                    seqs.append(cur_seq)
                cur_seq = ""
            else:
                cur_seq += l
        if cur_seq:
            seqs.append(cur_seq)
    return seqs

def long_sub(seqs):
    short_seq = min(seqs, key=len)
    long_sub = ""
    for length in range(len(short_seq), 0, -1):
        for start in range(len(short_seq) - length + 1):
            subs = short_seq[start:start + length]
            if all(subs in seq for seq in seqs):
                long_sub = subs
                return long_sub
    
    return long_sub

if __name__ == "__main__":
    file_path = 'input.fasta'
    seqs = read_fasta(file_path)
    result = long_sub(seqs)
    print(result)