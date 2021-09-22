from locust import HttpUser, task


class SimpleTest(HttpUser):
    @task
    def get_status(self):
        self.client.get("/status")
