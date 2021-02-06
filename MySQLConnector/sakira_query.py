import mysql_interface

# start of the main script
# establish logging
mysql_interface.setup_logging('sakira_query.log','ERROR')
# creating the connection
cnx = mysql_interface.establish_connection('SA','Password','127.0.0.1','sakila')
# run the query against the connection
query_results = mysql_interface.run_query(cnx,"select * from sakila.actor LIMIT 0, 1000")
# for loop takes the query results cursor and prints the details 
for (actor_id, first_name, last_name, last_update) in query_results:
  print("actor id '{}', first name '{}' , last_name '{}' , last_update '{}' ".format(
    actor_id, first_name, last_name, last_update))
# connection is closed 
mysql_interface.close_connection(cnx)
