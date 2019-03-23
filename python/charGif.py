#!/usr/python
# coding=utf-8
### ffmpeg -i "Touhou - Bad Apple!!  PV.webm" -f mp3 -vn apple.mp3 可以输出音频，暂时没有用到
workdir = r'E:\gitproject\test\python\girl'
### 按灰度替换的字符列表
sortedCharDegreeList = ['M', 'W', '@', 'N', 'H', '%', 'X', '$', 'B', 'K', 'R', '#', 'E', 'U', 'Q', 'D', '&', 'F', 'w', '8', 'k', '9', '6', 'h', 'm', 'A', 'P', 'p', 'd', '*', 'V', 'g', 'Y', '0', '5', 'b', 'q', 'G', 'O', 'n', 'x', 'f', 'S', 'J', 'T', 'Z', '3', 'y', 'u', 'I', 'C', 'L', '2', 'a', ']', '[', '1', '?', 'l', 's', 'e', 'r', '|', '}', '{', 't', 'z', 'o', 'v', '4', '+', '/', 'i', 'j', '=', 'c', '7', '(', ')', '!', '\\', '_', '>', '<', ':', '-', '"', "'", ',', ';', '.', '^', '`', ' ']
charsIndexMax = len(sortedCharDegreeList) -1 
import os, glob, cgi
os.chdir(workdir)
from PIL import Image, ImageFont, ImageDraw
result = []
imgs = glob.glob('*.bmp')
imgs = sorted(imgs, key=lambda x: int(x.split('.')[0])) # 这里对图片路径进行了处理，取后缀前的数字值进行排序
#
for img in imgs:
    originalImage = Image.open(img)# 图片尺寸为(480, 360)
    grayImage = originalImage.resize((120, int(90/2))).convert('L')
    # 将图片尺寸缩小，即减少像素点，并转换为灰阶
    # int(90/2) 因为字符的高是长的两倍，由于之后是一个像素点替换为一个字符，所以提前将高缩小一倍
    resulttext = ''
    for row in range(grayImage.size[1]):
        for col in range(grayImage.size[0]):
            pixel = grayImage.getpixel((col, row))
            char = sortedCharDegreeList[int(pixel/255*charsIndexMax)] # 像素点值为0是黑色，255为白色
            resulttext += char
        resulttext += '\n'
    result.append(resulttext)
    print(img,'is done!')
#
head = '''
<html>
<head>
</head>
<style>
pre {display:none;font-family:simsun;font-size:14px; line-height:14px}
</style>
<script>
window.onload = function(){
    var pres = document.getElementsByTagName('pre');
    var i = 0;
    var play = function(){
        if(i > 0){
            pres[i-1].style.display = 'none';
        }
        pres[i].style.display = 'inline-block';
        i++;
        if(i == pres.length){
            clearInterval(run)
        }
    }
    run = setInterval(play, 30)
}
</script>
<body>
'''
foot = '''
<video width="480" height="360" controls="controls" autoplay="autoplay">
  <source src="../Bad Apple!!  PV.webm" type="video/webm" />
</video>
</body>
</html>
'''
with open('2.html','w') as f:
    f.write(head)
    for resulttext in result:
        f.write("<pre>")
        f.write(cgi.escape(resulttext))
        f.write("</pre>")
    f.write(foot)