# Example Python Server

This is a HTTP ReST Server providing remote access to example data. It is implemented as a python3 flask server using connexion to define the api interface (and swagger doc page) and sqlalchemy as a database ORM.

## Setup

Python dependencies can be installed on the host OS using pip:

```
pip install -r requirements.txt
```

(you may want to create a virtualenv to host your python environment and all dependencies)

Before running the server for the first time, the database needs to be created and a server secret has to be generated. It will be stored as ```secret.json``` at the root of this repo. This secret will serve as an access token to all client requests. Execute the setup script to automate these steps:

```
python3 setup.py
```

During this step a SERVER_DATA folder will also be created for any added features, which may need to store additional files on your server. You may also use the above command to whipe all data on your server. 

*NOTE*: Anytime the database structure changes, you will have to call this setup script again to apply these changes. If you don't, your server will not continue to work properly. Again, be careful, this step will delete all data in your database. Data migration is currently not supported, but may be added in the future. 

To change the target port, refer to the content of the ```main.py```.

## Run

After performing the setup, simply call:

```
python3 main.py
```

To end the hosting, simply kill the instanciated process e.g. by ```Ctrl+C``` from the command line.

## Debugging

The output of the run command will indicate that the server is available on compatible network cards of the host machine under default port 44100. For documentation of the currently running ReST API and a GUI for request testing, visit ```http://<ip>:<port>/api/ui```, e.g. ```http://localhost:44100/api/ui```.

The database created during setup (example.db) is a sqlite3 database, which you can read and write to with any compatible tool, such as the commandline:

```
sqlite3 example.db
```