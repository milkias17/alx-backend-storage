#!/usr/bin/env python3
"""MongoDB"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document based on kwargs"""
    return mongo_collection.insert_one(kwargs).inserted_id
