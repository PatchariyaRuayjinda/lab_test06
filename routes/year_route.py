from fastapi import APIRouter
from datetime import date

year_api_router = APIRouter()

@year_api_router.get("/service/getage")
async def cal_age(year: int = 0):
    current_year = date.today().year + 543
    if year == 0:
        return {"error": "input not equal zero"}
    elif year <= 0:
        return {"error": "input less zero"}
    elif year > current_year:
        return {"error": "input more than current year"}
    else:
        output = current_year - year
        print("current year",current_year)
        return {"age": output}