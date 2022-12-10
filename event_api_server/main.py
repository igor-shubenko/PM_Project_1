import uvicorn
from fastapi import FastAPI

from routers import events_routers
from handlers.events_handlers import startup_event_handler, shutdown_event_handler


app = FastAPI(title='EventApiServer',
              description="Server for CRUD operations for events",
              version="1.0")


@app.get('/test')
async def test():
    return "test passed"


app.add_event_handler('startup', startup_event_handler(app))
app.add_event_handler('shutdown', shutdown_event_handler(app))


app.include_router(events_routers.events_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8767, workers=1, reload=True)
