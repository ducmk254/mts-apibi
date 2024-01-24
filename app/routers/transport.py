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

@router.post('/add', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateTRSSchema,user_id: str = Depends(oauth2.require_user)):
    dataset_ref = client.dataset('transport_public')
    table_ref = dataset_ref.table('raw_transport')
    if check_table('raw_transport') == False:
        create_table('raw_transport')
    table = client.get_table(table_ref)

    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.Id},]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_transport',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId(user_id),
        data_id = payload.Id,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId(user_id)
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId(user_id)
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}

@router.post('/update_status', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.UPDATETRSSchema,user_id: str = Depends(oauth2.require_user)):
    dataset_ref = client.dataset('transport_public')
    table_ref = dataset_ref.table('raw_transport_status')
    if check_table('raw_transport_status') == False:
        create_table('raw_transport_status')
    table = client.get_table(table_ref)

    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.Id},]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_transport_status',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId(user_id),
        data_id = payload.Id,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId(user_id)
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId(user_id)
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}
    
@router.post('/vintrans/add', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.CreateVINTRANSchema,user_id: str = Depends(oauth2.require_user)):
    dataset_ref = client.dataset('transport_public')
    table_ref = dataset_ref.table('raw_transport_vintrans')
    if check_table('raw_transport_vintrans') == False:
        create_table('raw_transport_vintrans')
    table = client.get_table(table_ref)
    payload.Ncc = 'Vintrans'
    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.Id},]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_transport_vintrans',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId(user_id),
        data_id = payload.Id,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId(user_id)
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId(user_id)
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}

@router.post('/vintrans/update_status', response_model=schemas.HistoryResponse)
async def create_history(payload: schemas.UPDATEVINTRANSchema,user_id: str = Depends(oauth2.require_user)):
    dataset_ref = client.dataset('transport_public')
    table_ref = dataset_ref.table('raw_transport_status_vintrans')
    if check_table('raw_transport_status_vintrans') == False:
        create_table('raw_transport_status_vintrans')
    table = client.get_table(table_ref)
    payload.Ncc = 'Vintrans'
    rows_to_insert = [{"data":ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),"data_id":payload.Id},]
    errors = client.insert_rows_json(table, rows_to_insert) 
    historyadd = schemas.HistoryBaseSchema(
        name = 'raw_transport_status_vintrans',
        data =  ujson.dumps(payload.__dict__, default = str, ensure_ascii=False),
        user_id = ObjectId(user_id),
        data_id = payload.Id,
        status = True,
        noteerror = ''
    )
    if errors == []:
        historyadd.status = True
        historyadd.user_id = ObjectId(user_id)
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = ''
        History.insert_one(historyadd.dict())
        return {"status": "success", "data": ujson.dumps(payload.__dict__, default=str, ensure_ascii=False) }
    else:
        historyadd.status = False
        historyadd.user_id = ObjectId(user_id)
        historyadd.emitted_at = datetime.utcnow()
        historyadd.noteerror = str(errors[0]['errors'])
        History.insert_one(historyadd.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}

def create_table(Tablename):
    table_id = "dw-mutosi.transport_public." + Tablename
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
    dataset_ref = bigquery.DatasetReference("dw-mutosi", "transport_public")
    table_ref = bigquery.TableReference(dataset_ref, table_id)
    try:
        client.get_table(table_ref)
        return True
    except Exception as e:
        return False