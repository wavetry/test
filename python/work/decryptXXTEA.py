#!/usr/python
# coding=utf-8
import os,shutil,sys,getopt
file_list = []
lua_dec_path = "D:/crack/luadecode/LuaDecode.exe"
root_path = ""
dst_path = ""
key = ""
sign = ""

def search(path):
    global root_path
    dirs_files = os.listdir(path)
    for file_name in dirs_files:
        full_path = os.path.join(path,file_name)

        if os.path.isdir(full_path):
            search(full_path)
        else:
            file_ext = file_name.split(".")[-1]
            if file_ext == "luac":
                relative_path = full_path[len(root_path):]
                
                target_path = dst_path + relative_path
                target_path = target_path[:-1]
                print("target_path",full_path,target_path)

                dirname = os.path.dirname(target_path)
                print("dirname",dirname)
                if not os.path.exists(dirname):
                    os.makedirs(dirname)
                # ret = os.system("%s %s %s %s %s" % (lua_dec_path,full_path,target_path,sign,key))
                # print(ret)

if __name__ == '__main__':
    argv = sys.argv
    try:
        opts, args = getopt.getopt(argv[1:], 'sdkg:', ['srcph=','dstph=','key=','sign='])
    except getopt.GetoptError, err:
        print str("err====>",err) 
        sys.exit(2)
    for o, a in opts:
        if o in ('-s', '--srcph'):
            root_path = a
        if o in ('-d', '--dstph'):
            dst_path = a
        if o in ('-k', '--key'):
            key = a
        if o in ('-g', '--sign'):
            sign = a
    
    base_path = "D:/download/assets/"
    root_path = base_path + "src"
    dst_path = base_path + "decrypt/src/"
    # sign=  "XXTEASIGN220151130"
    # key=  "fytx220151130"
    sign="20180309zslm"
    key="20180309zslm"
    # sign="kuaiyin4gfs4vm87bfqol2974vbel"
    # key="94h389feg396hjd41nv4cfd94nv5f"
    
    print ("root_path:",root_path)
    print ("dst_path:",dst_path)
    print ("key:",key)
    print ("sign:",sign)

    if None != root_path:
        search(root_path)
        ret = os.popen("%s %s %s %s %s" % (lua_dec_path,root_path,dst_path,sign,key)).read()
        print(ret)

    raw_input('Press Enter to exit...')


