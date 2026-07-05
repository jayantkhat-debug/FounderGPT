from pydantic import BaseModel


class AgentRead(BaseModel):
    key: str
    name: str
    specialty: str
    personality: str
