#Jacob Wilson
#Allison Obourn
#csc110_1L
#Project 8

MIN_CODONS = 5
MIN_CG_PERCENT = 30

#This fuction reads an introduction and tells what the
#program is going to do
def intro():
    print("This program reports information about DNA")
    print("nucleotide sequences that may encode proteins.")
    
#This function obtains the input file and the output file
def obtain_input():
    thefile = input("Input file name? ")
    outfile = input("Output file name? ")
    print()
    return thefile, outfile

#This function reads the file and collects all the data and returns
#the nucleotide seq, the nucleotide counts, the mass percent of each
#nucleotide, a list of codons, and whether or not the seq if a protein
def collect_data(lines, i):
    seq_name = lines[i].strip("\n")
    seq = lines[i+1].strip("\n")
    seq = seq.upper()
    a_count = 0
    c_count = 0
    g_count = 0
    t_count = 0
    dash_count = 0
    for j in range(0, len(seq)):
        if seq[j] == "A":
            a_count += 1

        elif seq[j] == "C":
            c_count += 1

        elif seq[j] == "G":
            g_count += 1
                
        elif seq[j] == "T":
            t_count += 1

        elif seq[j] == "-":
            dash_count += 1

        a_mass = float(a_count * 135.128)
        c_mass = float(c_count * 111.103)
        g_mass = float(g_count * 151.128)
        t_mass = float(t_count * 125.107)
        dash_mass = float(dash_count * 100.000)
        total_mass = (a_mass + c_mass + g_mass + t_mass + dash_mass)
        total_mass = round(total_mass, 1)
        
        a_percent = (a_mass / total_mass) * 100
        a_percent = round(a_percent, 1)
        c_percent = (c_mass / total_mass) * 100
        c_percent = round(c_percent, 1)
        g_percent = (g_mass / total_mass) * 100
        g_percent = round(g_percent, 1)
        t_percent = (t_mass / total_mass) * 100
        t_percent = round(t_percent, 1)

        new_seq = ""
        for z in range(0, len(seq)):
            if seq[z] != "-":
                new_seq += seq[z]                 
        codons = []
        for w in range(0, len(new_seq),3):
            codons.append(new_seq[int(w):int(w+3)])

        is_protein = 1
        if (c_percent + g_percent) < MIN_CG_PERCENT:
            is_protein += 1
        if codons[0] != "ATG":
            is_protein += 1
        if (codons[len(codons)-1] != "TAA" and codons[len(codons)-1] != "TAG"\
        and codons[len(codons)-1] != "TGA"):
            is_protein += 1
        if len(codons)-1 < MIN_CODONS:
            is_protein += 1

    nuc_list = [a_count, c_count, g_count, t_count, dash_count]
    mass_percent = [a_percent, c_percent, g_percent, t_percent]
    return seq_name, seq, nuc_list, mass_percent, codons, int(is_protein), total_mass

#This function prints out the data results
def print_output(seq_name, seq, nuc_list, mass_percent, codons, is_protein, total_mass, out):                    
        out.write("Regional Name: " + seq_name + "\n")
        out.write("Nucleotides: " + seq + "\n")
        out.write("Nuc. Counts: " + str(nuc_list) + "\n")
        out.write("Total Mass%: " + str(mass_percent) + " of " + str(total_mass) + "\n")
        out.write("Codons List: " + str(codons) + "\n")
        if is_protein == 1:
            out.write("Is Protein?: YES" + "\n")
        else:
            out.write("Is Protein?: NO" + "\n")
        out.write("\n")
                  
#This program reads an input file, collects information about dna,
#and then reports the data back to the user 
def main():
    intro()
    filename, outfile = obtain_input()
    file = open(filename, "r")
    out = open(outfile, "w")
    lines = file.readlines()
    for i in range(0, len(lines), 2):
        collect_data(lines, i)
        seq_name, seq, nuc_list, mass_percent, codons, is_protein, total_mass = collect_data(lines, i)
        print_output(seq_name, seq, nuc_list, mass_percent, codons, is_protein, total_mass, out)
                           
main()
