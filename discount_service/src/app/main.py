from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class DiscountRequest(BaseModel):
    product_id: str
    quantity: int
    price_per_item: float
    promo_code: Optional[str] = None

class DiscountResponse(BaseModel):
    discount_percent: float
    reason: str

@app.post("/discounts/calculate", response_model=DiscountResponse)
def calculate_discount(request: DiscountRequest) -> DiscountResponse:
    if request.promo_code == "STUDENT10":
        return DiscountResponse(
            discount_percent=10.0,
            reason="Студенческий промокод"
        )
    if request.quantity >= 10:
        return DiscountResponse(
            discount_percent=15.0,
            reason="Оптовая скидка"
        )
    return DiscountResponse(
        discount_percent=0.0,
        reason="Скидка не применима"
    )