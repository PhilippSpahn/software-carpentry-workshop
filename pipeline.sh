echo Cleaning up....
rm *.csv
echo Downloading ...
curl https://github.com/zonca/swcarpentry-workshop-pandas/blob/master/rawdata/rawdata.zip?raw=true -o rawdata.zip -L
echo Unpacking ...
unzip rawdata.zip
echo Deleting temporarys...
rm *.tmp
echo Renaming ...
rm *.txt *.csv