# demystify-youtube
This project is an effort at demystifying YouTube heterogeneous network. The dataset can aid various research problems.

USAGE:

~pip install scrapy

~cd demystify_youtube/

==run the following command==

~scrapy crawl youtube -a filename=seed_urls.txt -o scraped_data.csv -t csv

==to save in json format==

~scrapy crawl youtube -a filename=seed_urls.txt -o scraped_data.json

Above command reads start usrls from seed_urls.txt file, and saves the scraped data in scraped_data.csv.