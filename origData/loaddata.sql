SET autocommit=0;

/* load dictionary in npi database */
/* 
american-english
bfname.txt
gfname.txt
lastname.txt
GeoName.csv
*/

LOAD DATA LOCAL INFILE '/home/lancer/workspace.2016/ProviderMatch/origData/american-english' 
INTO TABLE jms_npi.DICTIONARY 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n'  
( @var ) set word_from = 'ENGDICT', word = upper(@var)  ;

LOAD DATA LOCAL INFILE '/home/lancer/workspace.2016/ProviderMatch/origData/lastname.txt' 
INTO TABLE jms_npi.DICTIONARY 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n'  
( @var1, @var2, @var3, @var4 ) set word_from = 'LASTN',  word = upper(@var1), freq = @var2 * 1000  ;

LOAD DATA LOCAL INFILE '/home/lancer/workspace.2016/ProviderMatch/origData/gfname.txt' 
INTO TABLE jms_npi.DICTIONARY 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n'  
( @var1, @var2, @var3, @var4 ) set word_from = 'GIRLFN',  word = upper(@var1), freq = @var2 * 1000  ;


LOAD DATA LOCAL INFILE '/home/lancer/workspace.2016/ProviderMatch/origData/bfname.txt' 
INTO TABLE jms_npi.DICTIONARY 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n'  
( @var1, @var2, @var3, @var4 ) set word_from = 'BOYFN',  word = upper(@var1), freq = @var2 * 1000  ;

LOAD DATA LOCAL INFILE '/home/lancer/workspace.2016/ProviderMatch/origData/GeoName.csv' 
INTO TABLE jms_npi.DICTIONARY 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n'  
( word, freq ) set word_from = 'GEONAME' ;



/*geoname come from BGN */

LOAD DATA LOCAL INFILE '/home/lancer/workspace.2016/ProviderMatch/origData/GeoName.csv' 
INTO TABLE jms_npi.NPI_WORD_FREQ 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n'  
( word, freq) set cat = 'GEON'  ;


/* load freq word in npi database */
/*
Address_City_NameDict.csv
Address_First_LineDict.csv
Address_Second_LineDict.csv
Provider_First_Name.csv
Provider_Last_Name.csv
Provider_Organization_NameDict.csv
*/

LOAD DATA LOCAL INFILE '/home/lancer/workspace.2016/ProviderMatch/origData/Address_City_NameDict.csv' 
INTO TABLE jms_npi.NPI_WORD_FREQ 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n'  
( word, freq) set cat = 'CTN'  ;

LOAD DATA LOCAL INFILE '/home/lancer/workspace.2016/ProviderMatch/origData/Address_First_LineDict.csv' 
INTO TABLE jms_npi.NPI_WORD_FREQ 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n'  
( word, freq) set cat = 'AFL'  ;

LOAD DATA LOCAL INFILE '/home/lancer/workspace.2016/ProviderMatch/origData/Address_Second_LineDict.csv' 
INTO TABLE jms_npi.NPI_WORD_FREQ 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n'  
( word, freq) set cat = 'ASL'  ;

LOAD DATA LOCAL INFILE '/home/lancer/workspace.2016/ProviderMatch/origData/Provider_First_Name.csv' 
INTO TABLE jms_npi.NPI_WORD_FREQ 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n'  
( word, freq) set cat = 'PFN'  ;

LOAD DATA LOCAL INFILE '/home/lancer/workspace.2016/ProviderMatch/origData/Provider_Last_Name.csv' 
INTO TABLE jms_npi.NPI_WORD_FREQ 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n'  
( word, freq) set cat = 'PSN'  ;

LOAD DATA LOCAL INFILE '/home/lancer/workspace.2016/ProviderMatch/origData/Provider_Organization_NameDict.csv' 
INTO TABLE jms_npi.NPI_WORD_FREQ 
FIELDS TERMINATED BY ',' ENCLOSED BY '"'  LINES TERMINATED BY '\n'  
( word, freq) set cat = 'PON'  ;






