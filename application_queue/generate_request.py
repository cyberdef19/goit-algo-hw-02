import uuid
from queue import Queue
from datetime import datetime

def generate_request(queue_applications: Queue):
    request = {
        'id': uuid.uuid4(),
        'info': "Information",
        'datetime': datetime.now()
    }
    queue_applications.put(request)