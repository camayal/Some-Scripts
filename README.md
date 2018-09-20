# Some-Scripts
Repository for different one-file scripts (Phylogenetics, Bioinformatics, Name managers, etc.)

Instructions are in the scripts. Here are some examples:

## [moveNames.py](https://github.com/camayal/Some-Scripts/blob/master/moveNames.py)
Script useful for moving parts of the name in files like fasta or fastq. It can rename an entire file from something like >ATG100X5_Sp1_Rand to >Sp1_ATG10X5_Rand using the pattern "2_1_3" moving the "elements" in the name knowing the separator.

### Examples
```bash
$ python moveNames.py fasta.fa _ "2_1"
$ python moveNames.py fasta.fastq _ "2_1" "@"
$ python moveNames.py fasta2.fas - "New-2-gID_3-4"
```
### Results
```
Original description line           New description line
>SeqABC_ATG10455           ----->  >ATG10455_SeqABC
@Seq1_gn33                 ----->  @gn33_Seq1
>SeqE-E1-kmr59944-Obs1     ----->  >New-E1-gID_3-Obs1
```
