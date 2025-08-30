from queue import Queue
import time

def process_request(queue_applications: Queue):
    if queue_applications.empty():
        print("Черга порожня: немає що обробляти")
    else:
        print("Маємо заявку. Обробляємо!")
        request = queue_applications.get()
        application_processing_imitation(request)

def application_processing_imitation(request: str):
    print(f"Починаємо обробку {request['id']}")
    time.sleep(2)
    print("Заявка оброблена")


