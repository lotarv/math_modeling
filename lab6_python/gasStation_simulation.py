import math
import random
from queue import Queue


class Request:
    """Класс для представления заявки."""
    def __init__(self, arrival_time):
        self.arrival_time = arrival_time
        self.start_time = None
        self.end_time = None


class GasStation:
    """Класс для моделирования работы бензоколонки."""
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
        self.current_request1 = None
        self.current_request2 = None
        self.current_time = 0.0
        self.next_request_arrival_time = 0.0
        self.lost_requests = 0
        self.served_requests = []
        self.total_requests = []
        self.departure_intervals = []
        self.queue1_lengths = []
        self.queue2_lengths = []
        self.queue_timestamps = []
        self.random = random.Random()
        self.random.seed()
        self.next_request_arrival_time = self.generate_next_request_arrival_time()

    def log(self, message):
        """Логирование событий."""
        print(f"[{self.current_time:.2f}]: {message}")

    def run(self, num_requests):
        """Основной метод для выполнения симуляции."""
        while len(self.total_requests) < num_requests:
            # Поступление новой заявки
            if self.current_time >= self.next_request_arrival_time:
                new_request = Request(self.next_request_arrival_time)
                self.log("Клиент подъехал")
                if self.queue1.qsize() < 5 and (self.queue1.qsize() <= self.queue2.qsize()):
                    self.queue1.put(new_request)
                    self.log("Клиент добавлен в первую очередь")
                elif self.queue2.qsize() < 5:
                    self.queue2.put(new_request)
                    self.log("Клиент добавлен во вторую очередь")
                else:
                    self.log("Клиент уехал, так как очереди переполнены")
                    self.lost_requests += 1
                self.total_requests.append(new_request)
                self.next_request_arrival_time = self.generate_next_request_arrival_time()

            # Обработка первой очереди
            if self.current_request1 is None and not self.queue1.empty():
                self.current_request1 = self.queue1.get()
                self.current_request1.start_time = self.current_time
                self.current_request1.end_time = self.current_time + self.generate_service_time()
                self.log("Обработка клиента начата на первой колонке")

            # Обработка второй очереди
            if self.current_request2 is None and not self.queue2.empty():
                self.current_request2 = self.queue2.get()
                self.current_request2.start_time = self.current_time
                self.current_request2.end_time = self.current_time + self.generate_service_time()
                self.log("Обработка клиента начата на второй колонке")

            # Завершение обслуживания в первой очереди
            if self.current_request1 and self.current_time >= self.current_request1.end_time:
                self.served_requests.append(self.current_request1)
                if len(self.served_requests) > 1:
                    prev_end_time = self.served_requests[-2].end_time
                    self.departure_intervals.append(self.current_time - prev_end_time)
                self.current_request1 = None
                self.log("Клиент уехал из первой очереди")

            # Завершение обслуживания во второй очереди
            if self.current_request2 and self.current_time >= self.current_request2.end_time:
                self.served_requests.append(self.current_request2)
                if len(self.served_requests) > 1:
                    prev_end_time = self.served_requests[-2].end_time
                    self.departure_intervals.append(self.current_time - prev_end_time)
                self.current_request2 = None
                self.log("Клиент уехал из второй очереди")

            # Обновление времени и статистики по длинам очередей
            self.update_queue_lengths()
            self.current_time += 0.01

    def update_queue_lengths(self):
        """Обновление длины очередей."""
        self.queue1_lengths.append(self.queue1.qsize())
        self.queue2_lengths.append(self.queue2.qsize())
        self.queue_timestamps.append(self.current_time)

    def generate_next_request_arrival_time(self):
        """Генерация времени следующей заявки."""
        interval = self.generate_exponential(10)  # lambda = 10 (средний интервал 0.1 времени)
        self.log(f"Интервал между клиентами: {interval:.3f}")
        return self.current_time + interval

    def generate_service_time(self):
        """Генерация времени обслуживания."""
        service_time = self.generate_exponential(2)  # lambda = 2 (среднее время 0.5 времени)
        self.log(f"Время обслуживания клиента: {service_time:.3f}")
        return service_time

    def generate_exponential(self, rate):
        """Генерация значения экспоненциального распределения."""
        return -math.log(1 - self.random.random()) / rate

    def average_queue_length(self, queue_lengths):
        """Средняя длина очереди."""
        total_length = 0.0
        for i in range(1, len(self.queue_timestamps)):
            duration = self.queue_timestamps[i] - self.queue_timestamps[i - 1]
            total_length += queue_lengths[i - 1] * duration
        total_time = self.queue_timestamps[-1] - self.queue_timestamps[0]
        return total_length / total_time if total_time > 0 else 0

    def lost_request_percentage(self):
        """Процент потерянных заявок."""
        total_requests = len(self.served_requests) + self.lost_requests
        return (self.lost_requests / total_requests) * 100 if total_requests > 0 else 0

    def average_departure_interval(self):
        """Средний интервал между отъездами."""
        return sum(self.departure_intervals) / len(self.departure_intervals) if self.departure_intervals else 0

    def average_time_in_system(self):
        """Среднее время пребывания клиента на заправке."""
        total_time = sum(req.end_time - req.arrival_time for req in self.served_requests)
        return total_time / len(self.served_requests) if self.served_requests else 0

    def analyze_results(self):
        """Анализ результатов работы бензоколонки."""
        print(f"Средняя длина очереди 1: {self.average_queue_length(self.queue1_lengths):.2f}")
        print(f"Средняя длина очереди 2: {self.average_queue_length(self.queue2_lengths):.2f}")
        print(f"Процент потерянных клиентов: {self.lost_request_percentage():.2f}%")
        print(f"Средний интервал между отъездами: {self.average_departure_interval():.2f}")
        print(f"Среднее время пребывания клиента: {self.average_time_in_system():.2f}")


# Пример использования
if __name__ == "__main__":
    station = GasStation()
    station.run(400)
    station.analyze_results()
