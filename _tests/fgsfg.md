---
layout: test
title: fgsfg
description: sfgsgsf
draft: true
code:
  code: >-
    class Animal
      include AnimalSkills # mixin

      @@name = 'an animal' # variable de classe

      def initialize(size, weight, color) # initialisation des variables d'instance
        @size = size.to_i
        @weight, @color = weight.to_i, color.to_s
      end

      def describe
        puts "I'm #{@@name} !"
        puts "I'm #{@size} meter tall, I weigh #{@weight} kilograms and I'm " + @color
      end
    end
  lang: ruby
color: "#d81818"
date: 2024/09/05
document: /assets/uploads/unary.py
thumbnail: /assets/uploads/mante-seb.jpg
authors:
  - authors
location: '{"type":"Point","coordinates":[18.984375,14.51978]}'
somemarkdown: dd
count: 2
airport-code: CDG
sections:
  - type: carousel
    header: Image Gallery
    template: carousel.html
    images:
      - image: /assets/uploads/boletus-edulis.jpg
        caption: Cèpe de Bordeaux
---
