# http-validator


##Run
To run this tool download the http-validator.tar.gz file from the repository via <insert link here when uploaded>

Untar the file and navigate your terminal to be in the same window as the request_maker.py script 
and create a text file containing urls separated by a new line like so

```text
www.google.com
www.yahoo.com
www.oracle.com
```

on the terminal run the program by typing 

```bash
python request_maker.py -file <name of file containing urls>.txt
```

You should see output on your command line along with generated json report files
for each url in the same directory as it was ran. You will also see a file called Http-Status-Report.json
which includes details on how many responses of a particular status type were acrued 
