CREATE DATABASE IF NOT EXISTS ADMIN_DB;
USE ADMIN_DB;

CREATE TABLE IF NOT EXISTS administrators (
        NAME VARCHAR(30) NOT NULL,
        USERNAME VARCHAR(30) PRIMARY KEY,
        PASSWORD VARCHAR(128) NOT NULL,
        PASSWORD_SALT VARCHAR(128) NOT NULL UNIQUE,
        SECURITY_KEY VARCHAR(128) NOT NULL);

INSERT INTO administrators VALUES('Abhijeet', 'abhijeet', '9b3a9c1f823a6dcade45d44f7b211604d1f49fa206217fe6e266f46c801df4c06361bc05ee2ed4bd4efa368dec76391f9c5bbcbd603a18c5fd74e312302f163b', 'Jb^@ZNE*j7z6ooAuBM(3*!8wlhXnI6CYuof1pGojA#EXCeYb#G9uqhUOrj#U8lWC2T26r8Jxmz#MUCF#^n(5Bhyc)8UsIi6gcJNU0!v06hq9P1rdvS$X%2nzfeWdYmEh', '5c8825996e27e8d2e8816ac0406707bffaf99190b6784a9280868bb09d4207a96ef25334f382d59d028f1e744665fd62e8714ed0d89d093373beb9abf3f82fdc');

INSERT INTO administrators VALUES('Armaan', 'armaan', '09a4f09e84fd00d3b79b027cee5ecf0e886b78fe445c786497e4c1cbc3e19a120cc09893b5dbab9402cb83c86e153b99c6d8560855d318fac53bc4ae531ea5c3', '3gsDhx%yjSCrLfK6%VE8^6s7wis7Y^zOJAp&&s2cZt)B^I)x3zmE#vXtqr4Jnu4*6^J6UmAwmbZAPs^DpMzhy()wnn0uS(QxmC&Tc07jxngdZ2vnjYoH5zb##ozOOHa9', '5c8825996e27e8d2e8816ac0406707bffaf99190b6784a9280868bb09d4207a96ef25334f382d59d028f1e744665fd62e8714ed0d89d093373beb9abf3f82fdc');

INSERT INTO administrators VALUES('Zaid', 'zaid', '1faf308374a2206e31a137c1afbf5caa067c9ea62b40c4d04f76d9e8e1b3c2123b5549eac035d9b9e9592b347239ce6db90493cb1c60a4162439b0dfb883fedf', 'D(q2dMY#oWQ@^$U1B*aA^FHxByjnjwL8RhLkrTTYE&Yz1lTvhxZebbyd9P(H@tziQLG^guxWJj!M&m6mvUfGDLrOZlv*O8jCkdUc!V5FTzh0Vhnm%UelJI#hr0t%Y5RN', '5c8825996e27e8d2e8816ac0406707bffaf99190b6784a9280868bb09d4207a96ef25334f382d59d028f1e744665fd62e8714ed0d89d093373beb9abf3f82fdc');

COMMIT;