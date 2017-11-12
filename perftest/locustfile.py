from bs4 import BeautifulSoup
from locust import HttpLocust, TaskSet, task


def s1(tag):
    if tag.name != 'input':
        return False

    if not tag.has_attr('name'):
        return False

    if not tag.has_attr('value'):
        return False

    return True


class UserBehavior(TaskSet):
    def on_start(self):
        self.login()

    def login(self):
        response = self.client.get('/auth/login')
        bs = BeautifulSoup(response.content,  "html.parser")
        a = bs.find_all(s1)
        self.client.post("/auth/login/", {
            "username": "user",
            "password": "user",
            "csrfmiddlewaretoken": a[0].attrs['value'],
        })

    @task(2)
    def contact_all(self):
        self.client.get("/contact/all/")

    @task(1)
    def tags_all(self):
        self.client.get("/tags/")


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 100
    max_wait = 3000


def track_success(**kwargs):
    print(kwargs)

# events.request_success += track_success
