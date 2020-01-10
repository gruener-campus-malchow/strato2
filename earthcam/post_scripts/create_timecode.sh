#!/bin/sh

for i in *jpg; 
do 

counter=$(printf %09d $x);

timecode=$(stat -c%y "$i"|cut -d'.' -f1); 
echo "$i - $timecode";

convert $i -geometry 1920x1080 -quality 100 -rotate 180 -fill yellow -pointsize 30 -gravity SouthWest -draw "text 15,15 'Modry Pavilon 2019'" $i

#convert $i -geometry 1920x1080 -quality 100 -rotate 180 -fill yellow -pointsize 30 -gravity SouthWest -draw "text 0,0 'Modry Pavilon 2019 `echo $timecode`'" $i


x=$(($x+1)); 
done

#motion_jpg_to_mpeg.sh 



