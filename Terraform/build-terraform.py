#!/usr/bin/python
import argparse
import ConfigParser
import stat
import os
__author__ = 'MCE123'

#Define Text Properties
class bcolors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

print '\b'
print bcolors.BOLD + 'build-terraform.py by Patrick R. McElhiney, MCE123 (www.mce123.com)' + bcolors.END
print '\b'

#Parse Input Variables
parser = argparse.ArgumentParser(description='This is a build-terraform script by MCE123.')
parser.add_argument('-f','--file', help='Input File Name',required=True)
parser.add_argument('-c','--classname',help='Class Name', required=False)
args = parser.parse_args()

#Read Configuration File and Set Environmental Variables
config = ConfigParser.RawConfigParser()
config.read('build-terraform.cfg')
path_to_terraform = config.get('Config', 'path_to_terraform')
root_path = config.get('Config', 'root_path')
terraform_mode = config.get('Config', 'terraform_mode')
terraformCommand = path_to_terraform + ' ' + terraform_mode

#Define classname and Create Root Sub-Directory For All Project Files
if args.classname is not None:
    classname = args.classname
    file_path = './' + classname + '/'
else:
    classname = os.path.splitext(os.path.basename(args.file))[0].strip('-input')
    file_path = './' + classname + '/'
try:
    os.makedirs(file_path)
except OSError:
    pass

#Read The Input File
fh=open(args.file,'r')
c=fh.readlines()
fh.close()
#Read The main.tf.template File
template_file=open('main.tf.template','r')
template_data=template_file.readlines()
template_file.close()
#Read The setup-env.sh.template File
sh_template_file=open('setup-env.sh.template','r')
sh_template_data=sh_template_file.readlines()
sh_template_file.close()
#Open a New build-terraform_<classname>.sh File
bt_sh_file = 'build-terraform_' + classname + '.sh'
bt=open(bt_sh_file,'w')
bt.write('#!/bin/bash\n\n')
#chmod build-terraform.sh to allow execution
st = os.stat(bt_sh_file)
os.chmod(bt_sh_file, st.st_mode | stat.S_IEXEC)
student_count = 0
#Parse Input
for line in c:
    #Create the Student Id
    thisline=line.split('\n')[0]
    studentid=thisline.split("@")[0]
    studentid = studentid.translate(None, ' ?.!/;:')
    student_file_path = file_path + studentid + '/'
    #Make Student Directory
    try:
        os.makedirs(student_file_path)
    except OSError:
        pass
    #Create main.tf File From main.template, and setup-env.sh from setup-env.sh.template
    student_maintf_filepath = student_file_path + 'main.tf'
    student_setupenv_filepath = student_file_path + 'setup-env.sh'
    #Open Student's main.tf and setup-env.sh Files For Writing
    fs=open(student_maintf_filepath,'w')
    sh=open(student_setupenv_filepath,'w')
    #Iterate For Each Line for main.tf.template to Student's main.tf
    for readline in template_data:
        fs.write(readline.replace("{% username %}", studentid))
    fs.close()
    #Iterate For Each Line for setup-env.sh.template to Student's setup-env.sh
    for read_sh_line in sh_template_data:
        sh.write(read_sh_line.replace("{% username %}", studentid))
    sh.close()
    print bcolors.GREEN + 'Created User Data for ' + studentid + ' in ' + student_file_path[1:] + bcolors.END + '\b'
    #Write to build-terraform.sh
    bt.write('cd ' + root_path + student_file_path[1:] + '\n')
    bt.write('echo $PWD\n')
    bt.write(terraformCommand + '\n')
    student_count+=1
#Close build-terraform.sh File
bt.close()
#Setup Bash Session
os.system('cd ' + root_path)
print bcolors.YELLOW + 'Created Shell Script: ' + bt_sh_file + bcolors.END
print '\b'
print 'Run the Shell Script manually: ./' + bt_sh_file
print '\b'
print bcolors.BOLD + bcolors.RED + 'WARNING: Running the Shell Script successfully will create ' + str(student_count) + ' AWS instances with the specifications in main.tf.template!' + bcolors.END
print '\b'
#Enable the following line to automatically run the Shell Script
#os.system('./' + bt_sh_file)



