#!/usr/bin/env python3
"""
Module: MongoDB Document Listing
"""


def list_all(mongo_collection):
    """
    List all documents in the specified MongoDB collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object.

    Returns:
    list: A list of documents in the collection. Returns an empty list if no documents are found.
    """
    # Find all documents in the collection
    documents = list(mongo_collection.find())
    
    # Return the list of documents
    return documents
