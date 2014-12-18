# -*- coding: utf8 -*-
# This file is part of PyBossa.
#
# Copyright (C) 2013 SF Isle of Man Limited
#
# PyBossa is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyBossa is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with PyBossa.  If not, see <http://www.gnu.org/licenses/>.

from pybossa.core import (db, user_repo, project_repo, task_repo, blog_repo,
    auditlog_repo)

import factory


def reset_all_pk_sequences():
    AppFactory.reset_sequence()
    BlogpostFactory.reset_sequence()
    CategoryFactory.reset_sequence()
    TaskFactory.reset_sequence()
    TaskRunFactory.reset_sequence()
    UserFactory.reset_sequence()


class BaseFactory(factory.Factory):
    @classmethod
    def _setup_next_sequence(cls):
        return 1

    @classmethod
    def _build(cls, model_class, *args, **kwargs):
        project = model_class(*args, **kwargs)
        db.session.remove()
        return project


# Import the factories
from app_factory import AppFactory
from blogpost_factory import BlogpostFactory
from category_factory import CategoryFactory
from task_factory import TaskFactory
from taskrun_factory import TaskRunFactory, AnonymousTaskRunFactory
from user_factory import UserFactory
from auditlog_factory import AuditlogFactory
