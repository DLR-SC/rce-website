# Website for RCE

Homepage (landing page) and announcements for RCE (http://rcenvironment.de).

Based on [Pelican](http://blog.getpelican.com/) and a modifed Polar theme by [CodePassenger](http://www.codepassenger.com/).

## Local Installation

* Install Python3 ([Anaconda](https://store.continuum.io/cshop/anaconda/) works perfectly)

* Install Pelican and supporting libraries

  ```
  pip install invoke==1.4.1
  pip install pelican==3.7.1
  pip install markdown==3.1.1
  ```
  
* If you want to deploy the website after changing it, additionally install
  ```
  pip install ghp-import==0.5.5
  ```
  Deployment requires write access to the repository https://github.com/DLR-SC/rce-website.

* Clone this repository

### Configuration

 * Set proper port for local testing which works on your machine in `fabfile.py`
  ```
  # Port for `serve`
  PORT = 8001
  ```

## Build 

* Generate website 
  ```
  invoke build
  ```

* Start local server for testing (accessible via http://localhost:[PORT]/).
  ```
  invoke serve
  ```
  This does not rebuild the website after changes, meaning you will have to manually stop the local server, rebuild the website using `invoke build`, and restart the testing server after each change.

* If you want to automatically rebuild the website after each change and have that new build served by the testing server, use
  ```
  invoke reserve
  ```

## Deployment

In order to deploy the website, please first make sure that you have no local branch named `gh-pages`.
You can verify by executing `git branch` and checking the output for a line that contains `gh-pages`.
If such a line exists, you can delete the existing local branch.
*Please make sure that that branch contains no changes that you want to retain* before deleting it by executing `git branch -D gh-pages`.

Once you have made sure that no local branch named `gh-pages` exists, execute the following commands to publish your changes.
This requires write access to the repository at https://github.com/DLR-SC/rce-website.
If you do not have such access, please contact one of the main developers at DLR for obtaining them.

```
git fetch https://github.com/DLR-SC/rce-website.git gh-pages:gh-pages
ghp-import -b gh-pages output
git push https://github.com/DLR-SC/rce-website.git gh-pages
```

## Writing Content

Use either [Markdown](http://daringfireball.net/projects/markdown/) or HTML for new articles, as described in [Writing content](http://docs.getpelican.com/en/3.6.3/content.html).

Add new articles to `content`.

### Metadata

The required meta data for RCE release announcements are:
```
Title: Release 6.3.0 
Date: 2015-07-29 10:20
Category: Releases
Author: RCE
```



### Image sizes

 * Article image: 870x440 px (doesn't apply for the overview image of the article)
 * Thumbnail large: 100x108
 * Thumbnail small: 67x73


