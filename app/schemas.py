from datetime import datetime
from pydantic import BaseModel, EmailStr, constr
from bson import ObjectId
from typing import List

class UserBaseSchema(BaseModel):
    name: str
    email: str
    photo: str
    role: str | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    verified: bool = False


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponseSchema(UserBaseSchema):
    id: str
    pass


class UserResponse(BaseModel):
    status: str
    user: UserResponseSchema


class HistoryBaseSchema(BaseModel):
    name: str
    emitted_at:  datetime | None = None
    data: str
    user_id:ObjectId
    data_id:str
    status:bool
    noteerror:str

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True

class CreateHistorySchema(HistoryBaseSchema):
    name: str
    data: str
    user_id:str
    data_id:str
    status:bool
    noteerror:str

class HistoryResponseSchema(HistoryBaseSchema):
    name: str
    data: str
    user_id:str
    data_id:str
    status:bool
    noteerror:str

class HistoryResponse(BaseModel):
    status: str
    data: str

class CreateSAP_ZSD05Schema(BaseModel):
    # Sales document
    AUBEL: str
    # Delivery
    VGBEL: str
    # Billing Document
    VBELN:str
    #Bill Date
    FKDAT:str
    # Billing Cancel
    FKSTO:str
    # Document Number
    BELNR:str
    #Document Date
    AUDAT: str
    #Payer
    KUNRG:str
    #Distribution Channel
    VTWEG:str
    #Material
    MATNR:str
    #Billed Quantity
    FKIMG: str
    #Sales unit
    VRKME:str
    #Net Value
    NETWR: str
    #GiaVon
    ZGIAVON:str
    #Create date
    ERDAT:str
    # Billing Items
    POSNR:str 
    # BATCH
    BATCH:str | None = None  
    # Customer_Reference
    BSTKD:str | None = None 


class CreateSAP_ZWM06Schema(BaseModel):
    # month
    ID: str | None = None  
    # month
    MONTH: str | None = None  
    # year
    YEAR: str | None = None  
    # Plant
    PLANT:str | None = None  
    # Valuation Type
    VALUATION_TYPE:str | None = None  
    #Material
    MATNR:str | None = None  
    #Material Description
    MATNR_DES:str | None = None  
    #Material type
    MATNR_TYPE:str | None = None  
    #MaterialTypeDesc
    MATNR_TYPE_DES:str | None = None  
    #MaterialGroup
    MATNR_GR:str | None = None  
    #MaterialGrpDesc
    MATNR_GR_DES:str | None = None  
    #DVT
    DVT:str | None = None  
    #TonCuoiKy
    TonCuoiKy:str | None = None  
    #GTCuoiKy
    GTCuoiKy:str | None = None  
    #ValuationClass
    VALUECLASS:str | None = None  
    #GLAccount
    GLACC:str | None = None  

class CreateListSAP_ZWM06Schema(BaseModel):
    data: List[CreateSAP_ZWM06Schema]

class CreateSAP_ZWM08Schema(BaseModel):
    # month
    ID: str | None = None  
    # month
    MONTH: str | None = None  
    # year
    YEAR: str | None = None  
    # StorageLocation
    STORAGELOCATION:str | None = None  
    #Material
    MATNR:str | None = None  
    #Material Description
    MATNR_DES:str | None = None  
    #Material type
    MATNR_TYPE:str | None = None  
    #MaterialTypeDesc
    MATNR_TYPE_DES:str | None = None  
    #ValuationType
    VALUATION_TYPE:str | None = None  
    # SpecialStock
    SPECIALSTOCK:str | None = None  
    #SpecialStockNumber
    SPECIALSTOCK_NUMBER:str | None = None  
    #Quantity
    QUANTITY:str | None = None  
    #Unit
    UNIT:str | None = None  
    #UnitPrice
    UNITPRICE:str | None = None  
    #Amount
    AMOUNT:str | None = None  
    #30days
    DAYS_30:str | None = None  
    #60days
    DAYS_60:str | None = None  
    #90days
    DAYS_90:str | None = None  
    #120days
    DAYS_120:str | None = None  
    #130days
    DAYS_130:str | None = None  
    #số ngày tồn thực tế
    SONGAYTON:str | None = None  
    # BATCH
    BATCH:str | None = None 
    # CHECK
    CHECK:str | None = None  

