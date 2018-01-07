# media-file-web-scraper
Scrape media content off of static web-links using Python 3's urllib.request module.

This showcases a specific example where I was asked to help out some colleagues pull down crash-safety test data from the US NHTSA website: https://www-nrd.nhtsa.dot.gov/. The data was in the form of various media files (video, image, PDF, ASCII, etc.), and the data was stored on static URLs that had a specific pattern.

The script attached used Python 3.6 and it's ```urllib.request``` module. The script assumes that the test numbers for which we want to download the data is a 4 or 5 digit number (which is input by the user), and generates the web link for the storage location of the media using a hard-coded pattern that was current as of Dec 2017. We then use ```urllib.request.urlretrieve``` to pull down the content, and Python's amazing file-handling capabilities to organize the information. The information is dumped into a directory at the same location as the script, with the directory name the same as the test number. 

As and when the NHTSA webmaster chooses to update the static URLs, the pattern would need to be updated. However, this kind of pattern update is relatively trivial compared to the amount of effort a user would have to spend collecting the media files manually. 


