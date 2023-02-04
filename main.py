import fastapi
import pykakasi
import uvicorn
from starlette import responses, templating

import models

app = fastapi.FastAPI()

templates = templating.Jinja2Templates(directory="templates")


@app.get("/furiganize/")
async def furiganize(q: str = ""):
    return models.KakasiResult(
        text=q,
        result=pykakasi.kakasi().convert(q),
    )


@app.get("/furiganize_html/", response_class=responses.HTMLResponse)
def furiganize_html(request: fastapi.Request, q: str = ""):
    result = models.KakasiResult(
        text=q,
        result=pykakasi.kakasi().convert(q),
    )
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,
            "content": result.get_html(),
        },
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
