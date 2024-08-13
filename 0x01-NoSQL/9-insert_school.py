#!/usr/bin/env python3
"""
Module: MongoDB Document Insertion
"""


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document with the specified attributes into the provided MongoDB collection.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object.
    **kwargs: Attributes of the document to be inserted.

    Returns:
    str: The _id of the newly inserted document.
    """
    # Insert the document and get the result
    result = mongo_collection.insert_one(kwargs)
    
    # Return the _id of the new document
    return str(result.inserted_id)
