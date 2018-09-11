# media-file-web-scraper
Example of a scraper that extracts media content off of static web-links using Python 3's urllib.request module.

This showcases a specific example I wrote to pull down crash-safety test data from the US NHTSA website: https://www-nrd.nhtsa.dot.gov/. The data was in the form of various media files (video, image, PDF, ASCII, etc.), and the data was pulled on static URLs.

- Test numbers for which we want to download data are hardcoded and input as a list.
- Base URL might change over time, so this might need to be updated as and when it does.

