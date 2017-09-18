# Copyright 2017 Christopher Haverman
# All Rights Reserved
#
from ..models import Category, Subcategory

__author__ = 'Christopher Haverman'


class Props:
    """
    Provides the initial props for use by the React app.
    """
    def __init__(self, dbsession):
        """
        :param dbsession: SQLAlchemy dbsession
        """
        self._dbsession = dbsession

    def to_dict(self):
        """
        :return: representation of the initial props as a dict.
        """
        categories = self._dbsession.query(Category).all()
        return {
            'items': [
                {
                    'name': category.name,
                    'subcategories': [
                        {
                            'name': subcategory.name,
                            'items': [(object_.kind, object_.slug) for object_ in subcategory.objects]
                        }
                        for subcategory in category.subcategories
                    ]
                }
                for category in categories
            ]
        }
