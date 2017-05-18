import sys;
import string;

if len(sys.argv) != 2:
	exit();
	
filename = sys.argv[1];
nb_img = 0;

f = open(filename, "rb");
data = f.read();
png_header = b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a";
png_end = b"IEND";

start = data.find(png_header);
while start != -1:
	end = data.find(png_end)+8;
	pngfile = data[start:end];
	data = data[end:-1];
	o = open("img"+str(nb_img)+".png", "wb");
	o.write(pngfile);
	o.close();
	nb_img+=1;
	start = data.find(png_header);