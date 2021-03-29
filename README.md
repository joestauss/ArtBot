# ArtBot

## About

This repository contains my toolkit for managing a Twitter artbot.  I'm interested in automation, and running an artbot seems like a high-visibility project that might end up in something unique I can add to the Twitter community.  I am currently using this code to manage a single account, \@TaglinesOTerror, which has been occasionally operational since January 2021. 

## Development Status

ArtBot can post, but development is on hold while I work on the data-ingestion system.  I am updating the data model, which is a process that needs to start in the related data-ingestion project.  The Twitter account will keep posting for a while, but the toy dataset I used in early development is almost exhausted.

## Repository Contents

 This repository is organized into the following folders.

* __ArtBot__ is the main repository.  Not uploaded: login info, the data used to create posts.
* __depricated__ contains the first version of ArtBot.  ArtBot began as a Selenium-based browser automation script ( it uses Tweepy now). 
* __docs__ contains a few Markdown documents and Jupyter notebooks that might be helpful.
* __tests__ contains testing resources.  Tests will fail if run in this folder; they need to be copied to _ArtBot_ to run successfully.
