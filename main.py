import fastapi
import pykakasi
import uvicorn
from starlette import responses, templating

import models

app = fastapi.FastAPI()

templates = templating.Jinja2Templates(directory="templates")


@app.get("/furiganise/")
async def furiganise(q: str = ""):
    return models.Furiganised(
        text=q,
        result=pykakasi.kakasi().convert(q),
    )


@app.get("/furiganise_html/", response_class=responses.HTMLResponse)
def furiganise_html(request: fastapi.Request, q: str = ""):
    furiganised = models.Furiganised(
        text=q,
        result=pykakasi.kakasi().convert(q),
    )
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,
            "content": furiganised.get_html(),
        },
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
