# from aws_lambda_powertools import Logger, Metrics, Tracer
# from aws_lambda_powertools.event_handler import APIGatewayRestResolver
# from aws_lambda_powertools.logging import correlation_paths
# from aws_lambda_powertools.metrics import MetricUnit
# from aws_lambda_powertools.utilities.typing import LambdaContext

# app = APIGatewayRestResolver()
# tracer = Tracer()
# logger = Logger()
# metrics = Metrics(namespace="Powertools")


# @app.get("/hello")
# @tracer.capture_method
# def hello():
# adding custom metrics
# See: https://awslabs.github.io/aws-lambda-powertools-python/latest/core/metrics/
# metrics.add_metric(name="HelloWorldInvocations", unit=MetricUnit.Count, value=1)

# structured log
# See: https://awslabs.github.io/aws-lambda-powertools-python/latest/core/logger/
# logger.info("Hello world API - HTTP 200")
# return {"message": "hello world"}


# Enrich logging with contextual information from Lambda
# @logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
# Adding tracer
# See: https://awslabs.github.io/aws-lambda-powertools-python/latest/core/tracer/
# @tracer.capture_lambda_handler
# ensures metrics are flushed upon request completion/failure and capturing ColdStart metric
# @metrics.log_metrics(capture_cold_start_metric=True)
# def lambda_handler(event: dict, context: LambdaContext) -> dict:
#     return app.resolve(event, context)


# trigger diff HELLO HELLO HELLO
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


# diff
