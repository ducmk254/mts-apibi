from datetime import datetime
from http.client import NOT_FOUND
import ujson
from bson import ObjectId
from fastapi import APIRouter, Depends
from google.cloud import bigquery
from google.oauth2 import service_account
credentials = service_account.Credentials.from_service_account_file(
'./dw-mutosi-047c9c3d37a7.json')

project_id = 'dw-mutosi'
client = bigquery.Client(credentials= credentials,project=project_id)

from app.database import History
from .. import schemas, oauth2

router = APIRouter()


@router.post('/zsd05', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateSAP_ZSD05Schema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_zsd05')
    if check_table('raw_sap_zsd05') == False:
        create_table('raw_sap_zsd05')
    table = client.get_table(table_ref)

    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.AUBEL + payload.VGBEL + payload.VBELN + payload.BELNR + payload.POSNR},]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_sap_zsd05',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
        data_id = payload.AUBEL + payload.VGBEL + payload.VBELN + payload.BELNR + payload.POSNR,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}

@router.post('/zwm06', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateListSAP_ZWM06Schema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_zwm06')
    if check_table('raw_sap_zwm06') == False:
        create_table('raw_sap_zwm06')
    table = client.get_table(table_ref)

    for item in payload.data:
        rows_to_insert = [{"data":ujson.dumps(item.__dict__, default = str, ensure_ascii=False),"data_id":item.ID + item.MONTH + item.YEAR},]
        errors = client.insert_rows_json(table, rows_to_insert) 
        historyadd = schemas.HistoryBaseSchema(
            name = 'raw_sap_zwm06',
            data =  ujson.dumps(item.__dict__, default = str, ensure_ascii=False),
            user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
            data_id = item.ID + item.MONTH + item.YEAR,
            status = True,
            noteerror = ''
        )
        if errors == []:
            historyadd.status = True
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = ''
            History.insert_one(historyadd.dict())
            
        else:
            historyadd.status = False
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = str(errors[0]['errors'])
            History.insert_one(historyadd.dict())
            return {"status": "error", "data": str(errors[0]['errors'])}
    return {"status": "success", "data": "Thành công" }

@router.post('/zwm08', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateListSAP_ZWM08Schema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_zwm08')
    if check_table('raw_sap_zwm08') == False:
        create_table('raw_sap_zwm08')
    table = client.get_table(table_ref)
    for item in payload.data:
        rows_to_insert = [{"data":ujson.dumps(item.__dict__, default = str, ensure_ascii=False),"data_id":item.ID},]
        errors = client.insert_rows_json(table, rows_to_insert) 
        historyadd = schemas.HistoryBaseSchema(
            name = 'raw_sap_zwm08',
            data =  ujson.dumps(item.__dict__, default = str, ensure_ascii=False),
            user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
            data_id = item.ID,
            status = True,
            noteerror = ''
        )
        if errors == []:
            historyadd.status = True
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = ''
            History.insert_one(historyadd.dict())
            
        else:
            historyadd.status = False
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = str(errors[0]['errors'])
            History.insert_one(historyadd.dict())
            return {"status": "error", "data": str(errors[0]['errors'])}
    return {"status": "success", "data": "Thành công" }

@router.post('/zar10a', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateSAP_ZAR10ASchema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_zar10a')
    if check_table('raw_sap_zar10a') == False:
        create_table('raw_sap_zar10a')
    table = client.get_table(table_ref)

    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.LFMON + payload.GJAHR + payload.VTWEG + payload.PARTNER + payload.LEVEL1},]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_sap_zar10a',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
        data_id = payload.LFMON + payload.GJAHR + payload.VTWEG + payload.PARTNER + payload.LEVEL1,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}

@router.post('/zap03n', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateSAP_ZAP03NSchema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_zap03n')
    if check_table('raw_sap_zap03n') == False:
        create_table('raw_sap_zap03n')
    table = client.get_table(table_ref)

    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.LFMON + payload.GJAHR  + payload.LEVEL1 + payload.LIFNR  },]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_sap_zap03n',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
        data_id = payload.LFMON + payload.GJAHR  + payload.LEVEL1 + payload.LIFNR,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}

