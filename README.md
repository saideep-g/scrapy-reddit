# scrapy-reddit
Experimenting to scrape using Scrapy. Connects to `https://www.reddit.com/r/india` and scraps the **title** and **url**. title and url is stored in the file _items.json_

#### Sample .json output
```
{"url": "/r/india/comments/46p905/jnu_discussion_part_iii/", "title": "JNU Discussion: Part III"}
{"url": "http://indianexpress.com/article/india/india-news-india/jat-reservation-agitation-haryana-live-updates-rohtak/", "title": "LIVE: Railway station set on fire in Jind, BJP leaders in huddle to solve Jat reservation crisis"}
{"url": "http://imgur.com/pL48yOW", "title": "[NP] How to earn 6 Crore in 6 months."}
{"url": "/r/india/comments/46vcat/why_is_it_okay_to_make_fun_of_someones_poor/", "title": "Why is it okay to make fun of someone's poor English writing/speaking skills ? [Serious ] [np]"}
```

#### Learnings
- XPATH  
- Using `$x` in Chrome console

#### Reference:

- [Web Scraping With Scrapy and MongoDB](https://realpython.com/blog/python/web-scraping-with-scrapy-and-mongodb/)
