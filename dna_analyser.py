from Bio.Seq import Seq

seq = Seq("ATGCTAGCTAGCTAGCT")

print("Sequence:", seq)
print("Length:", len(seq))
print("GC Content:", (seq.count("G") + seq.count("C")) / len(seq) * 100, "%")
print("Reverse Complement:", seq.reverse_complement())
print("A count:", seq.count("A"))
print("T count:", seq.count("T"))
print("G count:", seq.count("G"))
print("C count:", seq.count("C"))