@router.post('/zgl05n', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateListSAP_ZGL05NSchema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_zgl05n')
    if check_table('raw_sap_zgl05n') == False:
        create_table('raw_sap_zgl05n')
    table = client.get_table(table_ref)
    for item in payload.data:
        rows_to_insert = [{"data":ujson.dumps(item.__dict__, default = str, ensure_ascii=False),"data_id":item.MONAT + item.GJAHR + item.RACCT},]
        errors = client.insert_rows_json(table, rows_to_insert) 
        historyadd = schemas.HistoryBaseSchema(
            name = 'raw_sap_zgl05n',
            data =  ujson.dumps(item.__dict__, default = str, ensure_ascii=False),
            user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
            data_id = item.MONAT + item.GJAHR + item.RACCT,
            status = True,
            noteerror = ''
        )
        if errors == []:
            historyadd.status = True
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = ''
            History.insert_one(historyadd.dict())
            
        else:
            historyadd.status = False
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = str(errors[0]['errors'])
            History.insert_one(historyadd.dict())
            return {"status": "error", "data": str(errors[0]['errors'])}
    return {"status": "success", "data": "Thành công" }

@router.post('/zar03', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateListSAP_ZAR03Schema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_zar03')
    if check_table('raw_sap_zar03') == False:
        create_table('raw_sap_zar03')
    table = client.get_table(table_ref)

    for item in payload.data:
        rows_to_insert = [{"data":ujson.dumps(item.__dict__, default = str, ensure_ascii=False),"data_id":item.MONAT + item.GJAHR + item.KUNNR_LIFNR + item.HKONT},]
        errors = client.insert_rows_json(table, rows_to_insert) 
        historyadd = schemas.HistoryBaseSchema(
            name = 'raw_sap_zar03',
            data =  ujson.dumps(item.__dict__, default = str, ensure_ascii=False),
            user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
            data_id = item.MONAT + item.GJAHR + item.KUNNR_LIFNR + item.HKONT,
            status = True,
            noteerror = ''
        )
        if errors == []:
            historyadd.status = True
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = ''
            History.insert_one(historyadd.dict())
            
        else:
            historyadd.status = False
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = str(errors[0]['errors'])
            History.insert_one(historyadd.dict())
            return {"status": "error", "data": str(errors[0]['errors'])}
    return {"status": "success", "data": "Thành công" }

@router.post('/zgl07', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateListSAP_ZGL07Schema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_zgl07')
    if check_table('raw_sap_zgl07') == False:
        create_table('raw_sap_zgl07')
    table = client.get_table(table_ref)
    for item in payload.data:
        rows_to_insert = [{"data":ujson.dumps(item.__dict__, default = str, ensure_ascii=False),"data_id":item.MONTH +item.YEAR + item.CHITIEU +item.MASO+item.THUYETMINH},]
        errors = client.insert_rows_json(table, rows_to_insert) 
        historyadd = schemas.HistoryBaseSchema(
            name = 'raw_sap_zgl07',
            data =  ujson.dumps(item.__dict__, default = str, ensure_ascii=False),
            user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
            data_id = item.MONTH +item.YEAR + item.CHITIEU +item.MASO+item.THUYETMINH,
            status = True,
            noteerror = ''
        )
        if errors == []:
            historyadd.status = True
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = ''
            History.insert_one(historyadd.dict())
            
        else:
            historyadd.status = False
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = str(errors[0]['errors'])
            History.insert_one(historyadd.dict())
            return {"status": "error", "data": str(errors[0]['errors'])}
    return {"status": "success", "data": "Thành công" }

@router.post('/fagll03h', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateListSAP_FAGLL03HSchema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_fagll03h')
    if check_table('raw_sap_fagll03h') == False:
        create_table('raw_sap_fagll03h')
    table = client.get_table(table_ref)

    for item in payload.data:
        rows_to_insert = [{"data":ujson.dumps(item.__dict__, default = str, ensure_ascii=False),"data_id":item.COMPANY_CODE + item.DOCNUMENT_NUMBER + item.FISCAL_YEAR +item.LINE_ITEM},]
        errors = client.insert_rows_json(table, rows_to_insert) 
        historyadd = schemas.HistoryBaseSchema(
            name = 'raw_sap_fagll03h',
            data =  ujson.dumps(item.__dict__, default = str, ensure_ascii=False),
            user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
            data_id = item.MONTH + item.COMPANY_CODE + item.DOCNUMENT_NUMBER + item.FISCAL_YEAR +item.LINE_ITEM,
            status = True,
            noteerror = ''
        )
        if errors == []:
            historyadd.status = True
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = ''
            History.insert_one(historyadd.dict())
            
        else:
            historyadd.status = False
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = str(errors[0]['errors'])
            History.insert_one(historyadd.dict())
            return {"status": "error", "data": str(errors[0]['errors'])}
    return {"status": "success", "data": "Thành công" }

@router.post('/fbl1n', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateListSAP_FBL1NSchema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_fbl1n')
    if check_table('raw_sap_fbl1n') == False:
        create_table('raw_sap_fbl1n')
    table = client.get_table(table_ref)

    for item in payload.data:
        rows_to_insert = [{"data":ujson.dumps(item.__dict__, default = str, ensure_ascii=False),"data_id":item.COMPANY_CODE + item.DOCUMENT_NUMBER + item.FISCAL_YEAR +item.LINE_ITEM},]
        errors = client.insert_rows_json(table, rows_to_insert) 
        historyadd = schemas.HistoryBaseSchema(
            name = 'raw_sap_fbl1n',
            data =  ujson.dumps(item.__dict__, default = str, ensure_ascii=False),
            user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
            data_id = item.COMPANY_CODE + item.DOCUMENT_NUMBER + item.FISCAL_YEAR +item.LINE_ITEM,
            status = True,
            noteerror = ''
        )
        if errors == []:
            historyadd.status = True
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = ''
            History.insert_one(historyadd.dict())
            
        else:
            historyadd.status = False
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = str(errors[0]['errors'])
            History.insert_one(historyadd.dict())
            return {"status": "error", "data": str(errors[0]['errors'])}
    return {"status": "success", "data": "Thành công" }

@router.post('/fbl5n', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateListSAP_FBL5NSchema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_fbl5n')
    if check_table('raw_sap_fbl5n') == False:
        create_table('raw_sap_fbl5n')
    table = client.get_table(table_ref)
    for item in payload.data:
        rows_to_insert = [{"data":ujson.dumps(item.__dict__, default = str, ensure_ascii=False),"data_id":item.COMPANY_CODE + item.DOCUMENT_NUMBER + item.FISCAL_YEAR +item.LINE_ITEM},]
        errors = client.insert_rows_json(table, rows_to_insert) 
        historyadd = schemas.HistoryBaseSchema(
            name = 'raw_sap_fbl5n',
            data =  ujson.dumps(item.__dict__, default = str, ensure_ascii=False),
            user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
            data_id = item.COMPANY_CODE + item.DOCUMENT_NUMBER + item.FISCAL_YEAR +item.LINE_ITEM,
            status = True,
            noteerror = ''
        )
        if errors == []:
            historyadd.status = True
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = ''
            History.insert_one(historyadd.dict())
            
        else:
            historyadd.status = False
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = str(errors[0]['errors'])
            History.insert_one(historyadd.dict())
            return {"status": "error", "data": str(errors[0]['errors'])}
    return {"status": "success", "data": "Thành công" }

@router.post('/zco01', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateListSAP_ZCO01Schema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_zco01')
    if check_table('raw_sap_zco01') == False:
        create_table('raw_sap_zco01')
    table = client.get_table(table_ref)

    for item in payload.data:
        rows_to_insert = [{"data":ujson.dumps(item.__dict__, default = str, ensure_ascii=False),"data_id":item.MONTH + item.YEAR + item.PLANT + item.MATERIAL +item.VALUATION_TYPE},]
        errors = client.insert_rows_json(table, rows_to_insert) 
        historyadd = schemas.HistoryBaseSchema(
            name = 'raw_sap_zco01',
            data =  ujson.dumps(item.__dict__, default = str, ensure_ascii=False),
            user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
            data_id = item.MONTH + item.YEAR + item.PLANT + item.MATERIAL +item.VALUATION_TYPE,
            status = True,
            noteerror = ''
        )
        if errors == []:
            historyadd.status = True
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = ''
            History.insert_one(historyadd.dict())
            
        else:
            historyadd.status = False
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = str(errors[0]['errors'])
            History.insert_one(historyadd.dict())
            return {"status": "error", "data": str(errors[0]['errors'])}
    return {"status": "success", "data": "Thành công" }

@router.post('/category', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateSAP_CATEGORYSchema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_category')
    if check_table('raw_sap_category') == False:
        create_table('raw_sap_category')
    table = client.get_table(table_ref)

    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.ID},]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_sap_category',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
        data_id = payload.ID,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}

@router.post('/distributionchannel', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateSAP_DISTRIBUTIONCHANNELSchema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_distributionchannel')
    if check_table('raw_sap_distributionchannel') == False:
        create_table('raw_sap_distributionchannel')
    table = client.get_table(table_ref)

    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.ID},]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_sap_distributionchannel',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
        data_id = payload.ID,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}

@router.post('/distributor', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateSAP_DISTRIBUTORLSchema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_distributor')
    if check_table('raw_sap_distributor') == False:
        create_table('raw_sap_distributor')
    table = client.get_table(table_ref)

    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.ID},]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_sap_distributor',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
        data_id = payload.ID,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}

@router.post('/material', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateSAP_MATERIALSchema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_material')
    if check_table('raw_sap_material') == False:
        create_table('raw_sap_material')
    table = client.get_table(table_ref)

    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.ItemCode},]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_sap_material',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
        data_id = payload.ItemCode,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}

