"""sqlserver tap class."""

from typing import List

from singer_sdk import SQLTap, SQLStream
from singer_sdk import typing as th  # JSON schema typing helpers
from tap_sqlserver.client import sqlserverStream


class Tapsqlserver(SQLTap):
    """sqlserver tap class."""
    name = "tap-sqlserver"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "server_name",
            th.StringType,
            required=True,
            description="The name of the sql server"
        ),
        th.Property(
            "database_name",
            th.StringType,
            required=True,
            description="The name of the database"
        ),
        th.Property(
            "schema_name",
            th.StringType,
            required=True,
            description="The name of the database schema"
        ),
        th.Property(
            "table_names",
            th.ArrayType(th.StringType),
            required=True,
            description="The tables or views to replicate"
        ),
    ).to_dict()
