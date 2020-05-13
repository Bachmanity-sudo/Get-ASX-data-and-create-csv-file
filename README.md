# Grab-ASX-data
Powershell and Python script to quickly create a .csv file with other 10 years of ASX data

1. Setup folders.  Suggested: C:\ASX_DATA\DATA, C:\ASX_DATA\ZIPPED, C:\ASX_DATA\UNZIPPED. 

2. Navigate to https://www.asxhistoricaldata.com/ (this site contains over 10 years of free ASX data which is current to last Friday and is updated every Sunday).

3. Download all ASX data required to /ZIPPED directory.

4. Set variables (file locations) for powershell script "unpacker.ps1".  

5. Run powershell script "unpacker.ps1".  This will unzip all files and copy daily .txt files in /DATA
  directory.
  
6. Set variables (file locations) for python script “merge.py”.

7. Run python script “merge.py”.  This will merge all daily .txt files and create a merged .txt and merged .csv file. (this 
  will take about 110 seconds for 10 years of data).

8. Happy stock analysis and trading!