@router.post('/zpp06', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateListSAP_ZPP06Schema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_zpp06')
    if check_table('raw_sap_zpp06') == False:
        create_table('raw_sap_zpp06')
    table = client.get_table(table_ref)

    for item in payload.data:
        rows_to_insert = [{"data":ujson.dumps(item.__dict__, default = str, ensure_ascii=False),"data_id":item.ORDER},]
        errors = client.insert_rows_json(table, rows_to_insert) 
        historyadd = schemas.HistoryBaseSchema(
            name = 'raw_sap_zpp06',
            data =  ujson.dumps(item.__dict__, default = str, ensure_ascii=False),
            user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
            data_id = item.ORDER,
            status = True,
            noteerror = ''
        )
        if errors == []:
            historyadd.status = True
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = ''
            History.insert_one(historyadd.dict())
            
        else:
            historyadd.status = False
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = str(errors[0]['errors'])
            History.insert_one(historyadd.dict())
            return {"status": "error", "data": str(errors[0]['errors'])}
    return {"status": "success", "data": "Thành công" }

@router.post('/zsd09', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateSAP_ZSD09Schema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_zsd09')
    if check_table('raw_sap_zsd09') == False:
        create_table('raw_sap_zsd09')
    table = client.get_table(table_ref)

    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.ID},]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_sap_zsd09',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
        data_id = payload.ID,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}

