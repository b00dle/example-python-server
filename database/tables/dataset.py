from database.base import TableBase
from database.tables import associations
from sqlalchemy import Column, String, Integer

from sqlalchemy.orm import relationship


class Dataset(TableBase):
    __tablename__ = "dataset"

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(128), nullable=False)

    description = Column(String(1024), nullable=False)

    data_points = relationship("DataPoint", secondary=associations.dataset_datapoint, backref="datasets")

    def __repr__(self):
        return "<Dataset id=%s name=%s description=%s>" % (
            str(self.id), str(self.name), str(self.json))
