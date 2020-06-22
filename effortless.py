import os
import subprocess
import sys
import wget
import os
import requests
import time
from time import sleep
from multiprocessing.pool import ThreadPool
import shutil
from colorama import Fore, Back, Style
import fileinput
from pathlib import *
import pathlib
from sys import platform
from colorama import init
init()




def color_check():
	is_windows = sys.platform.startswith('win')
	if is_windows:
		G = '\033[92m'  # green
		Y = '\033[93m'  # yellow
		B = '\033[94m'  # blue
		R = '\033[91m'  # red
		W = '\033[0m'   # white
		try:
			import win_unicode_console , colorama
			win_unicode_console.enable()
			colorama.init()
			return G,Y,B,R,W;
		except Exception as e:
			print(e);
	else:
		yellowy
		G = '\033[92m'  # green
		Y = '\033[93m'  # yellow
		B = '\033[94m'  # blue
		R = '\033[91m'  # red
		W = '\033[0m'   # white
		def no_color():
			global G, Y, B, R, W
			G = Y = B = R = W = ''



def dependency_check():
    a=['apktool.jar', 'd2j-dex2jar.bat', 'jd-gui-1.5.1.jar', 'signapk.jar']

    for x in a:
        if x in os.listdir():
            #print(x)
            print( "[+] "+x + "-> " +"check done")
        else:
            print("[-] "+x +" -> "+ "not check done")
            print("[-------]"+ x + "->"+"  please download and put in this folder")
            exit(0)


#--------------------------------------------------------------------------------------------------------------------------------------------------------


def app_decompile():

    cmd ="java -jar" +" "+"apktool.jar d"
    cmd1 = "java -jar" +" "+"apktool.jar b --use-aapt2"
    global file
    global file1
    file = input("enter path name of file::\n")
    print("please wait your decompilation is in process")
    p = Path(file)
    print("[~~] input filename " +" "+str(p));
    a=p.name;
    #d=a+"1"+".apk"
    print(a);
    decompile=a.rsplit('.', 1)[0] ;
    c=decompile+"1.apk" ;
    print("[~~] Output filename " +" "+str(c));
    #print(c);
    #return_path =decompile+
    save_path = os.getcwd();
    b = "../"+decompile ;

    path2 =save_path+"/"+b ;
    status,result = subprocess.getstatusoutput(cmd +" "+file+" "+"-o"+path2+" "+"-f");
    print(result);
    return status,path2,p,decompile,cmd,cmd1,c,a;

#_________________________________________________________________________________________________________________________________________
def debug_check(path2):
     #status = ["True","False"]
     print("opening androidmainfest.xml file\n")
     f= open(path2+"/"+"AndroidManifest.xml","r");
     print(f.read());
     input("Press Enter to continue...");


#________________________________________________________________________________________________________________________________________
def extract_dex(p,decompile):
    print("extracting classes.dex file from  your build apk");
    extract_path ="../"+str(decompile)+"_"+"dex_files"
    print(extract_path)
    cmd3  =  "7za x"+" "+str(p)+" "+"-aoa"+" "+"classes*"+" "+"-o"+"."+"."+"/"+str(decompile)+"_"+"dex_files";
    #print(cmd3)
    #print(p,a)
    #print(str(p))
    status,result = subprocess.getstatusoutput(cmd3);
    print(status)
    print("please wait for 5 seconds")
    
    #print(result)
    return status,extract_path

#___________________________________________________________________________________________________________________________________
def final_part(extract_path):
    cmd0= "d2j-dex2jar"
    final_path="../final_output"
    for f in os.listdir(extract_path):
        if f.endswith(".dex"):
            b=os.path.join(extract_path,f)
            p = Path(b)
            a=p.name;
            print(a);
            print(p);
            status,result = subprocess.getstatusoutput(cmd0 +" "+ str(p) +" "+"-o"+" "+final_path+"/"+a+".jar");
            print(result)

    return final_path

        
        #return status,final_path

#_______________________________________________________________________________________________________________________________________
def open_jar(final_path):
    cmd0= "java -jar  jd-gui-1.5.1.jar"
    for f in os.listdir(final_path):
        if f.endswith(".jar"):
            b=os.path.join(final_path,f)
            p = Path(b)
            a=p.name;
            print(a);
            print(p);
            status,result = subprocess.getstatusoutput(cmd0 +" "+ str(p));
            print(result);




#____________________________________________________________________________________________________________________________________


#_________________________________________________________________________________________________________________________________

def main():

    #G,Y,B,R,W =color_check()
    
    #color_check()
    os.chdir(os.getcwd()+"/"+"TOOLS")
    dependency_check()
    print("[+] application decompilation process started")
    #x= app_decompile()
    status,path2,p,decompile,cmd,cmd1,c,a = app_decompile()
    #print(path2)
    #print(status)
    if status==0:
        print("app is decompile completely")
        print("[++] checking app is debuggable or not")
        debug_check(path2)
        print("unzipping apk file and extracting dex  files")
        status,extract_path=extract_dex(p,decompile)
        final_path=final_part(extract_path)
        open_jar(final_path)
      
     
        


    else:

        
        
        print("[-] some error comes sorry we are exiting");
        #print(Fore.RED + 'some red text') 
        exit(0)






if __name__ == '__main__':
    main()
