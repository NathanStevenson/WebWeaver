#!/bin/bash
DB_USER=$1
DB_NAME=$2

# Drop the database
sudo -u postgres psql -c "DROP DATABASE IF EXISTS $DB_NAME;"
# Drop the user (if no other databases depend on it) - add option to drop the user or not (may not want to if using other DB)
sudo -u postgres psql -c "DROP USER IF EXISTS $DB_USER;"