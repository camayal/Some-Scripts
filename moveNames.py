#!/usr/bin/python
#
#moveNames
#
#Author: Carlos Alonso Maya Lastra - 2018
#Description: Script useful for moving parts of the name in a file like fasta or fastq. 
#             It can rename an entire file (like fasta) from something like >ATG100X5_Sp1_Rand to >Sp1_ATG10X5_Rand using the pattern "2_1_3"
#             moving the "elements" in the name knowing the separator

import sys

if len(sys.argv) >= 4:  #verify all mandatory arguments are in the line           
    #with open("renamed_" + sys.argv[1], 'w') as outfile: #open or create new file for the result
    with open(sys.argv[1], 'r') as f: #open the file (argv[1])
        for nline, line in enumerate(f, start=1): #move line by line
            line = line.replace('\r', '') #avoid return problems
            line = line.replace('\n', '') #avoid new line problems
            if len(sys.argv) == 5: #detect if a different identificator is indicated as optional
                identificator =  str(sys.argv[4])     #use the custom identificator
            else:
                identificator = ">" #by default use fasta identificator
            if line.find(identificator) == 0: #process line only if is a identificator                     
                #print '\rLine: ', nline, #progress notification
                splitedName = line.split(sys.argv[2]) #split the original name
                splitedName[0] = splitedName[0].replace(identificator,'') #delete the identificator from the first element
                splitedPattern = sys.argv[3].split(sys.argv[2])  #split the pattern for the new name
                resultLine = "" #create empty var for the result
                for num, element in enumerate(splitedPattern, start=1): #organice the name using the pattern desired
                    if num > 1: #define if nee or not a separator
                        separatorForResult = str(sys.argv[2])
                    else:
                        separatorForResult = ''
                    if element.isdigit(): #detect if is a number in the pattern
                        intElement = int(element) - 1 #ajust the number entered with a 0 base array index
                        if intElement >= len(splitedName): #detect if the element (pattern) is in the name
                            IncludeSeparator = False #if is out the index ignore it and flag false the separator
                        else: #if is in the index boundaries do the movement
                            resultLine += separatorForResult + str(splitedName[intElement])
                            IncludeSeparator = True #and activate the flag for include the separator
                    else: #if is not a number, use the string
                        resultLine += separatorForResult + str(splitedPattern[num - 1])
                        IncludeSeparator = True
                #outfile.write(identificator + resultLine + '\n')
                print identificator + resultLine
            else:
                #outfile.write(line + '\n')   #write line in the result file if it does not have a indentificator
                print line
            #print '\rFinished: renamed_' + sys.argv[1] + ' was created'
                

else: #show a help if the script is not properlly called
    print 'This script need the follow arguments: \nfilename, separator (- _  |), pattern to rename (see the example and use the same separator), \n[optional: identifier  (> or @ or ;)]'
    print '\nExample 1:'
    print 'python moveNames.py fasta.fa _ "2_1"'
    print '\tOld name:'
    print '\t>ATG10442_SP1'
    print '\tNew name:'
    print '\t>SP1_ATG10442'
    print '\tWhere "1" = ATG10442 and "2" is SP1 in the old name'
    print '\nExample 1b:'
    print 'python moveNames.py fasta.fa _ "1_2"'
    print '\tOld name:'
    print '\t>ATG10442_SP1'
    print '\tNew name:'
    print '\t>ATG10442_SP1'
    print '\tThe new and old name are the same'
    print '\nExample 2:'
    print 'python moveNames.py fasta.fa _ "2_3_1_something"'
    print '\tOld name:'
    print '\t>ATG10442_SP1_iqIN'
    print '\tNew name:'
    print '\t>SP1_iqIN_ATG10442_something'
    print '\t>where "something" is any text, it can be in any position'
    print '\nExample 2:'
    print 'python moveNames.py fasta.fastq _ "2_1" "@"'
    print '\tOld name:'
    print '\t@SEQ1_IDx'
    print '\tNew name:'
    print '\t@IDx_SEQ1'
    print '\t>where "@" is identifier for the description line in fastq, by default the script search for ">"'

