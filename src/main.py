from aiohttp import web


def main():
    async def hello(request):
        return web.Response(text="Hello, world")

    app = web.Application()
    app.add_routes([web.get('/', hello)])

    web.run_app(app)


if __name__ == "__main__":
    main()
