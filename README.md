# Image-Downloader

# Why we need this?¶
Downloading images from google is not a big deal. We can download images from google image search, but it takes some time to download them because we do it manually. If we are looking for few images then its a good idea but what if we need to download images in bulk?

Other approach is that we can use specific software to download images, but finding out right software and its dependencies is very time consuming, so why dont we make a script which will fetch all images from google then it will start downloading the images in defined folder.

# Objective
Download images from internet of specific things.

# Usage
I am using this script to download image and create dataset for Machine Learning Models.

Now day's Deep Learning is mainly use in Data Science filed for images classification and object detection and some more.

To create your own dataset run this script with specifying the keyword of images which you want to download.

# Terminology
It uses the concept of web crawler in other words web spider or web robot.

# What is web crawler?
A Web crawler is a kind of bot which uses internet connection to crawl/scrape data from different websites.

They crawl one page at a time through a website until all pages have been indexed. Web crawlers help in collecting information about a website and the links related to them, and also help in validating the HTML code and hyperlinks.

Web crawlers collect information such the URL of the website, the meta tag information, the Web page content, the links in the webpage and the destinations leading from those links, the web page title and any other relevant information.

# How it works?
Its a web crawler, use accept the search keyword from user and send request to google image search. Once it get the response from google server it will parse the response page and start fetching image hyperlinks one by one and store it into urls.txt file.

Once fetching done it will start requesting the image url on server and downloading the images into images folder.
