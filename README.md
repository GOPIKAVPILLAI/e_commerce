E-commerce Platform Scraper with Asynchronous Processing


Description

This project is a web scraper for a selected Japanese e-commerce platform, developed using Django, Scrapy, and Celery. It scrapes product data, including title, description, selling status, and condition. The project features asynchronous task processing with Celery, error handling, and logging.It also supports pagination to scrape multiple pages of product listings.

Technologies Used

Django: Web framework for Python

Scrapy: Web scraping framework

Celery: Task queue for managing asynchronous jobs

Features

Asynchronous Scraping: Products are scraped in the background using Celery, allowing the system to remain responsive.

Pagination: Scrapes data across multiple pages of product listings.

Error Handling: Logs errors during scraping for debugging purposes.

Frontend UI: Simple user interface to trigger scraping and display results.

Prerequisites

Make sure you have the following installed:

Python 3.x

Django 3.x

Scrapy 2.x

Celery 5.x
