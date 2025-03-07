from enum import IntEnum


class MessageTemplateDto(IntEnum):
    Button = 0
    Custom = 1
    CustomerFeedback = 2
    Generic = 3
    Media = 4
    Product = 5
    Receipt = 6