#!/usr/bin/python3
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------
# ConvertFileUsingAlterAPI coded by Carlos Alonso Maya Lastra - 2017
#
# Performs multiple convertion of file format using ALTER API (Glez-Peña 2010)
# More information about the script in --help or http://camayal.info/scripts.htm
# More information about the ALTER API in http://sing.ei.uvigo.es/ALTER/api/
#-----------------------------------------------------------------------------


import os, httplib, urllib, argparse
from os import listdir
from os.path import isfile, join

# Read arguments to change options

parser = argparse.ArgumentParser(description='''This script permits convert
                                formats of DNA matrixes using the ALTER API
                                (Glez-Peña 2010) for all files contained in
                                one folder.                                
                                All options used by this script are original
                                of the ALTER API. 
                                Please check the manual of the original API
                                at: http://sing.ei.uvigo.es/ALTER/api/ to use
                                the current options for each parameter.
                                ''',
                                 epilog='''
                                 If you use this script you should citate the
                                 original API that it uses:
                                 D. Glez-Peña. Gómez-Blanco; M. Reboiro-Jato;
                                 F. Fdez-Riverola; D. Posada (2010) ALTER:
                                 program-oriented format conversion of DNA
                                 and protein alignments. Nucleic Acids Research.
                                 Web Server issue. ISSN: 0305-1048
                                 http://dx.doi.org/10.1093/nar/gkq321,
                                ''',
                                 usage='%(prog)s [any argument...] - if a argument (a.k.a parameter) is not declared, default value will be used')
parser.add_argument('--autodetect',
                    type=str,
                    default="true", 
                    dest="autodetect",
                    metavar="<true, false>",
                    help="Autodetect input so/program/format (Default: true)" )
parser.add_argument('--inO',
                    type=str,
                    default="windows", 
                    dest="inO",
                    metavar="<windows, linux, macos>",
                    help="Input operating system (Default: windows)" )
parser.add_argument('--inP',
                    type=str,
                    default="muscle", 
                    dest="inP",
                    metavar="<clustal, mafft, tcoffee, muscle, probcons>",
                    help="Input program (Default: muscle)" )
parser.add_argument('--inF',
                    type=str,
                    default="nexus", 
                    dest="inF",
                    metavar="<aln, fasta, gde, msf, nexus, phylip, pir>",
                    help="Input format (Default: nexus)" )
parser.add_argument('--gapsAsMissing',
                    type=str,
                    default="false", 
                    dest="gapsAsMissing",
                    metavar="<true, false>",
                    help="Treat gaps as missing data in haplotype collapsing (Default: false)" )
parser.add_argument('--limit',
                    type=int,
                    default=0, 
                    dest="limit",
                    metavar="<value>",
                    help="Collapse sequences whose differences are less than this value (Default: 0)" )
parser.add_argument('--outF',
                    type=str,
                    default="phylip", 
                    dest="outF",
                    metavar="<aln, fasta, gde, mega, msf, nexus, phylip, pir>",
                    help="Output format (Default: phylip)" )
parser.add_argument('--outO',
                    type=str,
                    default="linux", 
                    dest="outO",
                    metavar="<windows, linux, macos>",
                    help="Output operating system (Default: linux)" )
parser.add_argument('--outP',
                    type=str,
                    default="phyml", 
                    dest="outP",
                    metavar="<general, jmodeltest, mrbayes, paml, paup, phyml, prottest, raxml, tcs, bioedit, se-al, mega, mesquite, splitstree, dnasp, codabc, clustal, mafft, muscle, probcons, tcoffee, gblocks, seaview, trimal>",
                    help="Output program (Default: phyml)" )
parser.add_argument('--ext',
                    type=str,
                    default="phy", 
                    dest="ext",
                    metavar="<any extension (ex: phy, nex)>",
                    help="Extension for the result file (Default: phy)" )
parser.add_argument('--sequential',
                    type=str,
                    default="false", 
                    dest="sequential",
                    metavar="<true, false>",
                    help="Output in sequential form (ex: NEXUS, PHYLIP) (Default: false)" )
parser.add_argument('--version',
                    action='version',
                    version='%(prog)s 1.0 by Carlos Alonso Maya Lastra - April 2017')
args = parser.parse_args()


# This would give location of the current directory
mypath = os.getcwd()

# This charte the function listdir and filter only files
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# Define some global vars
ext = args.ext


# Put into sequence each file into the directory and call ALTER API
for w in onlyfiles:
    # Only process other than .py file
    if not w.lower().endswith((ext , ".py")):
        sequence = open(w).read()
        print "Processing: " + w
        #config parameters
        params = urllib.urlencode({
          'autodetect': args.autodetect,
          'inO': args.inO,
          'inP': args.inP,
          'inF': args.inF,
          'sequential': args.sequential,
          'gapsAsMissing': args.gapsAsMissing,
          'limit':args.limit,
          'outF': args.outF,
          'outO': args.outO,
          'outP': args.outP,
          'sequence':sequence})
        # Declare result file name based on the original plus extention
        resultfilename = w + "." + ext
        if os.path.isfile(resultfilename):
            print "Skipping, file already converted"
        else:    
            print "Connecting with sing.ei.uvigo.es..."   
            # Make the request
            headers = {"Content-type": "application/x-www-form-urlencoded","Accept": "text/plain"}
            conn = httplib.HTTPConnection("sing.ei.uvigo.es")
            conn.request("POST", "/ALTER/api/convert", params, headers)
            response = conn.getresponse()
            data = response.read()

            if "EXCEPTION PROCESSING REQUEST" not in data: 
                # print the data but split the console result and only put the file
                responsesplited = data.split("----- Converted Sequence ----\n")
                resultfile = open(resultfilename, "w")
                resultfile.write(responsesplited[1])
                resultfile.close()
                conn.close()
                print "Result saved as: " + resultfilename                
            else:
                resultfile = open(resultfilename + ".ERROR.log", "w")
                resultfile.write(data)
                resultfile.close()
                print "Failed, check error in" + resultfilename + ".ERROR.log"
                

print "End of script"


        
