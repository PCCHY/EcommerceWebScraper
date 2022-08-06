# NetAPorterScrape

Application to scrape Ecommerce Site.

## Description

This python-based application uses python scrapy framework to scrape product data from e-commerce site and then perform required Query On them.

## Getting Started

### Dependencies

Required Python Libraries for the Project
```bash
pip install pymongo[srv]
pip install scrapy
```

### Mongo DB Credentials
Credentails to access mongodb database 
```yaml
      Username: PCChy
      Password: pASswOrd
```

### Executing program

* First Install all the required Libraries
```bash
pip install -r requirements.txt
```

* Then Go to the Project Directory

* Then the following line to start Scraping
```bash
scrapy crawl product
```
* To run Queries enter following lines
```bash
py mongo_queries.py
```

* To Check Results Open File QueryResults.txt

### Folder Structure
#### Top Level Directory
    .
    ├── NetAPorterScrape
    ├── screenshots             # Folder to Store Project Screenshots
    ├── scrapy.cfg              # scrapy config files
    ├── requirements.txt        # Project Required Libraries
    └── README.md

#### NetAPorterFolder

    ├── ...
        ├── NetAPorterScrape
            ├── spiders                 # File for all the scrapers
            ├── items.py                # File for Product Data Format
            ├── pipelines.py            # File for Pipeline code
            ├── mongo_queries.py 		# File to Store Queries
            └── QueryResults.txt 		# Results of query
#### Spiders folder
	 ├── ...
		├── spiders                    # Scraper Code files
		│   └── product_spider.py      # Ecommerce Product Scraper code file
		└── ...
### Approach
#### To Scrape an Ecommerce Site 
* Setup Config Variables
* Setup the Mongodb connection using Scrapy Pipelines
* Go to the Site and Search for the div which have all the products listed
* Then from this div extract all the products
* Now for each product process their details and export it

![ProjectScreenShot1](/screenshots/Screenshot (770).png)
![ProjectScreenShot2](/screenshots/Screenshot (771).png)
![ProjectScreenShot3](/screenshots/Screenshot (772).png)

* Scrapy framework handles storing the data on server

![ProjectScreenShot11](/screenshots/Screenshot (780).png)

#### To Perform Queries
* Run the file mongo_queries.py
* Results are stored in QueryResults.txt

![ProjectScreenShot4](/screenshots/Screenshot (773).png)
![ProjectScreenShot5](/screenshots/Screenshot (774).png)
![ProjectScreenShot6](/screenshots/Screenshot (775).png)
![ProjectScreenShot7](/screenshots/Screenshot (776).png)
![ProjectScreenShot8](/screenshots/Screenshot (777).png)
![ProjectScreenShot9](/screenshots/Screenshot (778).png)
![ProjectScreenShot10](/screenshots/Screenshot (779).png)
![ProjectScreenShot12](/screenshots/Screenshot (781).png)


## Author

Prakash Chandra Choudhary


## Acknowledgments

Inspiration, code snippets, etc.
* [Scrapy](https://scrapy.org/)
* [MongoDB](https://www.mongodb.com/)
* [StackOverflow](https://stackoverflow.com/)
* [Net-A_Porter](https://www.net-a-porter.com/en-in/)