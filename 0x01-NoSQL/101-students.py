#!/usr/bin/env python3
"""
Module 101-students
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    
    Args:
    - mongo_collection: The pymongo collection
    object containing student documents.
    
    Returns:
    - A list of students, each containing an 'averageScore'
    key with the student's average score.
    """
    # MongoDB aggregation pipeline to calculate average scores and sort by it
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": { "$avg": "$topics.score" }
            }
        },
        { "$sort": { "averageScore": -1 } }
    ]
    
    # Execute the aggregation pipeline and return the results
    return list(mongo_collection.aggregate(pipeline))

