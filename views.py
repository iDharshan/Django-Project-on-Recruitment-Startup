from django.conf import settings
from django.shortcuts import render
from pymongo import MongoClient

def home(request):
    return render(request, 'index.html')  # Replace 'home.html' with your template name

def company_openings(request):
    # Connect to MongoDB
    client = MongoClient(
        host=settings.MONGO_DB['host'],
        port=settings.MONGO_DB['port'],
        username=settings.MONGO_DB['username'],
        password=settings.MONGO_DB['password'],
        authSource=settings.MONGO_DB['authSource'],
        authMechanism=settings.MONGO_DB['authMechanism']
    )
    
    # Access the database and collection
    db = client.your_database_name
    collection = db.job_listings  # Change to your collection name
    
    # Fetch job listings from MongoDB
    job_listings = list(collection.find())
    
    # Close the MongoDB connection
    client.close()
    
    context = {
        'jobs': job_listings,
    }
    
    return render(request, 'your_template_name.html', context)

