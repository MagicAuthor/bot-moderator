from aiogram import Router

def register_handlers() -> Router:
    from . import ban, login, triggers
    router = Router()
    router.include_router(ban.router)
    router.include_router(login.router)
    router.include_router(triggers.router)
    return router
