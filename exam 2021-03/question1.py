fn = 'gene_data.dat'

# Part A
def parse_nucleotides(file: str):
    data = {}
    with open(file, "r") as file:
        while True:
            line = file.readline().strip()
            if line == "":
                break  # Reached end of file
            # Read the comments
            while True:
                if not line.startswith('#'):
                    break
                line = file.readline().strip()

            # Read name
            name = line.split('% ')[1]

            # Read nucleotide data
            nucleotides = []
            while True:
                line = file.readline().strip()
                if line == "":
                    break
                nucleotides.extend(list(line))

            data[name] = nucleotides
    return data

# Part B
def count_nucleotides(dna):
    A_counter = 0
    G_counter = 0
    C_counter = 0
    T_counter = 0
    for item in dna:
        if item == 'A' or item == '*':
            A_counter += 1
        elif item == 'G' or item == '*':
            G_counter += 1
        elif item == 'C' or item == '*':
            C_counter += 1
        elif item == 'T' or item == '*':
            T_counter += 1

    return (A_counter, G_counter, C_counter, T_counter)


def count_max_nucleotides(data):
    results = {'A': {}, 'G': {}, 'C': {}, 'T': {}}
    for name, dna in data.items():
        counts = count_nucleotides(dna)
        length = len(dna)
        for (i, c) in enumerate(('A', 'G', 'C', 'T')):
            results[c][name] = counts[i] / length
    max_n = {}
    for nucleotide, result in results.items():
        k = max(result, key=result.get)
        max_n[nucleotide] = k

    return max_n

mRNA_mapping = {
    'T': 'A',
    'A': 'U',
    'G': 'C',
    'C': 'G',
    '*': '*',
}

# Part C
def export_to_mRNA(file, data):
    with open(file, 'w') as file:
        for name, dna in data.items():
            file.write(f'% {name}\n')
            for i, c in enumerate(dna):
                file.write(mRNA_mapping[c])
                if (i + 1) % 40 == 0:
                    file.write("\n")
            file.write("\n\n")


if __name__ == "__main__":
    d = parse_nucleotides("gene_data.dat")
    maxes = count_max_nucleotides(d)
    print(maxes)
    export_to_mRNA("gene_data_mrna.dat", d)
    d2 = parse_nucleotides("gene_data_mrna.dat")