class CreateListSAP_ZWM08Schema(BaseModel):
    data: List[CreateSAP_ZWM08Schema]

class CreateSAP_ZAR10ASchema(BaseModel):
    # month
    LFMON: str  | None = None
    # year
    GJAHR: str  | None = None
    # Customer
    PARTNER:str  | None = None
     # level 1
    LEVEL1: str | None = None 
    #Distribution Channel
    VTWEG:str  | None = None
    #Revenue YTD2023
    REVENUE_N:str  | None = None
    #Target2023
    TARGET:str  | None = None
    # Actual / Target
    TYLE:str  | None = None
    #Credit Limit
    CREDIT_LIMIT:str  | None = None
    #Revenue YTD2022
    REVENUE_O:str  | None = None
    #Total Receivable
    TOTAL:str  | None = None
    #<30 days
    PERIOD_1:str  | None = None
    #30 days < AR < 45 days
    PERIOD_2:str  | None = None
    #45 days < AR < 60 days
    PERIOD_3:str  | None = None
    #60 days < AR < 90 days
    PERIOD_4:str  | None = None
    #90 days < AR < 120 days
    PERIOD_5:str  | None = None
    #>120 days
    PERIOD_6:str  | None = None

class CreateSAP_ZAP03NSchema(BaseModel):
    # month
    LFMON: str | None = None  
    # year
    GJAHR: str | None = None  
    # level 1
    LEVEL1: str | None = None 
    # Suppliers' Code
    LIFNR:str | None = None  
    #Purchased
    PURCHASE_N:str | None = None  
    #Payables Amount
    PAYABLES:str | None = None  
    #30 days
    PERIOD_1:str | None = None  
    #30 days < AP < 60 days
    PERIOD_2:str | None = None  
    # 60 days < AP < 90 days
    PERIOD_3:str | None = None  
    #90 days < AP < 120 days
    PERIOD_4:str | None = None  
    #> 120 days
    PERIOD_5:str | None = None  
    #Note
    NOTE:str | None = None  

class CreateSAP_ZGL05NSchema(BaseModel):
    # month
    MONAT: str | None = None  
    # year
    GJAHR: str | None = None  
    # Customer
    RACCT:str | None = None  
    #Customer Name
    SKBEZ:str | None = None  
    #Debit
    LAST_DMBTR_S:str | None = None  
    #Credit
    LAST_DMBTR_H:str | None = None  
    #HanMuc
    DMBTR_S:str | None = None  
    #HanMuc
    DMBTR_H:str | None = None  
    #HanMuc
    END_DMBTR_S:str | None = None  
    #HanMuc
    END_DMBTR_H:str | None = None   

class CreateListSAP_ZGL05NSchema(BaseModel):
    data: List[CreateSAP_ZGL05NSchema]

class CreateSAP_ZAR03Schema(BaseModel):
    # month
    MONAT: str | None = None  
    # year
    GJAHR: str | None = None  
    # Account No
    KUNNR_LIFNR:str | None = None 
    # Account
    HKONT:str | None = None 
    #Description
    DMBTR_S_DK:str | None = None  
    #Debit
    DMBTR_H_DK:str | None = None  
    #Credit
    DMBTR_S_TK:str | None = None  
    #Credit
    DMBTR_H_TK:str | None = None  
    #Credit
    DMBTR_S_CK:str | None = None  
    #Credit
    DMBTR_H_CK:str | None = None  

class CreateListSAP_ZAR03Schema(BaseModel):
    data: List[CreateSAP_ZAR03Schema]

class CreateSAP_ZGL07Schema(BaseModel):
    # month
    MONTH: str | None = None  
    # year
    YEAR: str | None = None  
    # DoanhThuBHVaCCDV
    CHITIEU :str | None = None  
    #CacKhoanGiamTruDoanhThu
    MASO:str | None = None  
    #CacKhoanGiamTruDoanhThu
    THUYETMINH:str | None = None  
    #DTBHCCDV
    Value_n:str | None = None  
    #GVBH
    Value_0:str | None = None  
    #LNGBHDV
    Luyke_n:str | None = None  
    #DTHoatDongTC
    Luyke_0:str | None = None 

