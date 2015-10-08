#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import Base
from .entity import Entity
from sqlalchemy import Column, types


class Transfer(Base, Entity):

    __tablename__ = 'transfers'

    from_stop_id = Column(types.Integer, primary_key=True)
    to_stop_id = Column(types.Integer)
    transfer_type = Column(types.String(50))