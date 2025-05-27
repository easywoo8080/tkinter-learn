import importlib.util
import sys
from pathlib import Path

# 슬래시 문제 해결: 백슬래시 대신 슬래시 또는 raw 문자열 사용
file_path = Path("Sec1_Tkinter_Fundamentals/1_Tkinter_Hello_World.py")
module_name = "tkinter_hello"

spec = importlib.util.spec_from_file_location(module_name, str(file_path))

if spec is not None and spec.loader is not None:
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
else:
    raise ImportError(f"모듈을 로드할 수 없습니다: {file_path}")
