from math import comb
def binomial_prob(k, N):
    total_organisms = 2 ** k
    p_AaBb = 1 / 4
    p_not_AaBb = 3 / 4
    prob_at_least_N = 0
    for i in range(N, total_organisms + 1):
        prob_at_least_N += comb(total_organisms, i) * (p_AaBb ** i) * (p_not_AaBb ** (total_organisms - i))
    return prob_at_least_N

def read_input_from_file(file_path):
        with open(file_path, 'r') as file:
            k, N = map(int, file.readline().split())
        return k, N
if __name__ == "__main__":
    file_path = 'input.txt'
    k, N = read_input_from_file(file_path)
    result = binomial_prob(k, N)
    print(f"{result:.3f}")