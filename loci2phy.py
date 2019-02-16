#!/usr/bin/python
#
#loci2phy
#
#Author: Carlos Alonso Maya Lastra - 2019
#Description: Script to extract each locus from the *.loci from iPyrad

import sys
import argparse
parser = argparse.ArgumentParser(description='Script to extract each locus from the *.loci from iPyrad.')
parser.add_argument('infile', type=argparse.FileType('r'), default=sys.stdin, help='*.loci file to split')
parser.add_argument("-s", "--separator", help="indicate the character(s) that separate each loci", action="store", default="//")
parser.add_argument("-t", "--truncate", help="truncate names to 8 characteres", action="store_true")
parser.add_argument("-f,", "--format", help="select the output format", choices=['fasta', 'phylip'], action="store", default='phylip')
args = parser.parse_args()

if args.truncate:
    print("truncate turned on")


with args.infile as file:
    resultLocus = ''
    seqLenght = 0
    numSeq = 0
    nSubfile = 1 #set the number of current locus
    for nline, line in enumerate(file, start=1): #move line by line
        line = line.replace('\r', '') #avoid return problems
        line = line.replace('\n', '') #avoid new line problems
        #detect if is a separator, blank or sequence in the file
        if args.separator in line: #detect separator
            f = open(args.infile.name.split(".")[0] + '_locus_' + str(nSubfile) + '.phy', 'w') #each time reach a separator, save the previous seqs
            f.write(str(numSeq) + ' ' + str(seqLenght) + '\n' + resultLocus) 
            f.close()
            resultLocus = '' #reset the big variable
            seqLenght = 0
            numSeq  = 0
            nSubfile += 1 #each time that find the separator increase the number
        else: 
            if line != "": #detect no-blank line and skip blank ones
                resultLocus += line + '\n' #add line to the big variable
                seqLenght = len(line.split()[1]) #calculate the lenght of each sequence
                numSeq += 1 #increase the number of sequences between wach separator
