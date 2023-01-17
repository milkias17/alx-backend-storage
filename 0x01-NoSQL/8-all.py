#!/usr/bin/env python3
"""MongoDB"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    if mongo_collection.count_documents({}) == 0:
        return []

    return mongo_collection.find()
