# Tasks
This is an extra branch providing files, programs and tasks that can be used as competency test to test your basic devops skills.

## First Stage: Git  
The .gitignore file is still empty.  
Enter the appropriate content so that Python cache, .pkl files, and .npy files will bne ignored.  

## Second Stage: Contaianer  
1. There is a Docker file in the Docker folder.  
It uses a req.txt file, which does not yet exist.  
Create it and enter the following to be installed:  
    - numpy version 2.4.0
    - opencv
    - tqdm  version 4.67.1
    - pandas

2. Build the Docker image.  
If it is not already installed, first install Docker and make it operational (you may need to change the BIOS settings of your device).

3. Use enroot to convert the Docker image into an sqsh container.  
If it is not already installed, first install enroot on your device.

## Thrid Stage: Python  
1. Start a interactive docker container of the docker image.  
Thereby mount the Python folder in the /workspace directory of the container.

2. Run the file test_1.py in the Docker container. 

3. Have a look at test_2.py.  
The code works without errors, but it contains some weaknesses.  
Comment on what happens in each line.  
Create a docstring for the main function by describing the weak points and explain how they could be improved.  

4. Have a look at test_3.py.  
Here are comments describing what the code is supposed to do.  
However, there are some errors that make the code non-executable and also cause it not to do what it is actually supposed to do.  
Find and correct these errors.  

5. Create a file named test_4.py in the Python folder that generates 10000 times a random two-dimensional Numpy array of size 3*3 with 1 or 0 as possible values for each index and counts how often each combination occurs.  
For this purpose, also create a progress bar with tqdm, which also shows how often the most frequent combination has already occurred.  
    a) Write a maximum of 10 lines code for this (empy lines or only commend lines as well as docstrings also count).  
    b) Write a minimum of 20 lines code for this (empy lines or only commend lines as well as docstrings do not count).  

## Fourth Stage: Submisson
Prepare a zip file for submission containing the following: 
- The docker folder
- The Python folder
- The .gitignore file
- The .sqsh container
- The Readme.md of the main branch
- Nothing else

