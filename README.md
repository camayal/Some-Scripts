# Some-Scripts
Repository for different one-file scripts (Phylogenetics, Bioinformatics, Name managers, etc.)

Instructions are in the scripts. Here are some examples:

## moveNames.py
```bash
$ python moveNames.py fasta.fa _ "2_1"
$ python moveNames.py fasta.fastq _ "2_1" "@"
$ python moveNames.py fasta.fastq - "New-2-gID_3-4"
```
Results
```
Original description line           New description line
>SeqABC_ATG10455           ----->  >ATG10455_SeqABC
@Seq1_gn33                 ----->  @gn33_Seq1
>SeqE-E1-kmr59944-Obs1     ----->  >New-E1-gID_3-Obs1
```
