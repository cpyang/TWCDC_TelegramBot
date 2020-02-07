#!/usr/bin/env bash
cd fbcrawl
source ~/.secrets
/usr/bin/scrapy crawl fb -a email="$FACEBOOK_EMAIL" -a password="$FACEBOOK_PASSWORD" -a page="https://mbasic.facebook.com/TWCDC/" -a lang="en" -a date=`date --date='00:00 3 days ago' +'%Y-%m-%d'` -t "json" -o "../TWCDC.json"