class CreateListSAP_ZGL07Schema(BaseModel):
    data: List[CreateSAP_ZGL07Schema]

class CreateSAP_FAGLL03HSchema(BaseModel):
     # G/L Account
    COMPANY_CODE:str | None = None
    # G/L Account
    FISCAL_YEAR:str | None = None
    # G/L Account
    LINE_ITEM:str | None = None
    # month
    MONTH: str | None = None  
    # Transaction Code
    TRANSACTION_CODE:str | None = None  
    #Customer
    DOCNUMENT_NUMBER:str | None = None  
    #Supplier
    CUSTOMER:str | None = None  
    #Company Code Currency Value
    SUPPLIER:str | None = None  
    #G/L Account
    GL_ACCOUNT:str | None = None  
    #G/L Account: Long Text
    OFFSETTING_ACCOUNT:str | None = None  
    #Offsetting Account
    COST_CENTER:str | None = None  
    #Document Header Text
    COMPANYCODE_VALUE:str | None = None  
    #Company Code Currency Key
    GL_ACCOUNT_TEXT:str | None = None  
    #Document Currency Value
    DOCUMENT_HEADER_TEXT:str | None = None  
    #Document Date
    COMPANY_CODE_CURRENCY_KEY:str | None = None  
    #Posting Date
    DOCUMENT_CURRENCY_VALUE:str | None = None  
    #Net Due Date
    DOCUMENT_DATE:str | None = None  
    #Entry Date
    POSTING_DATE:str | None = None  
    #Quantity
    ENTRY_DATE:str | None = None  
    #Unit of Measure
    QUANTITY:str | None = None  
    #Purchasing Document
    UNIT:str | None = None  
    #Cost Center
    PURCHASING:str | None = None  
    #Order
    ORDER:str | None = None  
    #Document Currency Key
    DOCUMENT_CURRENCY_KEY:str | None = None 

class CreateListSAP_FAGLL03HSchema(BaseModel):
    data: List[CreateSAP_FAGLL03HSchema]


class CreateSAP_FBL1NSchema(BaseModel):
    # G/L Account
    COMPANY_CODE:str | None = None
    # G/L Account
    FISCAL_YEAR:str | None = None
    # G/L Account
    LINE_ITEM:str | None = None
    # G/L Account
    ACCOUNT:str | None = None  
    #Document type
    DOCUMENT_NUMBER:str | None = None  
    #Posting date
    GL_ACCOUNT:str | None = None  
    #Amount in local Currency
    POSTING_DATE:str | None = None  
    #Amount in local Currency
    DC_IND:str | None = None  
    #Amount in local Currency
    ACCOUNT_NAME:str | None = None  
    #Amount in local Currency
    ASSIGNMENT:str | None = None  
    #Amount in local Currency
    REFERENCE:str | None = None  
    #Amount in local Currency
    DOCUMENT_TYPE:str | None = None  
    #Amount in local Currency
    DOCUMENT_DATE:str | None = None  
    #Amount in local Currency
    BASELINE_PAYMENT:str | None = None 
    #Amount in local Currency
    NETDUE_DATE:str | None = None 
    #Amount in local Currency
    SPECIAL_GL:str | None = None 
    #Amount in local Currency
    NETDUE_DATE_SYMBOL:str | None = None 
    #Amount in local Currency
    ARREARS_DATE:str | None = None 
    #Amount in local Currency
    AMOUNT_LOCAL:str | None = None 
    #Amount in local Currency
    LOCAL_CURRENCY:str | None = None 
    #Amount in local Currency
    AMOUNT_DOC:str | None = None 
    #Amount in local Currency
    DOCUMENT_CURRENCY:str | None = None 
    #Amount in local Currency
    CLEARING_DOCUMENT:str | None = None 
    #Amount in local Currency
    CLEARING_DATE:str | None = None 
    #Amount in local Currency
    TEXT:str | None = None 
    #Amount in local Currency
    INVOICE_REFERENCE:str | None = None 

class CreateListSAP_FBL1NSchema(BaseModel):
    data: List[CreateSAP_FBL1NSchema]

