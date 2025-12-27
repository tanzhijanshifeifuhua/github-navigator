# -*- coding: utf-8 -*-
import sys
import traceback

try:
    import crawler
    print("导入成功")
except Exception as e:
    print(f"错误类型: {type(e).__name__}")
    print(f"错误信息: {str(e)}")
    traceback.print_exc()
