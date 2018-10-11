# Some-Scripts
Repository for different one-file scripts (Phylogenetics, Bioinformatics, Name managers, etc.)

Also check my gists for more useful one-line codes at: [https://gist.github.com/camayal](https://gist.github.com/camayal)

Instructions are in the scripts. Here are some examples:

## [moveNames.py](https://raw.githubusercontent.com/camayal/Some-Scripts/master/moveNames.py)
Script useful for moving parts of the name in files like fasta or fastq. It can rename an entire file from something like >ATG100X5_Sp1_Rand to >Sp1_ATG10X5_Rand using the pattern "2_1_3" moving the "elements" in the name knowing the separator.

### Help
```bash
python moveNames.py
```

### Examples
```bash
$ python moveNames.py fasta.fa _ "2_1" > newfasta.fa
$ python moveNames.py fasta.fastq _ "2_1" "@" > newfastq.fastq
$ python moveNames.py fasta2.fas - "New-2-gID_3-4" > newfasta2.fas
```
### Results
```
Original description line           New description line
>SeqABC_ATG10455           ----->  >ATG10455_SeqABC
@Seq1_gn33                 ----->  @gn33_Seq1
>SeqE-E1-kmr59944-Obs1     ----->  >New-E1-gID_3-Obs1
```



## [replaceLookTable.py](https://raw.githubusercontent.com/camayal/Some-Scripts/master/replaceLookTable.py)
Script that helps to replace easily strings in a file looking up a table of two columns (new string - old string)

### Help
```bash
python replaceLookTable.py
```

### Examples
```bash
$ python replaceLookTable.py table.txt fasta.fa > resultfile.fa
$ python replaceLookTable.py table.txt fasta.fa "," > resultfile.fa
```
The second line include custom separator "," by default the script look for a TAB

table.txt example:
```
1    ABCD
2    ATYL
3    ATYL-E1
4    ATYL-E2_
```
Be careful with your replacements, in the table.txt example ATYL will replace all ATYL ocurrences, include ATYL-E1, include some unique characters to avoid it like _ as showed in ATYL-E2_


## [ConvertFileUsingAlterAPI.py](https://raw.githubusercontent.com/camayal/Some-Scripts/master/ConvertFileUsingAlterAPI.py)
Script to convert all files in a folder using the API of the webservice of ALTER (Glez-Peña et al. 2010). It can be used in two ways: 1) Paste the file .py in the folder with files to convert and double click it by default it will convert Nexus files to Phylip for using in PhyML. 2) In terminal or cmd in Windows, you can call it using the command line options documented in --help command. If you use this, you must know that it is just a script to execute the ALTER API and you should cited it. Refer to the original ALTER website for more details about citation.

### Help
```bash
python ConvertFileUsingAlterAPI.py --help
```
