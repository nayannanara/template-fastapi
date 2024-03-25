from fastapi import status


async def test_hould_return_ok(client):
    response = await client.get("/healthz")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "OK"}


async def test_should_return_ok(client):
    response = await client.get("/readiness")

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"status": "OK"}
