"""Order service Lambda handler (legacy Python 3.8 style)."""
import json
import logging
from collections import Mapping  # removed in Python 3.10+
from typing import Dict, List, Optional

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

TAX_RATE = 0.08
_dynamodb = boto3.resource("dynamodb")
_table = _dynamodb.Table("Orders")


def _calc_total(items):
    # type: (List[Dict]) -> float
    subtotal = 0.0
    for item in items:
        subtotal += item["unitPrice"] * item["quantity"]
    return subtotal + (subtotal * TAX_RATE)


def is_valid_order(order):
    # type: (Mapping) -> bool
    return "orderId" in order and "items" in order


def handler(event, context):
    # type: (Dict, object) -> Dict
    order = json.loads(event.get("body", "{}"))
    if not is_valid_order(order):
        logger.warning("Invalid order payload: %s" % json.dumps(order))
        return {"statusCode": 400, "body": "invalid order"}

    total = _calc_total(order["items"])
    logger.info("Order %s total is %.2f" % (order["orderId"], total))

    result = {"orderId": order["orderId"], "total": total}  # type: Dict
    return {"statusCode": 200, "body": json.dumps(result)}
