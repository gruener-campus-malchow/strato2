mkdir /tmp/links;
x=1; 
for i in *jpg; 
do counter=$(printf %09d $x); 
echo "$i - $counter";
ln "$i" /tmp/links/img"$counter".jpg; 
x=$(($x+1)); 
done

ffmpeg -framerate 11 -f image2 -i /tmp/links/img%09d.jpg -c:v libx264 -r 11 -pix_fmt yuv420p -profile:v main ./1day_modry_pavilon_$(date +"%Y-%d-%m_%H-%M").mp4;

rm /tmp/links/*;
