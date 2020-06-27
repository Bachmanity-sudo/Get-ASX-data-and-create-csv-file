# Grab-ASX-data

Python script, ver 1.2,  to quickly create a .csv file with over 10 years of ASX data

1. Navigate to https://www.asxhistoricaldata.com/ (this site contains over 10 years of free ASX data which is current to last Friday and is updated every Sunday).

2. Download all ASX data required to \ZIPPED folder.

3. Set location of zipped folder variable in python script, i.e. C:\ASX_DATA\ZIPPED

4. Run python script “unpacker_1.2.py”. This will unzip all files, then merge all daily .txt files and create a merged .txt and merged .csv file. (this will 
take about 110 seconds for 10 years of data).  Output files will be saved into default python working folder.

5. Happy stock analysis and trading!
