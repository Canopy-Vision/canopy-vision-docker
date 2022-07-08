#!/usr/bin/env python3
import sys
import json
from datetime import datetime
import uuid
import os
from time import sleep
from datetime import datetime
import threading
import time

uuid_str = str(uuid.uuid4())[:4]
print(f"{uuid_str}: starting script at {datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]}")

# Example object detection data
# {'timestamp': 1640611347.163409,
#   'data': [{'class_id': 1,
#             'label': 'hardhat',
#             'confidence': -0.10000000149011612,
#             'top': 100.80000305175781,
#             'left': 396.8000183105469,
#             'width': 189.1555633544922,
#             'height': 240.00001525878906}]}

while True:
    try:
        data = input()
        print(data)
    except EOFError:
        continue
    
print("Exiting...")
