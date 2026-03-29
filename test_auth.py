import httpx
import asyncio

async def test():
    async with httpx.AsyncClient() as client:
        # signup
        print("Signing up...")
        res = await client.post("http://localhost:8000/api/auth/signup", json={
            "name": "Test User",
            "email": "test2@example.com",
            "password": "password123"
        })
        print(res.status_code, res.text)
        
        # login
        print("Logging in...")
        res2 = await client.post("http://localhost:8000/api/auth/login", json={
            "email": "test2@example.com",
            "password": "password123"
        })
        print(res2.status_code, res2.text)

asyncio.run(test())
