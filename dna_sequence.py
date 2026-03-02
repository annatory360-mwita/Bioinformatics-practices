sequence = "ATCTGACGATGACGAT"

print("DNA Sequence:", sequence)
print("length:", len(sequence))
print("GC content:",(sequence.count('G') + sequence.count('C'))/len(sequence)*100, "%")
