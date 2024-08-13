#!/usr/bin/env python3
"""
Module: MongoDB Document Update
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name.

    Args:
        mongo_collection: pymongo collection object.
        name (str): The name of the school to update.
        topics (list of str): The list of topics to set for the school.

    Returns:
        None
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
