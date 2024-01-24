def historyEntity(history) -> dict:
    return {
        "id": str(history["_id"]),
        "user_id": history["user_id"],
        "name": history["name"],
        "data": history["data"],
        "emitted_at": history["emitted_at"],
        "data_id": history["data_id"],
        "status": history["status"],
        "noteerror": history["noteerror"],
    }


def historyResponseEntity(history) -> dict:
    return {
        "id": str(history["_id"]),
        "user_id": history["user_id"],
        "name": history["name"],
        "data": history["data"],
        "emitted_at": history["emitted_at"],
        "data_id": history["data_id"],
        "status": history["status"],
        "noteerror": history["noteerror"],
    }


def historyListEntity(historys) -> list:
    return [historyEntity(user) for user in historys]
