from datetime import datetime
from http.client import NOT_FOUND
from bson import ObjectId
from fastapi import APIRouter, Depends
from app.serializers.historySerializers import historyResponseEntity
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
async def create_history(payload: schemas.CreateHistorySchema):
    dataset_ref = client.dataset('sap_public')
    table_ref = dataset_ref.table(payload.name)
    if check_table(payload.name) == False:
        create_table(payload.name)
    table = client.get_table(table_ref)
    rows_to_insert = [{"data":payload.data,"data_id":payload.data_id},]
    errors = client.insert_rows_json(table, rows_to_insert) 

    if errors == []:
        payload.status = True
        payload.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        payload.emitted_at = datetime.utcnow()
        payload.noteerror = ''
        History.insert_one(payload.dict())
        return {"status": "success", "data": payload.data }
    else:
        payload.status = False
        payload.user_id = ObjectId('64250f671f3fbfc4ac1c04c4')
        payload.emitted_at = datetime.utcnow()
        payload.noteerror = str(errors[0]['errors'])
        History.insert_one(payload.dict())
        return {"status": "error", "data": str(errors[0]['errors'])}
    

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