"""SQL client handling.

This includes sqlserverStream and sqlserverConnector.
"""

import sqlalchemy

from singer_sdk import SQLConnector, SQLStream


class sqlserverConnector(SQLConnector):
    """Connects to the sqlserver SQL source."""

    def get_sqlalchemy_url(cls, config: dict) -> str:
        """Concatenate a SQLAlchemy URL for use in connecting to the source."""
        return (
            f"mssql://{config["server_name"]}/{config["database_name"]}?"
            f"driver={config["driver_name"]}&"
            f"trusted_connection=yes&TrustServerCertificate=yes"
        )

    @staticmethod
    def to_jsonschema_type(sql_type: sqlalchemy.types.TypeEngine) -> dict:
        """Returns a JSON Schema equivalent for the given SQL type.

        Developers may optionally add custom logic before calling the default
        implementation inherited from the base class.
        """
        # Optionally, add custom logic before calling the super().
        # You may delete this method if overrides are not needed.
        return super().to_jsonschema_type(sql_type)

    @staticmethod
    def to_sql_type(jsonschema_type: dict) -> sqlalchemy.types.TypeEngine:
        """Returns a JSON Schema equivalent for the given SQL type.

        Developers may optionally add custom logic before calling the default
        implementation inherited from the base class.
        """
        # Optionally, add custom logic before calling the super().
        # You may delete this method if overrides are not needed.
        return super().to_sql_type(jsonschema_type)


class sqlserverStream(SQLStream):
    """Stream class for sqlserver streams."""

    connector_class = sqlserverConnector

    def get_records(self, partition: Optional[dict]) -> Iterable[Dict[str, Any]]:
        """Return a generator of row-type dictionary objects.

        Developers may optionally add custom logic before calling the default
        implementation inherited from the base class.

        Args:
            partition: If provided, will read specifically from this data slice.

        Yields:
            One dict per record.
        """
        # Optionally, add custom logic instead of calling the super().
        # This is helpful if the source database provides batch-optimized record
        # retrieval.
        # If no overrides or optimizations are needed, you may delete this method.
        yield from super().get_records(partition)
