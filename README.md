# python-challenge  

This repository will contain the scripts for solving the challenges found at http://www.pythonchallenge.com.  

WARNING! This product contains Docker.  
How to run:  
1. Go to the root directory of the repository  
2. Build image: `docker build -t python-challenge .`  
3. Start a container: `docker run --rm --name python-challenge -v $(pwd)/scripts:/usr/src/app/scripts -it python-challenge /bin/bash`  
    `--rm`: automatically remove the container when it exits.  
    `--name`: gives a name to the container.  
    `--v`: makes the two given volumes share data between them, good for writing code without rebuilding the image and restarting the container. Useless if just running code.  
    `-it`: starts a bash session inside the container.  
    Note: for Powershell use `${pwd}`.  
4. In the container terminal go to the scripts directory and run the desired script with `python script-name.py`

OR use the containers extension in VSCode.  
