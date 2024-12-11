# รับข้อมูลการแจ้งเหตุรถเสียจากลูกค้า รวมถึงข้อมูลลูกค้า รายละเอียดรถ และตำแหน่งที่รถเสีย
class Request_Assistance_Tool(BaseTool):
   
    name = "request_assistance_tool"
    description = "Tool for assisting customers reporting vehicle breakdowns."
    parameters = [
        {"name": "customer_name", "type": "string", "description": "Customer's full name."},
        {"name": "vehicle_details", "type": "string", "description": "Details of the customer's vehicle."},
        {"name": "breakdown_location", "type": "string", "description": "Exact location of the breakdown."},
    ]


    required = [
        "customer_name", "vehicle_details", "breakdown_location"
    ]


    def use(customer_name: str, vehicle_details: str, breakdown_location: str):
        return f"สวัสดีค่ะ คุณ{customer_name} ไม่ทราบว่ารถรุ่น {vehicle_details} จอดเสียอยู่ที่ {breakdown_location} ใช่ไหมคะ? เราจะจัดส่งทีมงานไปช่วยเหลือในทันทีค่ะ!"

# ใช้สำหรับยืนยันข้อมูลการช่วยเหลือกับลูกค้า เช่น ชื่อ เบอร์โทร รายละเอียดรถ และตำแหน่งที่รถเสีย
class Confirm_Assistance_Tool(BaseTool):
   
    name = "confirm_assistance_tool"
    description = "Tool for confirming assistance details with customers."
    parameters = [
        {"name": "customer_name", "type": "string", "description": "Customer's full name."},
        {"name": "vehicle_details", "type": "string", "description": "Details of the customer's vehicle."},
        {"name": "breakdown_location", "type": "string", "description": "Exact location of the breakdown."},
        {"name": "phone_number", "type": "string", "description": "Customer's phone number."},
    ]


    required = [
        "customer_name", "vehicle_details", "breakdown_location", "phone_number"
    ]


    def use(customer_name: str, vehicle_details: str, breakdown_location: str, phone_number: str):
        return f"ขอบคุณค่ะ คุณ{customer_name} สำหรับข้อมูล รถรุ่น {vehicle_details} จอดเสียอยู่ที่ {breakdown_location} และเบอร์โทร {phone_number} ทีมงานจะไปถึงที่เร็วที่สุดค่ะ!"

# ใช้สำหรับจัดการลูกค้าที่ปฏิเสธการขอความช่วยเหลือ โดยแสดงความสุภาพและเปิดโอกาสให้ลูกค้าติดต่อกลับในภายหลัง
class Decline_Assistance_Tool(BaseTool):
   
    name = "decline_assistance_tool"
    description = "Tool for handling customers who decline assistance."
    parameters = [
        {"name": "customer_name", "type": "string", "description": "Customer's full name."},
    ]


    required = [
        "customer_name"
    ]


    def use(customer_name: str):
        return f"ไม่เป็นไรค่ะ คุณ{customer_name} หากต้องการความช่วยเหลือในภายหลัง สามารถติดต่อเราได้ตลอดเวลานะคะ ขอบคุณค่ะ!"

# ใช้สำหรับจัดการการติดตามลูกค้าในภายหลัง เช่น กรณีที่ลูกค้าต้องการความช่วยเหลือเพิ่มเติม หรือเพื่อตรวจสอบสถานการณ์
class Follow_Up_Assistance_Tool(BaseTool):
   
    name = "follow_up_assistance_tool"
    description = "Tool for scheduling follow-ups regarding vehicle breakdowns."
    parameters = [
        {"name": "customer_name", "type": "string", "description": "Customer's full name."},
        {"name": "follow_up_date", "type": "string", "description": "Date for follow-up call."},
    ]


    required = [
        "customer_name", "follow_up_date"
    ]


    def use(customer_name: str, follow_up_date: str):
        return f"คุณ{customer_name} เราจะติดต่อกลับในวันที่ {follow_up_date} เพื่อให้ความช่วยเหลือเพิ่มเติมหากจำเป็นนะคะ ขอบคุณค่ะ!"
