
import random
import matplotlib.pyplot as plt

def FrequentWords(Text, k):
    Count = {}
    
    for i in range(len(Text)-k+1):
        Pattern = Text[i:i+k]
        if Pattern in Count:
            Count[Pattern] += 1
        else:
            Count[Pattern] = 1

    return Count

def ReverseComplement(Pattern):
    revComp = ''
    revComp = ''.join([complement(x) for x in Pattern][::-1])
    
    return revComp

def complement(Nucleotide):
    comp = ''
    comp = {
        'A': 'T',
        'C': 'G',
        'G': 'C',
        'T': 'A'
    }.get(Nucleotide, 'N')
    
    return comp

def sum_com(freq_dict):
    new_dict = {}
    
    while freq_dict:
        pat = next(iter(freq_dict)) # pattern
        com = ReverseComplement(pat) # complement

        pat_num = freq_dict.pop(pat)
        com_num = 0
        if com in freq_dict:
            com_num = freq_dict.pop(com)

        new_dict[(pat, com)] = pat_num + com_num

    return new_dict

def find_val(Text):
    freq_dict = FrequentWords(Text, 9)
    patcom_dict = sum_com(freq_dict)

    sorted_key = sorted(patcom_dict, key=patcom_dict.get, reverse=True)
    sorted_val = [patcom_dict[key] for key in sorted_key]
    
    #print(sorted_key[0], sorted_val[0])
    return sorted_val

def gen_random(length):    
    random_s = '' # random string
    for _ in range(length):
        random_c = random.choice(['A', 'C', 'T', 'G']) # random character
        random_s += random_c

    return random_s

V_cholerae = open("Vibrio_cholerae.txt").read()
V_val = find_val(V_cholerae)

random_s = gen_random(len(V_cholerae))
R_val = find_val(random_s)

V_line, = plt.plot(V_val, label="V. cholerae")
R_line, = plt.plot(R_val, label="random")

plt.ylabel('Frequency of 9-mers')
plt.xlabel('9-mers, sorted by frequency')
plt.legend(handles=[V_line, R_line])

plt.show()

#E_coli = open("E_coli.txt").read()
#print(len(E_coli))
