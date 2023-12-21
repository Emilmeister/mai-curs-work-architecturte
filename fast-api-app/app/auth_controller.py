import json

from fastapi import FastAPI, Response, status
from models import User
from repo.user_repo import filter_users, get_user_by_login, create_user, update_user
import jwt
import random
import string
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from redis import asyncio as aioredis
import redis

app = FastAPI()
jwt_encode_secret = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))

redis_db = redis.Redis(host='redis_host', port=6379, decode_responses=True, username="default", password='pass', encoding='utf8')
@app.on_event("startup")
async def start():
    redis_2 = aioredis.from_url("redis://default:pass@redis_host:6379/0", encoding="utf8", decode_responses=True)
    FastAPICache.init(RedisBackend(redis_2), prefix="fastapi-cache")

@app.post("/user/create")
async def create(user: User):
    id = create_user(user)
    user.id = id
    redis_db.set("/user/{login}:"+user.login, str(json.dumps(user.model_dump(), indent=4, sort_keys=True, default=str)), 600)
    return id


def key_builder(*args, **kwargs):
    namespace = args[1]
    login = kwargs['kwargs']['login']
    print(namespace+":"+login)
    return namespace+":"+login


@app.get("/user/{login}")
@cache(expire=600, key_builder=key_builder, namespace="/user/{login}")
async def get(login):
    #time.sleep(2)
    result = get_user_by_login(login, 0)
    if result is not None:
        return result
    else:
        result = get_user_by_login(login, 1)
        return result


@app.post("/user/update")
async def update(user: User):
    id = update_user(user)
    user.id = id
    redis_db.set("/user/{login}:" + user.login, str(json.dumps(user.model_dump(), indent=4, sort_keys=True, default=str)), 600)
    return id


@app.get("/user/filter/{surname_mask}/{name_mask}")
async def filtering(surname_mask, name_mask):
    result = filter_users(surname_mask, name_mask, 0)
    result.extend(filter_users(surname_mask, name_mask, 1))
    return result


users = [User()]


@app.post("/auth/login")
async def login(user: User, response: Response):
    print(user)
    user_list = list(filter(lambda u: u.login == user.login and u.password == user.password, users))
    if len(user_list) == 1:
        db_user = user_list[0]
        return jwt.encode({
            'id': db_user.id,
            'login': db_user.login,
            'password': db_user.password,
            'first_name': db_user.first_name,
            'last_name': db_user.last_name,
            'email': db_user.email,
            'insert_date': db_user.insert_date.isoformat(),
        }, jwt_encode_secret, algorithm="HS256")
    else:
        response.status_code = status.HTTP_401_UNAUTHORIZED


@app.post("/auth/check")
async def login_in(jwt_string: str):
    try:
        jwt_decoded = jwt.decode(jwt_string, jwt_encode_secret, algorithms=["HS256"])
        return {'user': jwt_decoded, 'success': True}
    except Exception:
        return {'user': None, 'success': False}
