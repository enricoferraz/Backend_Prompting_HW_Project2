from pydantic import BaseModel

class NegativeTreatment(BaseModel):
    treated_case: str
    treatment_nature: str
    treatment_text: str
    explanation: str