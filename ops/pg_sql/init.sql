CREATE DATABASE mysite;
CREATE DATABASE test_mysite;

CREATE ROLE dbuser WITH LOGIN PASSWORD 'dbuser';

GRANT ALL ON DATABASE mysite TO dbuser;
GRANT ALL ON DATABASE test_mysite TO dbuser;

ALTER DATABASE mysite OWNER TO dbuser;
ALTER DATABASE test_mysite OWNER TO dbuser;

ALTER USER dbuser CREATEDB;
