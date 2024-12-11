from tools import Request_Assistance_Tool, Confirm_Assistance_Tool, Decline_Assistance_Tool, Follow_Up_Assistance_Tool
from prompt import PROMO_CALL_PROMPT

system_prompt = PROMO_CALL_PROMPT.format(
    language="Thai"
)


for tool in [
    Request_Assistance_Tool, Confirm_Assistance_Tool, Decline_Assistance_Tool, Follow_Up_Assistance_Tool
]:
