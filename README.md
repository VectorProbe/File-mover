MoverScript.py is a script that checks each folder in a given directory for existing files (including folders) and then moves those discovered files into a specified directory. The script works as supposed to, but had a major flaw, which was that it only checks a folder and moves whatever is in there into the destination folder. 

Mover2.py was created to overcome this flaw. The script checks each folder in the given directory. If a folder is discovered, it opens that folder and does not just move the folder. It looks for files instead and in the absence of a file, it leaves without moving anything. When files are moved, they also are renamed a temporary name in numerical order.

The two scripts ultimately have their uses set apart, but the goal I had in mind was achieved with the Mover2.py
I had over 200 files that were each stored in a separate folder, with those files then stored in another folder and then ultimately stored in a folder named temp1.
The script had gone into each recursion and moved all the files into another destination folder named temp2 successfully. This made it easy to rename each of those files with my batch renamer script (https://github.com/VectorProbe/Batch-file-renamer-in-python).

Both scripts have been modified to fit and now only Mover2 works properly. Moverscript is going to need a fix, while using Mover2 requires the destinations to be swapped on each iteration. This project was abandoned since its creation on 25/06/2024 because its purpose was fulfilled, and was only uploaded to Github today, being the 7/30/2024.
