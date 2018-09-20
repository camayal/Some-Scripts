#!/usr/bin/python
#
#replaceLookTable
#
#Author: Carlos Alonso Maya Lastra - 2018
#Replace easily string following a table of two columns
#


import sys

if len(sys.argv) >= 3:  #verify all mandatory arguments are in the line           
    with open(sys.argv[2], 'r') as f: #open the file (argv[2])
        
        for nline, line in enumerate(f, start=1): #move line by line
            line = line.replace('\r', '') #avoid return problems
            line = line.replace('\n', '') #avoid new line problems
            newLine = line
            with open(sys.argv[1], 'r') as table: #open the table (argv[1])
                for nsline, sline in enumerate(table, start=1): #move line by line
                    sline = sline.replace('\r', '') #avoid return problems
                    sline = sline.replace('\n', '') #avoid new line problems
                    if len(sys.argv) >= 4: #detect the custom separator argument
                        dictionary = sline.split(str(sys.argv[3])) #use custom separator
                    else:
                        dictionary = sline.split('\t') #use tab by default
                    if len(sys.argv) >= 5: #check if reverse mode is in arguments
                        if sys.argv[4] == "-r":
                            newLine = newLine.replace(dictionary[0],dictionary[1]) #use the first column as old string
                        else:
                            newLine = newLine.replace(dictionary[1],dictionary[0]) #in case that 4th arguments is not -r use default mode
                    else:
                        newLine = newLine.replace(dictionary[1],dictionary[0]) #use the first column as new string
                print newLine #print in console to operate with > to another file.
                   
                    
                    
                
            
                

else: #show a help if the script is not properlly called
    print 'This script need the follow arguments: tablefile.txt filename.txt '
    print '\nExample:'
    print 'python replaceLookTable.py table.txt fasta.fa'
    print '\twhere "table.txt" is a file that contain two columns separed by a TAB, '
    print '\tthe first column is the new text and second column is the old text'
    print '\nExample 2:'
    print 'python replaceLookTable.py table.txt fasta.fa ","'
    print '\t'+R'where "," is the separator [by default is "\t" meaning TAB]'
    print '\nExample 3:'
    print '\tpython replaceLookTable.py table.txt fasta.fa $\'\\t\' -r'
    print '\twhere $\'\\t\' (note the single quotation!) is the separator for TAB (must be included if -r argument is used) and'
    print '\twhere "-r" is reverse mode, where the first column is the old text and second column is the new text'
    print '\t'+R'Any special argument like \t \' \" must be included in single quotations and $ as prefix'

    

