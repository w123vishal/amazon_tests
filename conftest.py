# {
#   "single_test": {
# 	"browserName": "Chrome",
# 	"browserVersion": "135",
# 	"LT:Options": {
# 		"username": "w123vishal",
# 		"accessKey": "LT_XCggEtu0daIiw9BavEqrM1jSuihrt55707qTfnlRj6DHh0a",
# 		"platformName": "Linux",
# 		"build": "test1",
# 		"project": "interview assessment",
# 		"name": "test1",
# 		"w3c": True,
# 		"plugin": "python-pytest"
# 	}
#   }
# }
# conftest.py
import logging
import os

def pytest_configure(config):
    worker_id = os.getenv('PYTEST_XDIST_WORKER', 'gw0')  # Default gw0
    log_file = f"logs/{worker_id}.log"
    
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] [%(name)s] [%(process)d] %(message)s",
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