class CreateSAP_FBL5NSchema(BaseModel):
    # G/L Account
    COMPANY_CODE:str | None = None
    # G/L Account
    FISCAL_YEAR:str | None = None
    # G/L Account
    LINE_ITEM:str | None = None
    # G/L Account
    GL_ACCOUNT:str | None = None  
    #Document type
    DOCUMENT_NUMBER:str | None = None  
    #Posting date
    DOCUMENT_DATE:str | None = None  
    #Amount in local Currency
    ITEMS_SYMBOL:str | None = None  
    #Amount in local Currency
    ASSIGNMENT:str | None = None  
    #Amount in local Currency
    DOCUMENT_TYPE:str | None = None  
    #Amount in local Currency
    SPECIAL_GL:str | None = None  
    #Amount in local Currency
    NETDUE_DATE:str | None = None  
    #Amount in local Currency
    AMOUNT_LOCAL:str | None = None  
    #Amount in local Currency
    LOCAL_CURRENCY:str | None = None  
    #Amount in local Currency
    CLEARING_DOCUMENT:str | None = None  
    #Amount in local Currency
    TEXT:str | None = None

class CreateListSAP_FBL5NSchema(BaseModel):
    data: List[CreateSAP_FBL5NSchema]

class CreateSAP_ZCO01Schema(BaseModel):
    # month
    MONTH: str | None = None  
    # year
    YEAR: str | None = None 
    # Material
    PLANT:str | None = None   
    # Material
    MATERIAL:str | None = None  
    #Valuation Type
    VALUATION_TYPE:str | None = None  
    #Base Unit of Measure
    UNIT:str | None = None  
    #Số lượng nhập kho
    SLNHAPKHO: str | None = None  
    #Currency
    CURRENCY: str | None = None  
    #Tổng giá trị thực tế
    TONGGIATRITT: str | None = None  
    #Cost Component
    COSTCOMPONENT: str | None = None  
    #Giá thành đơn vị thực tế
    GIATHANHTT: str | None = None  
    #Giá thành đơn vị kế hoạch
    GIATHANHKH: str | None = None  
    #% chênh lệch giá thành đơn vị thực tế và
    CHENHLECHGIA: str | None = None  
    #Nguyên vật liệu
    NVL: str | None = None  
    #Chi phí nhân công TT
    CHIPHINC: str | None = None  
    #Nhân công gián tiếp
    NCGT: str | None = None  
    #Chi phí khấu hao
    CHIPHIKHAUHAO: str | None = None  
    #Chi phí chung
    CHIPHICHUNG: str | None = None  
    #Chi phí điện
    CHIPHIDIEN: str | None = None  
    #Vật tư tiêu hao
    VTTIEUHAO: str | None = None  
    #CP gia công ngoài
    CPGIACONGNGOAI: str | None = None 

class CreateListSAP_ZCO01Schema(BaseModel):
    data: List[CreateSAP_ZCO01Schema]

class CreateSAP_CATEGORYSchema(BaseModel):
    # G/L Account
    CODE:str
    #Document type
    NAME:str

class CreateSAP_DISTRIBUTIONCHANNELSchema(BaseModel):
    # G/L Account
    CODE:str
    #Document type
    NAME:str

class CreateSAP_DISTRIBUTORLSchema(BaseModel):
    # CUSTOMER_CODE
    CUSTOMER_CODE:str
    #BP_EXTERNAL
    BP_EXTERNAL:str
    #PREV_ACCT_NO_
    PREV_ACCT_NO_:str
    #PLANNING_GROUP
    PLANNING_GROUP:str
    #CUSTOMER_NAME
    CUSTOMER_NAME:str
    #TAX_NUMBER
    TAX_NUMBER:str
    #VAT_CODE
    VAT_CODE:str
    #RECON__ACCOUNT
    RECON__ACCOUNT:str
    #PAYMENT_METHODS
    PAYMENT_METHODS:str
    #DESC_PAYMENTTERM
    DESC_PAYMENTTERM:str
    #SALES_ORG_CODE_
    SALES_ORG_CODE_:str
    #SALES_ORG_NAME_
    SALES_ORG_NAME_:str
    #DISTRIBUTIN_CHANNEL
    DISTRIBUTIN_CHANNEL:str
    #DISTRIBUTIN_CHANNEL_DES
    DISTRIBUTIN_CHANNEL_DES:str
    #CUSTOMER_GROUP_CODE
    CUSTOMER_GROUP_CODE:str
    #CUSTOMER_GROUP_NAME
    CUSTOMER_GROUP_NAME:str
    #SALE_GROUP_CODE
    SALE_GROUP_CODE:str
    #SALE_OFFICE
    SALE_OFFICE:str
    #SALE_GROUP_NAME
    SALE_GROUP_NAME:str
    #SALES_DISTRICT
    SALES_DISTRICT:str
    #CITY
    CITY:str
    #DISTRICT
    DISTRICT:str
    #TELEPHONE
    TELEPHONE:str
    #EMAIL
    EMAIL:str
    #PAYER
    PAYER:str

