CREATE TABLE if not exists dsi_gmail;
use dsi_gmail;

CREATE TABLE IF NOT EXISTS company_gmail(
	emailid varchar(50),
	pwd varchar(50)
);

INSERT INTO company_gmail VALUES('datasyncinternational@gmail.com', 'DataSync#Abhi#Arm#Zai');
COMMIT;