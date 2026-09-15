from locust import HttpUser, task, between

class LLMUser(HttpUser):
    # Each simulated user will wait 1 - 3 seconds between making
    # consecutive requests to API
    
    # Without the wait this would function more akin to a Dos attack
    wait_time = between(1, 3)

    @task(3)
    def check_health(self):
        """Lightweight health check endpoint."""
        self.client.get("/health")

    @task(1)
    def generate_llm(self):
        """Heavy LLM generation endpoint."""
        payload = {"prompt": "Write 10 characters."}
        #Extends timeout since local LLM can be slower
        self.client.post("/generate", json=payload, timeout=60)