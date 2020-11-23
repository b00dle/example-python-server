from database.base import TableBase
from sqlalchemy import Column, String, Integer, Float, Boolean


class DataPoint(TableBase):
    __tablename__ = "data_point"

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(128), nullable=False)

    some_int_property = Column(Integer, nullable=False)

    some_float_property = Column(Float, nullable=False)

    some_bool_property = Column(Boolean, nullable=False)

    # definition see tables.dataset
    datasets = []

    def __repr__(self):
        return "<DataPoint id=%s name=%s some_int_property=%s some_float_property=%s some_bool_property=%s>" % (
            str(self.id), str(self.name), str(self.some_int_property), str(self.some_float_property), str(self.some_bool_property))
