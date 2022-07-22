import subprocess, datetime, os, time, signal , sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from optparse import OptionParser
from tqdm import tqdm



__cmd__ = "uncompyle6 -o "
__version__ = "0.0.1"
__timeout__ = 35 




def logo():
    print("""
                                                 .__            _____        .__  .__   
  __ __  ____   ____  ____   _____ ______ ___.__.|  |   ____   /  |  |_____  |  | |  |  
 |  |  \/    \_/ ___\/  _ \ /     \\____ <   |  ||  | _/ __ \ /   |  |\__  \ |  | |  |  
 |  |  /   |  \  \__(  <_> )  Y Y  \  |_> >___  ||  |_\  ___//    ^   // __ \|  |_|  |__
 |____/|___|  /\___  >____/|__|_|  /   __// ____||____/\___  >____   |(____  /____/____/
            \/     \/            \/|__|   \/               \/     |__|     \/           


    
                                                                                Version {_}
                                                                                Writen by 4me
    
    """.format(_ = __version__))



def TIMEOUT_COMMAND(command, timeout): 
    """call shell-command and either return its output or kill it
    if it doesn't normally exit within timeout seconds and return None""" 
    import subprocess, datetime, os, time, signal 
    cmd = command.split(" ") 
    start = datetime.datetime.now() 
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE) 
    while process.poll() is None: 
        time.sleep(0.2) 
        now = datetime.datetime.now() 
        if (now - start).seconds> timeout: 
            os.kill(process.pid, signal.SIGKILL) 
            os.waitpid(-1, os.WNOHANG) 
            return None 
    return process.stdout.readlines() 




def main():
    usage="Usage: python %prog -p <filepath> -t <threads>"
    parser=OptionParser(usage=usage)
    parser.add_option("-p","--path",type="string",dest="filepath",help="pyc/pyo file path ")
    parser.add_option("-t","--threads",type="int",dest="threads",help="threads number")
    (options,args)=parser.parse_args()

    if len(sys.argv) ==1:
        print(parser.print_help())
        sys.exit()

    
    _filepath=options.filepath
    _threads=options.threads

    if (_filepath==None):
        print("[!] -------------- filepath is in need :)----------------")
        sys.exit()
    
    if (_threads == None):
        _threads = 5
        #判断输入不为空
    pool = ThreadPoolExecutor(_threads)
    targets = []
    for root, dirs, files in os.walk(_filepath):
        for name in files :
            filename  =  os.path.join(root, name)
            # if "migrations/" not in filename and filename.endswith(".pyc"):
            if filename.endswith(".pyc") or filename.endswith(".pyo"):
                cmd_line = __cmd__ + filename[:-1] + " " + filename
                targets.append(cmd_line)

    log_name = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")+".log"
    task_list = set()
    for cmd_line in targets:
        task_list.add(pool.submit(TIMEOUT_COMMAND, cmd_line, __timeout__))

    print("Your absolute path is " + os.path.abspath(_filepath) + "\n")
    print("\n")
    with open(log_name,"a") as fp:
        for future in tqdm(as_completed(task_list), total=len(task_list)):
            res_text  = future.result()
            if res_text == None:
                continue
            res_text = res_text[-2].decode().strip().replace("-","") +  "           "  + res_text[-1].decode().strip() + "\n"
            fp.write(res_text)
    
    if os.path.exists(log_name):
        print("\n")
        print("[+] "+log_name + " ----> The log file is created!")
        print("\n")





if __name__ == "__main__":
    logo()
    main()

    
    



                        
                    
            











                
     
     

