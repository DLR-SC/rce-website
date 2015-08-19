# Website for RCE

Homepage (landing page) and announcements for RCE (http://rcenvironment.de).

Based on [Pelican](http://blog.getpelican.com/) and a modifed Polar theme by [CodePassenger](http://www.codepassenger.com/).

## Local Installation

* Install Python ([Anaconda](https://store.continuum.io/cshop/anaconda/) works perfectly)

* Install Pelican and supporting libraries

  ```
pip install pelican
pip install markdown
pip install fabric
pip install ghp-import
```

 * Clone rce-website

  ```
git clone https://github.com/onyame/rce-website.git
```

### Configuration

 * Set proper port for local testing, which works on your machine in `fabfile.py`

  ```
# Port for `serve`
PORT = 8001
```

## Build 

 * Generate website 
  ```
fab build
```

 * Start local server for testing
  ```
fab serve
```

 * Convenience target for rebuild and starting local server
  ```
fab reserve
```

## Deployment



## Writing Content

Use either Markdown or HTML for new articles...

### Metadata

### Image sizes
 * Article image: 870x440 px
 * Thumbnail large: 100x108
 * Thumbnail small: 67x73


