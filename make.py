import os,json,shutil,re,time
from pydub import AudioSegment

#---------------------------------------\
# YOU CAN EDIT THE FOLLOWING VARIABLES #|\
                                       #| |
packName='TestPack'                    #| |
                                       #| |
path="raw"                             #| |
convert_path='convert'                 #| |
output_path='build/'+packName          #| |
                                       #| |
package='net.mikoto.musicpack'         #| |
pack_format=5                          #| |
description='auto'                     #| |
                                       #| |
#\--------------------------------------\ |
# \______________________________________\|

content={}
num=0

def hub(filename,directory):
        if os.path.isdir(directory+'/'+filename):
                if filename==convert_path:
                        return
                new_path=os.path.join(directory,filename)
                print('进入'+new_path)
                for fn in os.listdir(new_path):
                        hub(fn,new_path)
                print('退出'+new_path)
        else:
                rawname=filename
                for i in re.findall('[^0-9a-zA-Z\-\._\/]',filename):
                        filename=filename.replace(i,"_")
                filename=filename.lower()
                os.rename(os.path.join(directory,rawname),os.path.join(directory,filename))
                if filename.endswith("ogg"):
                        ogg_handler(filename,directory)
                else:
                        convert(filename,directory)
def convert(filename,directory):
        try:
                end=filename.split('.')[-1]
                export_path=os.path.join(os.path.join(os.path.join(os.getcwd(),path),convert_path),filename.strip(end)+'ogg')
                try:
                        os.close(os.open(export_path,0))
                except:
                        print('正在转换：'+filename.strip('.'+end)+'    ['+end+'->ogg]')
                        s = AudioSegment.from_file(directory+'/'+filename,format=end)
                        
                        s.export(out_f=export_path, format="ogg")
                        print('转换成功')
        except BaseException as e:
                print(filename+' 转换失败：'+str(e))
                return
        try:
                ogg_handler(filename.strip(end)+'ogg',os.path.join(os.path.join(os.getcwd(),path),convert_path))
        except BaseException as e:
                print('载入出错：'+str(e))
                
def ogg_handler(filename,directory):
	global content,num
	filename = filename[:-4]
	content[filename]={'category':'record','sounds':[{'name':package+'/'+filename,'stream':True}]}
	new_path=os.path.join(os.getcwd(),output_path+'/assets/'+package+'/sounds')+'/'+filename+'.ogg'
	num+=1
	shutil.copyfile(os.path.join(directory,filename+'.ogg'),new_path)
try:
        os.makedirs(os.path.join(os.getcwd(),path+'/convert'))  
except:
        pass
try:
        os.makedirs(os.path.join(os.getcwd(),output_path+'/assets/'+package+'/sounds'))
except:
        pass
try:
        shutil.copyfile('pack.png',os.path.join(os.getcwd(),output_path)+'/pack.png')
except:
        pass

raw_files=os.listdir(os.path.join(os.getcwd(),path))

for filename in raw_files:
        hub(filename,os.path.join(os.getcwd(),path))

if description=='auto':
        description='§e'+packName+' §7- §b'+package+'\n§r'+str(num)+' songs in the pack'
intro={
  "pack": {
    "pack_format": pack_format,
    "description": description
  }
}

# 写入pack.mcmeta
f = open(os.path.join(os.getcwd(),output_path)+'/pack.mcmeta',"w")
f.write(json.dumps(intro))
f.close()

# 写入sounds.json
f = open(os.path.join(os.getcwd(),output_path+'/assets/'+package+'/sounds.json'),"w")
f.write(json.dumps(content))
f.close()

print('打包完成')
time.sleep(5)
