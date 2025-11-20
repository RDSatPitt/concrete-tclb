# RDSO

## Instructions

1. Clone the repository
```shell
git clone https://www.github.com/RDSatPitt/concrete-tclb
```

2. Enter the project directory
```shell
cd concrete-tclb
```

3. Create a virtual environment and activate it ([docs](https://docs.python.org/3.9/tutorial/venv.html))
```shell
# make it
$ python3 -m venv env

# activate it (mac)
$ . env/bin/activate

# activate it (windows)
$ env\Scripts\activate
```

4. Install required python packages
```shell
pip install r- requirements.txt
```

5. Download the necessary data from the Pitt sharepoint link (provided by Ross). The link will contain two folders ("images" and "data") and one standalone file (".env"). **Note**: Your system may try and rename ".env" to "env" (no leading ".") after downloading it from Sharepoint. Make sure that it is ".env" in your project directory, and if it is not, refactor the file so it is named ".env".


6. Add the three items to your `concrete-tclb` folder. Your folder structure should look like this: 
```
└── concrete-tclb/
    ├── data/
    │   ├── assessments.csv
    │   ├── liens.csv
    │   ├── parcels.geojson
    │   └── tricog_footprint.geojson
    └── .env
```


7. Use the marimo `run` command to launch the program.
```shell
marimo run tricog.py
```