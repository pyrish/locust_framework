from locust import task, SequentialTaskSet


class CategoryNavigate(SequentialTaskSet):
    
    def on_start(self):
        pass

    @task
    def navigate_to_women_category(self):
        pass

    @task
    def navigate_to_dresses_category(self):
        pass

    @task
    def navigate_to_shirt_category(self):
        pass


    @task
    def exit_task_execution(self):
        self.interrupt()