from locust import task, SequentialTaskSet


class MyAccountNavigate(SequentialTaskSet):

    @task
    def fetch_personal_information(self):
        pass

    @task
    def exit_task_execution(self):
        self.interrupt()