from django.shortcuts import render
import argparse
# Create your views here.

class IndexView(TemplateView):
    template_name = 'main.html'
    __author__ = 'MCE123'
    parser = argparse.ArgumentParser(description='This is a demo script by MCE123.')
    parser.add_argument('-f','--file', help='Input File Name',required=True)
    #parser.add_argument('-o','--output',help='Output file name', required=True)
    args = parser.parse_args()
    fh=open(args.file,'r')
    c=fh.readlines()
    fh.close() 
    s=''
    for line in c:
        thisline=line.split('\n')[0]
        name=thisline.split("@")[0]
        print(name)
        print '<<insert per instance code here>>'
        print '\b'
    print '\b'
    print '<<insert final commands here>>'


    


