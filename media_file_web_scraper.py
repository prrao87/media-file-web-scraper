"""
Python version: 3.6
This script is specifically designed to download NHTSA media data from their web page
https://www-nrd.nhtsa.dot.gov/
* Modified as per web page syntax of 2017

To use the script, the user just needs to input the NHTSA "test number", which is a 4 or 5 digit number
The script generates the static web links and pulls the relevant media through Python 3's urllib.request

Created by: Prashanth Rao (PR)
Date: 06/21/2017
"""
import os
import time
import urllib.request

## BEGIN USER INPUTS ===============================================

# List of test numbers that we want
num_list = [9478]              
max_photos = 700        # Max number of photos to attempt to extract
max_reports = 20        # Max number of reports to attempt to extract
max_videos = 20         # Max number of videos to attempt to extract

## END OF USER INPUTS ========================================

def downloadMedia(test_num, media_url, max_range, identifier, out_extension, subdir):
    """
    Download the test's media content (photos, reports, videos) through Python 3's urllib.request
    """
    # Navigate to test directory and create media sub-directories
    os.chdir(test_num)
    if not os.path.isdir(subdir): os.mkdir(subdir)
    
    for i in range(1, max_range):
        temp_url = media_url+'tstno='+test_num+'&index='+str(i)+'&database=V&type='+identifier
        filename = "v%s%s%s.%s" % (str(test_num).rjust(5, "0"), identifier, str(i).rjust(3, "0"), out_extension)
        print("Downloading: "+filename)
        fullPath = os.path.join(os.getcwd(), subdir+"//"+filename)
        # Download file from specified link
        try:
            urllib.request.urlretrieve(temp_url, fullPath)
        except:     
            pass    # ignore failed downloads for now
        
    os.chdir("../") # Navigate back to rootpath
    
def downloadExtras(test_num, extra_url, identifier, out_extension):
    """
    Download the test's additional content (ASCII EV5, XML, ABF) through Python 3's urllib.request
    """
    # Navigate to test directory
    os.chdir(test_num)
    if len(test_num) < 5: 
        temp_url = extra_url+'tstno=0'+test_num+'&curno=&database=v&name=v0'+test_num+'&format='+identifier
    else:
        temp_url = extra_url+'tstno='+test_num+'&curno=&database=v&name=v'+test_num+'&format='+identifier
        
    filename = "v%s%s.%s" % (str(test_num).rjust(5, "0"), identifier, out_extension)
    print("Downloading: "+filename)
    fullPath = os.path.join(os.getcwd(), filename)
    # Download file from specified link
    try:
        urllib.request.urlretrieve(temp_url, fullPath)
    except: 
        pass    # ignore failed downloads for now
    
    os.chdir("../") # Navigate back to rootpath
    
def getFiles(filepath):
    """Recursively get a list of all files in the local directory - returns a list of filenames"""
    filenames = []
    for path, subdirs, files in os.walk(filepath):
        for name in files:
            filenames.append(os.path.join(path, name))
    
    return filenames
    
# Run script
if __name__ == "__main__":  

    a = time.time()
    #Define base path where our script is
    rootpath = os.getcwd()

    # Download each successive test number's data in a loop
    for num in num_list:
        os.chdir(rootpath)
        num = str(num)
        # "If specified directory is not found, then create it"
        if not os.path.isdir(num): os.mkdir(num)

        # Base URLs for media and extra files (this may change with time, so must keep this up to date)
        media_url = 'https://www-nrd.nhtsa.dot.gov/database/MEDIA/getmedia.aspx?'
        extra_url = 'https://www-nrd.nhtsa.dot.gov/database/VSR/Download.aspx?'
        
        print(f"\nBeginning download for test {num}\n")

        # Media
        downloadMedia(num, media_url, max_photos, "P", "jpg", "Photos")  # Download photos
        downloadMedia(num, media_url, max_reports, "R", "pdf", "Reports")  # Download reports
        downloadMedia(num, media_url, max_videos, "C", "avi", "Videos")  # Download videos

        print("\nCompleted media downloads!\n")

        # Additional content
        downloadExtras(num, extra_url, "abf", "abf")    # ABF files
        downloadExtras(num, extra_url, "ev5", "zip")    # ASCII X-Y (EV5) files
        downloadExtras(num, extra_url, "xml", "zip")    # XML files

        print("\nCompleted XML, ASCII (EV5) and ABF downloads!\n")
        
        # We overestimated the number of media files - these empty, unwanted files are now cleaned up
        filenames = getFiles(rootpath)
        for file in filenames:
            if os.path.getsize(file) < 1024:    # If file size < 1024 bytes, delete file
                os.unlink(file)
                
    print("Downloaded files for %i tests in %.8f sec" % (len(num_list), time.time() - a))
                
