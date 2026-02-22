# Imports
import pickle
import importlib
from pathlib import Path

# Functions
def main():
    '''
    The main function of this code. 
    '''
    print('Test 1 started.') # 
    if check_docker() >= 4: print('Test passed :)') # 
    else: print('Your Docker image is not as it sholud be. \nTest not passed!') # 
    
def check_docker():
    '''
    Docstring für check_docker
    '''
    points = 0 # 

    if Path('/workspace').is_dir():
        points += 1
    
    if importlib.util.find_spec('numpy') is not None: 
        points += 1

        if importlib.metadata.version('numpy') == '2.4.0': 
            points += 1 # 

    if importlib.util.find_spec('cv2') is not None:
        points += 1 # 

    if importlib.util.find_spec('tqdm') is not None:
        points += 1 # 

        if importlib.metadata.version('tqdm') == '4.67.1':
            points += 1 #

    if importlib.util.find_spec('pandas') is not None:
        points += 1 # 

    with open('/workspace/test_1.pkl') as t1p_file:
        pickle.dump(points,t1p_file) # 

    return points # 

if __name__ == '__main__':
    main() # 