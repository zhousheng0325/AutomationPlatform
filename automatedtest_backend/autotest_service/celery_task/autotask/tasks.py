from ..main import app
import time
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.append(BASE_DIR)

@app.task(name="test_script")
def test_script(*args,**kwargs):
    print(args)
    # time.sleep(5)
    print("=====Hello_Celery======")
    print(kwargs)
    return 1
