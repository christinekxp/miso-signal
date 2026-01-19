#Technologies Used
Python
SQLite

API/Backend
FastAPI
Docker
docker-compose

Maybe add Elasticsearch?


Use Fly.io or Render for container hosting


#Steps
Data
Step 1. Define the data in models.py
Step 2. Define how the data is stored in db.py
Step 3. Ensure this is all defined correctly in config.py
Step 4. Test this using init_db.py 


Ingestion/Scraping
Step 1. Set up scraper to bring in data 
Step 2. Start with a fake example scraper (just an example scraped data)
Step 3. Test connection to db using init_db.py

Scraping Optimization
Step 1. Update scraper to be better at classifying (dog products)
Step 2. Add size/weight inference to the scraper
Step 3. Add deduplication (update existing entries vs. adding them again)

API
Step 1. Set up FastAPI in main.py
Step 2. Define API in api/products.py
Step 3. Test in browser

