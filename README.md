# python-oracle-cloud-db-connection

HOW TO CONNECT TO ORACLE CLOUD AUTONOMOUS DATABASE USING PYTHON

- download and unzip latest version of Oracle Instant client from suitable to your system from 
    https://www.oracle.com/pl/database/technologies/instant-client/downloads.html

- unzip files to appriopriate folder
- download Wallet to your database from Oracle Cloud site.
- from the Wallet unzip three following files to your instant client location  '<path_to_instant_client>\network\admin'
    * cwallet.sso
    * sqlnet.ora
    * tnsnames.ora
- ensure that in sqlnet.ora file following entries exist

    WALLET_LOCATION = (SOURCE = (METHOD = file) (METHOD_DATA = (DIRECTORY="<path_to_instant_client>\network\admin")))
    SSL_SERVER_DN_MATCH=yes

- create environment variables OCI_USER and OCI_PASS
