#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: <Macarena Reale Portelli>

import os

secret_key = 'secret'
PWD = os.path.abspath(os.curdir)

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///{}/dbase.db'.format(PWD)
SQLALCHEMY_TRACK_MODIFICATIONS = False