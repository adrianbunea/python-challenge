# python-challenge  

Solutions for http://www.pythonchallenge.com.  
 
To run use the Remote-Containers extension in VSCode OR:
1. Go to the root directory of the repository  
2. Build image: `docker build -t python-challenge .`  
3. Start a container: `docker run --rm --name python-challenge -v $(pwd)/scripts:/usr/src/app/scripts -it python-challenge /bin/bash`  
    `--rm`: automatically remove the container when it exits.  
    `--name`: names the container.  
    `--v`: links the two volumes, good for writing code without rebuilding the image and restarting the container.
    `-it`: starts a bash session inside the container.  
    Note: for Powershell use `${pwd}`.  
4. In the container's terminal go to the "scripts" directory and run a script 
