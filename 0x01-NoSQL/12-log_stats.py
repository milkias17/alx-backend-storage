#!/usr/bin/env python3
"""MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    nginx = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{} logs".format(nginx.count_documents()))
    print("Methods:")

    for method in methods:
        print(
            "\tmethod {}: {}".format(method,
                                     nginx.count_documents({"method": method}))
        )

    print(
        "{} status check".format(
            nginx.count_documents({"method": "GET", "path": "/status"})
        )
    )
