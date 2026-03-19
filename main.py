import redis
import time

r = redis.Redis(host='localhost', port=6379, decode_responses=True)
r.set("name", "sumit")
print(r.get("name"))

# r.set("otp", "12345", ex=10)
# print(r.get("otp"))
# time.sleep(11)
# print(r.get("otp"))

# r.delete("name")
# print(r.get("name"))


code = input("enter a passcode: ")

def check_pass(code):

    counter = r.incr("login_attempts:user1")
    password = "1234"
    print(f"counter: {counter}")
    print(f"code: {code}")

    if counter > 3:
        r.expire("login_attempts:user1", 10)
        print("maximum limit reached")
        return

    if password != code:
        counter = r.incr("login_attempts:user1")
        print("invalid passcode")
        print(counter)
    else:
        print("valid passcode")

check_pass(code)

r.delete("user:1")
r.hset("user:1", mapping={
    "name": "sumit",
    "age": 20,
    "gender": "male"
})

user = r.hgetall("user:1")
print(user)
