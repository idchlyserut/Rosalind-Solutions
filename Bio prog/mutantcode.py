
def parse_fasta(s):
    output = {}
    strings = s.strip().split('>')

    for s in strings:
        if len(s) == 0:
            continue

        parts = s.split()
        label = parts[0]
        bases = ''.join(parts[1:])

        output[label] = bases
        
    return output


def gc_content(s):
    n = len(s)
    m = 0

    for c in s:
        if c == 'G' or c == 'C':
            m += 1

    return 100 * (float(m) / n)


if __name__ == "__main__":

    small_dataset = """
    >Rosalind_6404
    CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC
    TCCCACTAATAATTCTGAGG
    >Rosalind_5959
    CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT
    ATATCCATTTGTCAGCAGACACGC
    >Rosalind_0808
    CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC
    TGGGAACCTGCGGGCAGTAGGTGGAAT
    """

    large_dataset = open('C:/Users/User/3D Objects/Bio prog/rosalind_gc.txt').read()

    output = parse_fasta(large_dataset)
    output = dict([(id, gc_content(gc)) for id, gc in output.items()])

    highest_id = None
    highest_gc = 0

    for id, gc in output.items():
        if gc > highest_gc:
            highest_id = id
            highest_gc = gc

    print (highest_id)
    print ('%f%%' % highest_gc)