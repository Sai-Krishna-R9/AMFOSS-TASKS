
                                   #####LEVEL-1#######

in the task_01 there are 4 sectors and basically it has 10 files all of them have similar names and every file has same description so the usual cat command does not really work 
here!in the readme.md file there is a clue saying that if you use the command ./eat.sh <path to file> the file  shows a awakening flag if the right file is used or it shows 
nothing happens. i used ls -la to show the file and also the permission given to it like r,w and x so  i saw  devil_fruit_6.txt file to be in green color and also the permission 
given to it is different from others like in the description it says it has a freedom to change it forms like that so it is the only file to have these permission after i
 confirmed i used the./eat.sh sector_C/devil _fruit_6.txt and boom it awakened and gave the flag 


                                     ####LEVEL-2#####
In the level 2  first we have to export the flag we found in level 1 this checks the environment and ensures that we have completed the first level and give you the entry
there is a hidden folder in whiskey peak investigation when ls command is used It only shows The feast_manifest.txt but wwhen ls -a is used it shows the baroque_works_cache it 
starts with a .(dot ) cause it is hidden we again use ls -ls command to get the all the files including hidden files with their permissions.just as in  the level one here also 
there is only one file which has permission -rwx-rwxr-x and aslo it is in green in color the real message is some where in Marine intercept.log and bounty_hunter_feed.log there 
is a clue in the message itself to run diff to compare this two files and we and ther we can find baroque_Dial{split_timeline_misdirection} which is the level-2 flag 


                                       ####LEVEL-3###
the whole point of level 3 is to find a cypher tag the code we found in the whiskey peak is the clue to it the tag we want is in base 64 form which is used to convert any 
text or image to a form where only 64 characters are used it always end with= or == we use git checkout and add wax jungle in to the main branch
here we use grep command which is nothing but to find a specific file in a ton of files we use the base 64 form and grep command to search for the fragment file as it is said 
in the tasks description and i found the baroque works executive report also in the same file.
                                     #####level_4### 
In this city of water_7 there is a file we should find in the description it is said that they "stripped its identity" which means that we dont know what type of file it is 
now we will use the file command to know what type of file it is .it shows that it is in gzip form and also as bonus this command shows what it was called before it was renamed 
it was called as "step2_blueprints.tar" so now this gives a clue for us that to decompress it the tool for that is gunzip and we get a tar file if we do that now we have a 
zip file  we can unzip for extracting the files after doing so we get to see two files which are 
*hull_design/frame_specs.dat
*secret_link.txt
when we cat that secrent link.txt file we can see the PONEGLYPH_FRAGMENT_II="SwnbzptDiM3JSpvFiMuJ28PJzAlJ28VIzA=" 
                                                      PONEGLYPH_FRAGMENT_I  = "KjY2MjF4bW0lKzYqNyBsIS0vbTAtJTcnL"
                                     ########level_5######

