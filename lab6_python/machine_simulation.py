import math
import random
from queue import Queue


class Request:
    """Класс для представления заявки."""
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time
        self.start_time = None
        self.end_time = None

class Machine:
    """Класс для моделирования работы станка."""
    def __init__(self):
        self.queue = Queue()
        self.current_request = None
        self.current_time = 0.0
        self.next_breakdown_time = 0.0
        self.next_request_arrival_time = 0.0
        self.completed_requests = []
        self.random = random.Random()
        self.random.seed()
        self.next_breakdown_time = self.generate_next_breakdown_time()
        self.next_request_arrival_time = self.generate_next_request_arrival_time()
        self.time_busy = 0.0
        self.time_idle = 0.0
        self.breakdown_count = 0
        self.last_event_time = 0.0
        self.processing_times = []

    def log(self, message):
        """Логирование текущего времени и события."""
        print(f"[{self.current_time:.2f} ч] {message}")

    def run(self, requests_number):
        """Основной метод для выполнения симуляции."""
        while len(self.completed_requests) < requests_number:
            # Обновляем время работы или простоя
            if self.current_request:
                self.time_busy += self.current_time - self.last_event_time
            else:
                self.time_idle += self.current_time - self.last_event_time
            self.last_event_time = self.current_time

            # Новая заявка
            if self.current_time >= self.next_request_arrival_time:
                new_request = Request(self.next_request_arrival_time)
                self.queue.put(new_request)
                self.log("Поступила новая заявка")
                self.next_request_arrival_time = self.generate_next_request_arrival_time()

            # Установка новой заявки в обработку
            if self.current_request is None and not self.queue.empty():
                element = self.queue.get()
                self.current_request = element
                setup_time = self.generate_setup_time()
                self.current_request.start_time = self.current_time + setup_time
                self.log(f"Станок начинает наладку для заявки (наладка: {setup_time:.2f} ч)")

            # Обработка текущей заявки
            if self.current_request and self.current_time >= self.current_request.start_time:
                processing_time = self.generate_processing_time()
                self.current_request.end_time = self.current_request.start_time + processing_time

                if self.current_time >= self.next_breakdown_time:
                    # Поломка станка
                    self.on_breakdown()
                elif self.current_time >= self.current_request.end_time:
                    # Завершение заявки
                    self.log(f"Станок завершил выполнение заявки (время обработки: {processing_time:.2f} ч)")
                    self.processing_times.append(processing_time)
                    self.completed_requests.append(self.current_request)
                    self.current_request = None

            self.current_time += 0.01  # Шаг симуляции

    def on_breakdown(self):
        """Обработка поломки станка."""
        self.breakdown_count += 1
        repair_time = self.random.uniform(0.1, 0.5)
        self.log(f"Станок сломался, ремонт займет {repair_time:.2f} ч")
        self.current_time += repair_time
        self.next_breakdown_time = self.generate_next_breakdown_time()

        if self.current_request:
            self.queue.put(self.current_request)
            self.log("Текущая заявка возвращена в очередь")
            self.current_request = None

    def generate_next_request_arrival_time(self):
        """Генерация времени следующего поступления заявки (экспоненциальное распределение)."""
        return self.current_time + self.generate_exponential(1.0)

    def generate_setup_time(self):
        """Генерация времени наладки станка (равномерное распределение)."""
        return self.random.uniform(0.2, 0.5)

    def generate_processing_time(self):
        """Генерация времени выполнения заявки (нормальное распределение)."""
        return max(0, self.generate_normal(0.5, 0.1))

    def generate_next_breakdown_time(self):
        """Генерация времени до следующей поломки (нормальное распределение)."""
        return self.current_time + max(0, self.generate_normal(20, 2))

    def generate_exponential(self, rate):
        """Генерация значения экспоненциального распределения."""
        return -math.log(1 - self.random.random()) / rate

    def generate_normal(self, mean, stddev):
        """Генерация значения нормального распределения (Box-Muller)."""
        u1 = self.random.random()
        u2 = self.random.random()
        rand_std_normal = math.sqrt(-2.0 * math.log(u1)) * math.sin(2.0 * math.pi * u2)
        return mean + stddev * rand_std_normal

    def analyze_results(self):
        """Анализ результатов работы станка."""
        total_time = self.current_time
        total_requests = len(self.completed_requests)
        avg_processing_time = sum(self.processing_times) / len(self.processing_times)
        busy_percentage = (self.time_busy / total_time) * 100

        print(f"Общее время симуляции: {total_time:.2f} часов")
        print(f"Количество завершённых заявок: {total_requests}")
        print(f"Среднее время выполнения заявки: {avg_processing_time:.5f} часов")
        print(f"Процент загрузки станка: {busy_percentage:.2f}%")
        print(f"Количество поломок: {self.breakdown_count}")
    


# Пример использования
if __name__ == "__main__":
    machine = Machine()
    machine.run(500)
    machine.analyze_results()
