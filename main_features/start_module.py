# This module allows to run files in operative directories 
import sys

def run():
    sys.path.append('../bussiness_fit/') # Main path
    sys.path.append('../bussiness_fit/main_features/') # function module    
    sys.path.append('../bussiness_fit/branx_sources/')

if __name__ == '__main__':
    run()