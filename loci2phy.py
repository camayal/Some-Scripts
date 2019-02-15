#!/usr/bin/python
#
#loci2phy
#
#Author: Carlos Alonso Maya Lastra - 2019
#Description: Script to extract each locus from the *.loci from iPyrad

import sys

if len(sys.argv) >= 2:  #verify all mandatory arguments are in the line   
    if len(sys.argv) > 2: #if the second argument is provided take it as separator else put // as default
       separator = str(sys.argv[2])
    else:
        separator = '//'


    with open(sys.argv[1], 'r') as f: #open the file (argv[1])
        resultLocus = ''
        seqLenght = 0
        numSeq = 0
        nSubfile = 1 #set the number of current locus
        for nline, line in enumerate(f, start=1): #move line by line
            line = line.replace('\r', '') #avoid return problems
            line = line.replace('\n', '') #avoid new line problems
            #detect if is a separator, blank or sequence in the file
            if separator in line: #detect separator
                f = open(str(sys.argv[1].split('.')[0]) + '_locus_' + str(nSubfile) + '.phy', 'w') #each time reach a separator, save the previous seqs
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


            
                

else: #show a help if the script is not properlly called
    print 'This script need the follow arguments: \nfilename, [separator]'
    print '\nExample 1:'
    print 'python loci2phy.py file.loci'
    print '\nIt separate each locus in an independent file named: file_locus_n.phy'
