from database.access.api import Api
from database.base import engine
from database import tables
from flask import abort

import setup


def create_dataset(access_token, dataset):
    setup.validate(access_token)
    api = Api(bind=engine)
    api.open()
    obj = tables.Dataset(**dataset)
    api.insert(obj)
    api.commit()
    res = obj.as_dict()
    api.close()
    return res


def remove_datasets(access_token, ids=[]):
    setup.validate(access_token)
    api = Api(bind=engine)
    api.open()
    objs = api.select(tables.Dataset, tables.Dataset.id.in_(ids)).all()
    for o in objs:
        api.delete(o)
    api.commit()
    api.close()


def get_dataset_list(access_token):
    setup.validate(access_token)
    api = Api(bind=engine)
    api.open()
    res = [r.as_dict() for r in api.select(tables.Dataset)]
    api.close()
    return res


def add_data_point(access_token, dataset_id, data_point_id):
    setup.validate(access_token)
    api = Api(bind=engine)
    api.open()
    dataset = api.select(
        tables.Dataset,
        tables.Dataset.id == dataset_id
    ).first()
    if dataset is None:
        abort(404, "dataset not found")
    data_point = api.select(
        tables.DataPoint,
        tables.DataPoint.id == data_point_id
    ).first()
    if data_point is None:
        abort(404, "data_point not found")
    dataset.data_points.append(data_point)
    api.commit()
    api.close()


def remove_data_point(access_token, dataset_id, data_point_id):
    setup.validate(access_token)
    api = Api(bind=engine)
    api.open()
    dataset = api.select(
        tables.Dataset,
        tables.Dataset.id == dataset_id
    ).first()
    if dataset is None:
        abort(404, "dataset not found")
    data_point = api.select(
        tables.DataPoint,
        tables.DataPoint.id == data_point_id
    ).first()
    if data_point is None:
        abort(404, "data_point not found")
    dataset.data_points.remove(data_point)
    api.commit()
    api.close()
