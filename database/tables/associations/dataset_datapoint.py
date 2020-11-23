from database import constants
from database.base import TableBase

from sqlalchemy import Column, Table
from sqlalchemy import ForeignKey

dataset_datapoint = Table(
    "dataset_datapoint", TableBase.metadata,
    Column(
        "dataset_id",
        ForeignKey(
            "dataset.id", name="a",
            onupdate=constants.CASCADE, ondelete=constants.CASCADE
        ),
        primary_key=True
    ),
    Column(
        "data_point_id",
        ForeignKey(
            "data_point.id", name="b",
            onupdate=constants.CASCADE, ondelete=constants.CASCADE
        ),
        primary_key=True
    )
)
