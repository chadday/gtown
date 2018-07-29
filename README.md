# gtown
Teaching materials for Georgetown data journalism

A place to put some of the tutorials we'll be using for basic python and webscraping in class. 


## Basic web scraping with Python

Today, we'll be adding to our data journalism toolkit by getting a quick introduction to Python, working with a csv file and then writing a small webscraper to pull down a list of FBI recently released FOIA requests. 

## Why are we doing this

As we've learned in class, most data doesn't come in a nice clean format. Many times we have to compile it ourselves. With web scraping, we can do that and more as you'll see. We'll be writing a short Python script that will scrape the [website in the FBI's FOIA Reading Room](https://vault.fbi.gov/recently-added) where the bureau posts the most recently released documents. 

The way to think of this is as a before and after exercise. Before, the data exists as an HTML web page out on the Internet. After, we'll have a nice clean csv of the names of the documents, the links to their location and the data of their posting. In between, we'll be learning a lot about how Python programming that you can use in everyday reporting.

## Getting started 

First, let's talk about text editors. For the purposes of this class, we're going to be using the MacLab computers and the Sublime text editor installed on them. But if you're working on your own computer, here are some suggestions:

#### For Mac

I suggest installing [Brackets](http://brackets.io/) lately because its free and easy to use. It has everything we need for this tutorial and more.

I also recommend [Sublime](https://www.sublimetext.com/3). You an use it for free for as long as you want, but it's encouraged to purchase a license to support the software's development. Licenses are $80 and entitle you to use it on as many devices as you like. 

#### For Windows 

Jack and I are both fans of [Notepad++](https://notepad-plus-plus.org/). It has a bunch of plugins and a lot of functionality across multiple languages. It's also free.

## Installation 

First things first, we're going to do some setup on our computers before we can start programming in Python. Each of the MacLab machines has Python 2.7 installed on them, so we'll be using that. Much of what we're going over will translate to Python 3.5 or higher, except for the print statement, which we'll talk about. 

#### Install pip

Short for "Pip Installs Packages," pip is just what it sounds like. It's a package manager that installs python packages. We're going to use it for installing a series of python packages that our scraper will rely on. 

To install pip, open the Terminal on the MacLab machines. You can find it by using the spotlight and searching for "Terminal." 

Then copy and paste this code into your terminal window, which will download the pip install source code to your machine and then install it. We'll be installing it just to our user profile, instead of the machine itself, so we won't run into problems with not being the administrator on the computers. 
```
curl https://bootstrap.pypa.io/get-pip.py -o ~/Downloads/get-pip.py
```
Once the file has downloaded, enter this: 
```
python ~/Downloads/get-pip.py --user
```
Now we add this to our PATH, allowing us to invoke pip from the command line/terminal.
```
PATH=$PATH:~/Library/Python/2.7/bin
```
To make sure, it's added try ```echo $PATH ``` and you should see it added to your PATH.

#### Install requests

Next, we'll be using pip to install the python packages we'll need. The first one is requests. You can read more about [requests](http://docs.python-requests.org/en/master/), but the short version is that requests is a package, or library, that allows us to make HTTP requests (i.e. follow urls and return their content) in python. Now that we've install pip, the installation is easy. 
```
pip install requests --user
```

#### Install BeautifulSoup
Now that we've installed requests, we'll install BeautifulSoup. This library is an html parser, which is a type of package that will allow us to interact with html and pull the data we want out of it, a concept known as parsing. 
```
pip install beautifulsoup4 --user 
```

#### Dependencies 
We'll also install some dependencies that are necessary for all of these packages to work together.
```
pip install -U pyopenssl --user

pip install lxml --user
```

Now we're ready to get started. 

