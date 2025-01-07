from fastapi import FastAPI, HTTPException, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.status import HTTP_303_SEE_OTHER
import requests
import os

# Initialize FastAPI application
app = FastAPI(title="Christmas Shopping Items API", version="v0")

# External API base URL (do not modify this)
SPRING_BOOT_API_URL = os.getenv("SPRING_BOOT_API_URL", "http://localhost:8080/api/shoppingItems")

# Template rendering setup
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


# Route: Display all items
@app.get("/")
def render_home(request: Request):
    try:
        response = requests.get(SPRING_BOOT_API_URL)
        items = response.json() if response.status_code == 200 else []
    except requests.exceptions.RequestException:
        items = []
    return templates.TemplateResponse("index.html", {"request": request, "items": items})


# Route: Add item form
@app.get("/add")
def display_add_form(request: Request):
    return templates.TemplateResponse("add_item.html", {"request": request})


# Route: Add item submission
@app.post("/add")
def submit_add_item(name: str = Form(...), amount: int = Form(...)):
    item_data = {"name": name, "amount": amount}
    response = requests.post(SPRING_BOOT_API_URL, json=item_data)
    if response.status_code in [200, 201]:
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    raise HTTPException(status_code=400, detail="Failed to add item.")


# Route: Update item form
@app.get("/update/{name}")
def display_update_form(request: Request, name: str):
    return templates.TemplateResponse("update_item.html", {"request": request, "name": name})


# Route: Update item submission
@app.post("/update/{name}")
def submit_update_item(name: str, amount: int = Form(...)):
    updated_item = {"name": name, "amount": amount}
    response = requests.put(f"{SPRING_BOOT_API_URL}/{name}", json=updated_item)
    if response.status_code == 200:
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    raise HTTPException(status_code=400, detail="Failed to update item.")


# Route: Delete item
@app.get("/delete/{name}")
def delete_item(name: str):
    response = requests.delete(f"{SPRING_BOOT_API_URL}/{name}")
    if response.status_code == 204:
        return RedirectResponse(url="/", status_code=HTTP_303_SEE_OTHER)
    raise HTTPException(status_code=400, detail="Failed to delete item.")
