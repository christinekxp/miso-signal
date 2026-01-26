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
Step 4. Add request/response schemas

Tests
Step 1. Add tests using pytest
#TODO Step 2. Add integration tests (scraper -> DB -> API)
#TODO Step 3. Error handling and logging
#TODO Step 4. Use pytest-mock





Advanced product classification:

Use keyword-based rules or light ML to classify products by dog size/age/type.

For example, a tiny dog product classifier could be a simple scikit-learn or even spaCy text classifier.

Enrichment:

Add fields like estimated price range, shipping info, popularity scores.

Add image scraping and store URLs or thumbnails.

Scheduling & automation:

Use Celery or APScheduler to run the scraper periodically.

Rate limiting / polite scraping:

Add delays, respect robots.txt, and avoid IP blocks.
Wire /products

Add filtering

Add 1–2 solid tests

🔜 Scraping Optimization (return later)

Improve dog classification

Improve inference

Improve dedup logic
Database / Backend Enhancements

Better DB design:

Add indexes for frequent queries (like product category searches).

Consider using PostgreSQL JSON fields if product attributes vary.

ORM improvements:

Use SQLAlchemy effectively (relationships, constraints).

Caching:

Add Redis to cache frequent API queries.

Deduplication:

Use hashes of product URLs or normalized names to detect duplicates.
API / Frontend

Advanced API features:

Filtering, sorting, pagination.

Search endpoints (full-text search using PostgreSQL or ElasticSearch).

Authentication / Security:

JWT or OAuth2 if you want user accounts.

Swagger docs / OpenAPI:

FastAPI does this automatically—make it polished.

Frontend (optional):

A small React/Next.js interface showing scraped products.

Could be a nice showcase if you want to present this as a full-stack project.
DevOps Skills

This is where Docker, Kubernetes, and CI/CD come in.

Docker:

Containerize your API + scraper + DB for consistent environments.

Skills: Dockerfile, docker-compose, environment variables, volumes.

Kubernetes (optional for learning / deployment):

Deploy your Dockerized app with pods, services, and configs.

Skills: manifests (Deployment, Service), ConfigMaps, Secrets.

CI/CD:

GitHub Actions or GitLab pipelines to test code automatically when you push.

Build → Test → Docker build → Push → Deploy.

Cloud deployment:

AWS, GCP, or Azure:

Host API (FastAPI on EC2, AWS Fargate, or Heroku)

DB (RDS/Postgres)

Optional: S3 for images.