class CreateSAP_MATERIALSchema(BaseModel):
    # Material Number
    ItemCode:str | None = None  
    #Material type
    ItemName:str | None = None  
    #Material Group
    MaterialGroup:str | None = None  
    #Material Group
    MaterialGroup_name:str | None = None  
    #Old material number
    Status:str | None = None  
    #Base Unit of Measure
    Division:str | None = None  
    #Material Description
    UnitCode:str | None = None  
     # Material Number
    VAT:str | None = None
     # Material Number
    Data_date:str | None = None
     # Material Number
    System:str | None = None
     # Material Number
    IntegrationType:str | None = None
     # Material Number
    Material_type:str | None = None
     # Material Number
    Old_material_number:str | None = None
     # Material Number
    Material_type__Diengiai:str | None = None
     # Material Number
    product_hierarchy:str | None = None
class CreateSAP_ZPP06Schema(BaseModel):
    # P.Order
    ORDER:str | None = None  
    #Bas. Start Date
    START_DATE:str | None = None  
    #Total Order Quantity
    ORDER_QUANTITY:str | None = None  
    #Base Unit of Measure
    UNIT:str | None = None  
    #Material
    MATERIAL:str | None = None  
    #Mat.Group
    MAT_GROUP:str | None = None  
    #Opertn task list no.
    TASK_LISTNO:str | None = None  
    #Total Quantity
    TOTAL_QUANTITY:str | None = None  
    #GR Quantity
    GR_QUANTITY:str | None = None  
    #Value of goods rec.
    VALUE_OF_GOOD:str | None = None  
    #Work Center
    WORK_CENTER:str | None = None  

class CreateListSAP_ZPP06Schema(BaseModel):
    data: List[CreateSAP_ZPP06Schema]

class CreateSAP_ZSD09Schema(BaseModel):
    # month
    MONTH: str | None = None  
    # year
    YEAR: str | None = None  
    # Customer
    CUSTOMER:str | None = None  
    #Tổng đơn đã đặt 
    TONGDONDADAT:str | None = None  
    #Tỷ lệ giao hàng thành công
    TYLEGIAOHANG:str | None = None  
    #Giao hàng thành công
    GIAOHANGTHANHCONG:str | None = None  
    #Ðang giao hàng
    DANGGIAOHANG:str | None = None  
  
class CreateTRSSchema(BaseModel):
    Id:int
    Code:str
    PartnerCode: str | None = None
    Status: int
    StatusName:str
    CreateDate:str
    FinishDate:str | None = None
    DeadlineDate:str | None = None
    RecipientName:str | None = None
    RecipientAddress:str | None = None
    RecipientPhone:str | None = None
    CitySendName:str | None = None
    CityRecipientName:str | None = None
    ServiceName:str | None = None
    Weight:float | None = None
    Number:int | None = None 
    Amount:float | None = None
    COD:float | None = None
    Noted:str | None = None
    NotedUnableShip:str | None = None
    Recipient_reality:str | None = None
    RequestCode:str | None = None
    LicensePlate:str | None = None
    OfficerPickup:str | None = None
    Phone:str | None = None
    StatusRequest:str | None = None
    Ncc:str

class UPDATETRSSchema(BaseModel):
    Id:int
    Code:str | None = None
    Status: int
    StatusName:str
    FinishDate:str
    CreateDate:str
    Noted:str | None = None
    NotedUnableShip:str | None = None
    Ncc:str 

