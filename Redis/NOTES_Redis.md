If Redis is set up to run as a service, you can check its status using:
```bash
systemctl status redis
```

Check Redis version
```bash
redis-server --version
```

Test the connection to Redis using redis-cli
```bash
redis-cli ping
```

View more Redis details: You can get more details about the Redis instance with the info command in redis-cli
```bash
redis-cli info
```
