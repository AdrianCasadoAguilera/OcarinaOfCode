import pandas as pd
import pymysql
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder

ssh_host = '4.231.232.138'
ssh_username = 'equipo7'
ssh_password = '@W7YS9i5vufnGSi'
database_username = 'root'
database_password = 'root'
database_name = 'proyecto_zelda'
localhost = '127.0.0.1'

def open_ssh_tunnel(verbose=False):
    """Open an SSH tunnel and connect using a username and password.
    :param verbose: Set to True to show logging
    :return tunnel: Global SSH tunnel connection
    """
    if verbose:
        sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
    global tunnel
    tunnel = SSHTunnelForwarder(
        (ssh_host, 22),
        ssh_username = ssh_username,
        ssh_password = ssh_password,
        remote_bind_address = ('127.0.0.1', 3306)
    )
    tunnel.start()

def mysql_connect():
    """Connect to a MySQL server using the SSH tunnel connection
    :return connection: Global MySQL database connection
    """
    global connection
    connection = pymysql.connect(
        host='127.0.0.1',
        user='root',
        passwd='root',
        db='zelda',
        port=tunnel.local_bind_port
    )

def mysql_disconnect():
    #Closes the MySQL database connection.
    connection.close()

def close_ssh_tunnel():
    #Closes the SSH tunnel connection.
    tunnel.close

def run_query(sql):
    """Runs a given SQL query via the global database connection.
    
    :param sql: MySQL query
    :return: Pandas dataframe containing results
    """
    
    return pd.read_sql_query(sql, connection)


print(run_query("SELECT * FROM enemies WHERE game_id = (SELECT max(game_id) FROM game)"))