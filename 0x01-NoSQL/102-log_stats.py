#!/usr/bin/env python3
"""MongoDB"""

from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient()
    collec_nginx = client.logs.nginx

    num_docs = collec_nginx.count_documents({})
    print(f"{num_docs} logs")
    print("Methods:")
    method_list = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in method_list:
        method_count = collec_nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")
    status = collec_nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status} status check")

    print("IPs:")

    top_IPs = collec_nginx.aggregate(
        [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10},
            {"$project": {"_id": 0, "ip": "$_id", "count": 1}},
        ]
    )
    for top_ip in top_IPs:
        count = top_ip.get("count")
        ip_address = top_ip.get("ip")
        print(f"\t{ip_address}: {count}")
