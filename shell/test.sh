#!/bin/bash
# author:菜鸟教程
# url:www.runoob.com
# function rm () {  
#     local path  
#     for path in "$@"; do  
#         # ignore any arguments  
#         if [[ "$path" = -* ]]; then :  
#         else  
#             local dst=${path##*/}  
#             # append the time if necessary  
#             if [[ -z "$dst" ]]; then  
#                 dst=$(echo $path | sed -e 's/\/$//')  
#                 dst=${dst##*/}  
#             fi  
#             while [ -e ~/.Trash/"$dst" ]; do  
#                 dst="$dst"-$(date +%Y-%m-%d-%H-%M-%S)  
#             done  
#             sudo mv "$path" ~/.Trash/"$dst"  
#         fi  
#     done  
# }  
alias
rm="mv
 -t ~/.Trash"
rm "test4.txt"

# funWithReturn(){
#     echo "这个函数会对输入的两个数字进行相加运算..."
#     echo "输入第一个数字: "
#     read aNum
#     echo "输入第二个数字: "
#     read anotherNum
#     echo "两个数字分别为 $aNum 和 $anotherNum !"
#     return $(($aNum+$anotherNum))
# }
# funWithReturn
# echo "输入的两个数字之和为 $? !"