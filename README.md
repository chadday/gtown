# gtown
Teaching materials for Georgetown data journalism

A place to put some of the tutorials we'll be using for basic python and webscraping in class.


## Basic web scraping with Python

Today, we'll be adding to our data journalism toolkit by getting a quick introduction to Python, working with a csv file and then writing a small webscraper to pull down a list of FBI recently released FOIA requests.

## Why are we doing this

As we've learned in class, most data doesn't come in a nice clean format. Many times we have to compile it ourselves. With web scraping, we can do that and more as you'll see. In this case, we're scraping this [website in the FBI's FOIA Reading Room](https://vault.fbi.gov/recently-added).

The way to think of this is as a before-and-after exercise. Before, the data exists as an HTML web page out on the Internet. After, we'll have a nice clean csv of the names of the documents, the links to their location and the date of their posting. In between, we'll be learning a lot about Python programming that you can use in everyday reporting.

## Getting started

First, let's talk about text editors. For the purposes of this class, we're going to be using the MacLab computers and the Sublime text editor installed on them. But if you're working on your own computer, here are some suggestions:

#### For Mac

I suggest installing [Brackets](http://brackets.io/). It's free and easy to use. It has everything we need for this tutorial and more.

I also recommend [Sublime](https://www.sublimetext.com/3). You an use it for free for as long as you want, but it's encouraged to purchase a license to support the software's development. Licenses are $80 and entitle you to use it on as many devices as you like.

#### For Windows

Jack and I are both fans of [Notepad++](https://notepad-plus-plus.org/). It has a bunch of plugins and a lot of functionality across multiple languages. It's also free.

## Installation

First things first, we're going to do some setup on our computers before we can start programming in Python. We will be coding in Python 3 (preferably 3.6 or higher).

#### Check your python install

On a Mac, open a Terminal window and type `python`. (You can find the Terminal by using the spotlight and searching for "Terminal.") If you see something like this:

`Python 3.6.8 (v3.6.8:3c6b436a57, Dec 24 2018, 02:04:31)
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
`

You're in business.

On a Windows machine, if you installed the Microsoft store version, open a command prompt and type `python3.8` or you can find it in the Start menu.


#### If not installed, install Python

    [Mac installer instructions](https://www.python.org/downloads/)


  If Windows, I would suggest using the [Microsoft store version](https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l?activetab=pivot:overviewtab) if you're looking to learn. You can also do the full install using the [Windows installer instructions](https://www.python.org/downloads/windows/). Note: Make sure to check the box during the install process to add Python to your path.


#### Install pip

Short for "Pip Installs Packages," pip is just what it sounds like. It's a package manager that installs python packages. We're going to use it for installing a series of Python packages that our scraper will rely on.

On Windows, if you installed from the Microsoft store, it should be included.

On Mac, to install pip, open the Terminal. Then copy and paste the code contained below into your terminal window. We'll be installing just to our user profile, instead of the machine itself, so we won't run into problems with not being the administrator on the computers.
```
curl https://bootstrap.pypa.io/get-pip.py -o ~/Downloads/get-pip.py
```
Once the file has downloaded, enter this:
```
python ~/Downloads/get-pip.py --user
```

After install, type `pip` into your terminal and press Enter. A help menu should pop up. If not, make sure it's added to your path, try ```echo $PATH ``` and you should see it added to your PATH.


#### Install Jupyter notebook

Now that we have `pip` installed, we can use it to install another tool we're going to use: Juypter notebooks. [Jupyter notebooks](https://jupyter.org/install) are incredibly powerful, open source environment for Python scripting. We'll be using them to do some tutorials and data work but I use them every day in my job for all kinds of data work.

To install, type:

```
pip install notebook
```

To make sure you have it installed, type:

`jupyter notebook`

A notebook session should pop up in your browser of choice.

#### Install requests

Next, we'll be using pip to install the Python packages we'll need. The first one is requests. You can read more about [requests](http://docs.python-requests.org/en/master/), but the short version is that requests is a package, or library, that allows us to make HTTP requests (i.e. follow urls and return their content) in Python. Now that we've install pip, the installation is easy. 
```
pip install requests --user
```

#### Install BeautifulSoup
Now that we've installed requests, we'll install BeautifulSoup. This library is an html parser, which is a type of package that will allow us to interact with html and pull the data we want out of it, a concept known as parsing.
```
pip install beautifulsoup4 --user
```

#### Install lxml and pyOpenSSL
We'll also install two other packages that are necessary for all of these packages to work together. [lxml](https://lxml.de/) processes xml and html in Python and is used by BeautifulSoup to parse. pyOpenSSL is used by requests and you can read more about it [here](https://pyopenssl.org/en/stable/introduction.html).
```
pip install -U pyopenssl --user

pip install lxml --user
```

Now we're ready to get started.