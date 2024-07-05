from aiogram import Router

def register_handlers() -> Router:
    from . import start, confirm, messages
    router = Router()
    router.include_router(start.router)
    router.include_router(confirm.router)
    router.include_router(messages.router)
    return router
