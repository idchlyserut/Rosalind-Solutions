#Calculate Estimated Offspring

def calc(dataset):
    # To calculate total expected dominant values from data. 
    dominant_genotype_table, expected_value = [1.0, 1.0, 1.0, 0.75, 0.5, 0], 0
    # Static loop that aggregates dominant gene occurrences from data and data-table
    for n in range(6):
        expected_value += 2 * dataset[n] * dominant_genotype_table[n] 
    return expected_value

def main():
    # NOTE: Requires being in parent repo ('pwd' must return up to directory '/Rosalind_Bioinformatics/Bioinformatics_Stronghold')
    FileRead = "C:/Users/User/3D Objects/Bio prog/rosalind_iev.txt"
    FileWrite = "C:/Users/User/3D Objects/Bio prog/output.txt"

    # Reads text data from raw dataset as single-line array of characters
    with open(FileRead, "r") as fr:
        data = [float(n) for n in fr.read().split(" ")]

    # Creates output file and writes appropriate response to file and notifies user
    with open(FileWrite, "w") as fw:
        fw.write(str(calc(data)))

    return print("\nThe Expected Offspring dataset has been processed and the appropriate output has been saved to {}.\n".format(FileWrite[2:]))

if __name__ == "__main__":
    main()
