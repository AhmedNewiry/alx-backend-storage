#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient



def log_stats():
    """
        provide stats about nginx
        logs stored in mongodb
    """
    # Connect to the MongoDB server
    client = MongoClient('mongodb://127.0.0.1:27017')
    
    # Select the database and collection
    db = client.logs
    nginx_collection = db.nginx

    # Count the total number of logs
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count logs for each method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")
    
    # Count logs with method GET and path /status
    status_check_count = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")