@router.post('/customer', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateSAP_Customerchema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_customer')
    if check_table('raw_sap_customer') == False:
        create_table('raw_sap_customer')
    table = client.get_table(table_ref)

    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.CustomerCode},]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_sap_customer',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
        data_id = payload.CustomerCode,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}

@router.post('/zpp07', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateListSAP_ZPP07chema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table('raw_sap_zpp07')
    if check_table('raw_sap_zpp07') == False:
        create_table('raw_sap_zpp07')
    table = client.get_table(table_ref)
    for item in payload.data:
        rows_to_insert = [{"data":ujson.dumps(item.__dict__, default = str, ensure_ascii=False),"data_id":item.MONTH + item.YEAR + item.MATNR + item.WERKS},]
        errors = client.insert_rows_json(table, rows_to_insert) 
        historyadd = schemas.HistoryBaseSchema(
            name = 'raw_sap_zpp07',
            data =  ujson.dumps(item.__dict__, default = str, ensure_ascii=False),
            user_id = ObjectId('64250f671f3fbfc4ac1c04c4'),
            data_id = item.MONTH + item.YEAR + item.MATNR + item.WERKS,
            status = True,
            noteerror = ''
        )
        if errors == []:
            historyadd.status = True
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = ''
            History.insert_one(historyadd.dict())
            
        else:
            historyadd.status = False
            historyadd.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
            historyadd.emitted_at = datetime.utcnow()
            historyadd.noteerror = str(errors[0]['errors'])
            History.insert_one(historyadd.dict())
            return {"status": "error", "data": str(errors[0]['errors'])}
    return {"status": "success", "data": "Thành công" }

def create_table(Tablename):
    table_id = "dw-mutosi.sap_public." + Tablename
    schema = [
        bigquery.SchemaField("id", "STRING", default_value_expression="GENERATE_UUID()"),
        bigquery.SchemaField("emitted_at", "DATETIME", default_value_expression="CURRENT_DATETIME()"),
        bigquery.SchemaField("data", "STRING"),
        bigquery.SchemaField("data_id", "STRING")
    ]
    table = bigquery.Table(table_id, schema=schema)
    table = client.create_table(table)
    print(
        "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
    )

def check_table(table_id):
    dataset_ref = bigquery.DatasetReference("dw-mutosi", "sap_public")
    table_ref = bigquery.TableReference(dataset_ref, table_id)
    try:
        client.get_table(table_ref)
        return True
    except Exception as e:
        return False