# -*- coding: utf-8 -*-
"""
Vercel Serverless Function Entry Point
"""

import sys
import os

# 添加项目根目录到 Python 路径
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from app import app

# Vercel 需要这个变量
handler = app
