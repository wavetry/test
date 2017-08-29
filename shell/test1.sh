#!/bin/sh
cd ~
mkdir shell_tut
cd shell_tut
for((i=0;i<10;i++)); do
	touch test_$i.txt
done
name="test"
hello1="hello,"$name""
hello2="hello,${name}"
echo $hello1 $hello2