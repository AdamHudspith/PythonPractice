"""
Script : MySQLInterface
Version : 1.0
Purpose : To provide functions to assist with connecting to MySQL Databases including

> establish_connection()
> run_query()
> close_connection()
> setup_logging()

There are 3 states of logging that can be used :

    > DEBUG - All logging enabled, including parameterrs used in each function
    > INFO - Some of the additional logging added to give indicators of what worked
    > ERROR - Just the errors

"""
# import statements
import logging
from datetime import datetime
import mysql.connector
# function to establish a connection to a MySQL Database, returns a connection variable
def establish_connection(db_user,db_password,db_host,database_schema):
    """ Establishing a connection with a return connection object """
    try:
        # establish connection using DB User, Password , Host IP Address & database schema
        logging.debug("Attempting to establish connection with the following details ... ")
        logging.debug("Database User : %s" , db_user)
        logging.debug("Database Password : %s" , db_password)
        logging.debug("Database Host/IP Address : %s" , db_host)
        logging.debug("Database schema : %s" , database_schema)
        connection = mysql.connector.connect(user=db_user, password=db_password,
                                    host=db_host,
                                    database=database_schema)
        logging.info("Connection has been established at time %s" , datetime.now())
        return connection
    except mysql.connector.Error as err:
        # error handling for access denied or the database connection error
        logging.error(err)
        raise SystemExit from err
# function to run a query to a MySQL database, returns a cursor variable
def run_query(connection,query):
    """ Running a Query with a return cursor """
    try:
        logging.debug("Connection  -> %s" , connection)
        logging.debug("Query to be executed -> %s" , query)
        results = connection.cursor()
        results.execute(query)
        logging.info("Query has been run successfully at %s" , datetime.now())
        return results
    except mysql.connector.Error as err:
        logging.error(err)
        raise SystemExit from err
# function to close the provided connection details
def close_connection(connection):
    """ Closing a provided connection object """
    try:
        connection.close()
        logging.info("Connection has been closed successfully at %s" , datetime.now())
    except mysql.connector.Error as err:
        logging.error(err)
        raise SystemExit from err
# establishing log files
def setup_logging(log_file,log_level):
    """ Setting up logging for the above 3 functions """
    logging.basicConfig(filename=log_file, level=log_level)
    # setting up a basic logging file with 3 states
