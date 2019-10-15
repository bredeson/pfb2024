Here are some of the TAs and Instructors favorite or most used unix commands


__Sofia__

`ls -lt | head`

list the contents of your directory with all the information sorted by most recent at the top, but only show me the top 10.

Simon suggests `ls -ltrh`  as an alternative, which lists all files so that the last file you modified shows up at the bottom of the list (just above the prompt) and prints file sizes in readable form e.g. '10M' for megabytes

`perl -pe 's/\r/\n/g' badfile > newfile`

Sometimes you have carriage returns instead of newline and you want to replace all of them. This command replaces all \r (carriage returns) with \n (newlines). The old file is not changed, but the new file has the changes. 



`date ; someCommand ; date`

This will print out the date and time before you run some script and after. Now you can see how long it took



`comm -[1][2][3] file1 file2`

Compares two **sorted** files and prints out content depending on the flags



`comm -3 file1 file2`

`-3` will print out only the shared lines
`-1` will print out the lines unique to file1
`-2` will print out the lines unique to file2





### Simon

Quick way to see sequence identifiers in a fasta file

`grep ">" sequences.fa`

### Joe


`paste file1.txt file2.txt`

This will join two files line by line and display on the screen

`column -t |less -S`

Makes a messy table have clean columns and presents it with an easily viewable scrolling display 

`zgrep -v "##" file.vcf.gz| column -t |less -S`

Display a vcf without all the header garbage

__Kirsten__

`cat file.txt | cut -f 1 | sort | uniq -c`

Cuts out the first column in a whitespace delimited file and pulls out and counts the unique elements

`cat file.txt | cut -f 1 | sort | uniq | wc -l`

Count the number of unique items in column one of your file.

`top`

Check the computational processing going on

`echo $PWD/file.txt`

Get the full path to the file you are working on
