---
layout: test
title: My first test
description: My test description
draft: true
code:
  lang: yaml
  code: |-
    backend:
      name: git-gateway
      branch: main

    site_url: https://jekyll-decap-cms.netlify.app
color: "#c23838"
date: 09/05/2024
document: /assets/uploads/unary.py
thumbnail: /assets/uploads/mante-seb.jpg
authors:
  - authors
location: '{"type":"Point","coordinates":[5.1370994,48.1002763]}'
count: 21
airport-code: CDG
sections:
  - type: carousel
    header: Image Gallery
    template: carousel.html
    images:
      - /assets/uploads/mante-seb.jpg
      - /assets/uploads/boletus-edulis.jpg
  - type: spotlight
    header: Spotlight
    template: spotlight.html
    text: Hello World
---
Yolo **Markdown** !!
