import cx_Oracle
from sqlalchemy import create_engine
import sys
import os
import pandas as pd

'''
- download and unzip latest version of Oracle Instant client from suitable to your system from 
    https://www.oracle.com/pl/database/technologies/instant-client/downloads.html

- unzip files to appriopriate folder
- download Wallet to your database from Oracle Cloud site.
- from the Wallet unzip three following files to your instant client location  <path to instant client>\network\admin
    * cwallet.sso
    * sqlnet.ora
    * tnsnames.ora
- ensure that in sqlnet.ora file following entries exist
    WALLET_LOCATION = (SOURCE = (METHOD = file) (METHOD_DATA = (DIRECTORY="<path to instant client>\network\admin")))
    SSL_SERVER_DN_MATCH=yes

- create environment variables OCI_USER and OCI_PASS

'''
if sys.platform.startswith("darwin") or sys.platform.startswith("linux"):
    cx_Oracle.init_oracle_client(
        lib_dir=os.environ.get("HOME")+"/instantclient_19_8",
        config_dir="")
elif sys.platform.startswith("win"):
    cx_Oracle.init_oracle_client(
        lib_dir=r"D:\\oracle\\instantclient_21_6")

username = os.getenv('OCI_USER')
# set the password in an environment variable called "OCI_PASS" for security
password = os.getenv('OCI_PASS')
dsn="extuat_high"

engine = create_engine(
    f'oracle://{username}:{password}@{dsn}/?encoding=UTF-8&nencoding=UTF-8', max_identifier_length=128)

with engine.connect() as conn:
     result=conn.execute("select * from employees")
     df = pd.DataFrame(result)
     print(df)
    