---
layout: post
title:  "Installing Decap CMS with Jekyll"
date:   2024-09-03 17:21:22 +0200
categories: jekyll decap-cms
---

## Install Jekyll

See [Jekyll install doc](https://docs.google.com/document/d/1LaqoY2Qii0Hcc6W6c8yt6eByBQiBJ1MB/edit?usp=sharing&ouid=104371554567107929993&rtpof=true&sd=true)

## Version your project

See [Git documentation](https://docs.google.com/document/d/1TfthdzUD5Cu6U8MjtL_WqqI4O09He0nr/edit?usp=sharing&ouid=104371554567107929993&rtpof=true&sd=true)

[Repo here](https://github.com/djacquel/jekyll-decap-cms)

## Install Decap CMS

ref : [Decap CMS documentation for Jekyll](https://decapcms.org/docs/jekyll/)

Create an admin folder at the root of your site.

Create an ___index.html___ file containing :

{% highlight html %}
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Content Manager</title>
    <!-- Include the identity widget -->
    <script src="https://identity.netlify.com/v1/netlify-identity-widget.js" type="text/javascript"></script>
  </head>
  <body>
    <!-- Include the script that builds the page and powers Decap CMS -->
    <script src="https://unpkg.com/decap-cms@^3.0.0/dist/decap-cms.js"></script>
  </body>
</html>
{% endhighlight %}

And a ___config.yml___ file containing :

{% highlight yaml %}
backend:
  name: git-gateway
  branch: main

media_folder: 'assets/uploads'

collections:
  - name: 'blog'
    label: 'Blog'
    folder: '_posts/'
    fields:
      - { name: Title }
{% endhighlight %}

## Deploy to Netlify

Follow the steps : __Add new site__ > __Import an existing project__

[Site config here](https://app.netlify.com/sites/jekyll-decap-cms/overview)

### Activate Netlify Identity 

From site overview > __Integrations__ > __Identity__

  1. __Activate Identity__
  2. From Identity > Services : __Activate Git Gateway__