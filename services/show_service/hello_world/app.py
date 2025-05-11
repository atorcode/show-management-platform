import json


def lambda_handler(event: dict, context: dict) -> dict:
    http_method = event["httpMethod"]

    proxy = ""  # the path after /shows
    if (
        "pathParameters" in event
        and event["pathParameters"]
        and "proxy" in event["pathParameters"]
    ):
        proxy = event["pathParameters"]["proxy"]

    if http_method == "GET":
        if proxy and proxy != "":  # if there's something after /shows/
            return {"statusCode": 200, "body": json.dumps({"message": "GET BY ID"})}
        if not proxy:
            return {"statusCode": 200, "body": json.dumps({"message": "GET MANY"})}

    if http_method == "POST" and not proxy:
        return {"statusCode": 200, "body": json.dumps({"message": "POST SHOW"})}

    if http_method == "PUT" and proxy:
        return {"statusCode": 200, "body": json.dumps({"message": "PUT/UPDATE SHOW"})}

    if http_method == "DELETE" and proxy:
        return {"statusCode": 204}

    return {"statusCode": 404, "body": json.dumps({"message": "CATCH-ALL ERROR ROUTE"})}


# DIFF!!!!!