class CreateVINTRANSchema(BaseModel):
    Id:int
    SenderId:int
    Code:str
    PartnerCode: str | None = None
    Status: int
    StatusName:str
    CreateDate:str
    MiningDay:str | None = None
    Deadline:str | None = None
    SenderName:str | None = None
    SenderCompany:str | None = None
    SenderPhone:str | None = None
    SenderAddress:str | None = None
    RecipientName:str | None = None
    RecipientAddress:str | None = None
    RecipientCompany:str | None = None
    RecipientPhone:str | None = None
    CitySendName:str | None = None
    CityRecipientName:str | None = None
    DistrictRecipientCode:str | None = None
    DistrictRecipientName:str | None = None
    ServiceCode:str | None = None
    ServiceName:str | None = None
    Weight:float | None = 0
    Mass:float | None = 0
    Number:float | None = 0
    PriceMain:float | None = 0
    OnSiteDeliveryMoney:float | None = 0
    BPPrice:float | None = 0
    THBBPrice: float | None = 0
    PDKPrice: float | None = 0
    PackPrice:float | None = 0
    DeliverySurcharge:float | None = 0
    COD: float | None = 0
    CODPrice: float | None = 0
    Insured: float | None = 0
    InsuredPrice: float | None = 0
    PPXDMoney: float | None = 0 
    VATMoney: float | None = 0
    Amount: float | None = 0
    Description: str | None = None
    Noted:str | None = None
    OfficerCSName:str | None = None
    OfficerCSPhone:str | None = None
    Ncc:str | None = None

class UPDATEVINTRANSchema(BaseModel):
    Id:int
    SenderId:int
    Code:str | None = None
    Status: str
    StatusName:str
    DateTime:str | None = None
    OfficerName:str | None = None
    POName:str | None = None
    Mobile:str | None = None
    Note:str | None = None
    TypeReason:str | None = None
    FinishDate:str | None = None
    RecipientReality:str | None = None
    Ncc:str | None = None

class CreateSAP_Customerchema(BaseModel):
    # Customer Code
    CustomerCode:str | None = None  
    #SalesOrg
    SalesOrg:str | None = None  
    #CustomerName
    CustomerName:str | None = None  
    #Status
    Status:str | None = None  
    #Address
    Address:str | None = None  
    #Mat.Group
    District:str | None = None  
    #Opertn task list no.
    City:str | None = None  
    #Total Quantity
    Country:str | None = None  
    #GR Quantity
    TaxCode:str | None = None  
    #Value of goods rec.
    Phone:str | None = None  
    #Work Center
    Emailcode:str | None = None 
    #Work Center
    Contact:str | None = None
    #Work Center
    Channel:str | None = None
    #Work Center
    Division:str | None = None
    #Work Center
    CustomerGroup:str | None = None
    #Work Center
    SalesOffice:str | None = None
    #Work Center
    SalesGroup:str | None = None
    #Work Center
    SalesCode:str | None = None
    #Work Center
    Data_date:str | None = None
    #Work Center
    System:str | None = None
    #Work Center
    IntegrationType:str | None = None


class CreateSAP_ZPP07chema(BaseModel):
    # month
    MONTH: str | None = None  
    # year
    YEAR: str | None = None  
    #SalesOrg
    WERKS:str | None = None  
    #CustomerName
    MATNR:str | None = None  
    #Status
    MAKTX:str | None = None  
    #Address
    BISMT:str | None = None  
    #Mat.Group
    MEINS:str | None = None  
    #Opertn task list no.
    ESTOCK:str | None = None  
    #Total Quantity
    STOCKMB:str | None = None  
    #GR Quantity
    STOCKMN:str | None = None  
    #Value of goods rec.
    KHSX1:str | None = None  
    #Work Center
    KHSX2:str | None = None 
    #Work Center
    KHSX3:str | None = None
    #Work Center
    KHMH1:str | None = None
    #Work Center
    KHMH2:str | None = None
    #Work Center
    KHMH3:str | None = None
    #Work Center
    KHBH1:str | None = None
    #Work Center
    KHMH2:str | None = None
    #Work Center
    KHMH3:str | None = None
    #Work Center
    KHBH1:str | None = None
    #Work Center
    KHBH2:str | None = None
    #Work Center
    KHBH3:str | None = None
    #Work Center
    KHTK1:str | None = None
    #Work Center
    KHTK2:str | None = None
    #Work Center
    KHTK3:str | None = None

class CreateListSAP_ZPP07chema(BaseModel):
    data: List[CreateSAP_ZPP07chema]