from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Example marks data
marks_data = [{"name":"4jOgd1dnJ","marks":94},{"name":"Y","marks":87},{"name":"wQBD","marks":58},{"name":"sdBGO6xdgL","marks":85},{"name":"Rs8Lf","marks":8},{"name":"J2WlQ7","marks":18},{"name":"2","marks":72},{"name":"61lUsiKPDo","marks":8},{"name":"BW","marks":84},{"name":"2qFE","marks":34},{"name":"yaADYUaEKE","marks":43},{"name":"0","marks":72},{"name":"qJKGx","marks":29},{"name":"ILwD6DU3","marks":43},{"name":"S","marks":1},{"name":"bR8RToj","marks":42},{"name":"Ij5IrkhSr","marks":59},{"name":"4jChDCs5us","marks":92},{"name":"Bpvab","marks":48},{"name":"Nc4SLXe9c","marks":4},{"name":"iJa","marks":60},{"name":"0ysKftQoH","marks":43},{"name":"nXCEi5","marks":84},{"name":"Ctg","marks":91},{"name":"h","marks":17},{"name":"RW8EeV","marks":90},{"name":"SsAUr","marks":49},{"name":"UH","marks":83},{"name":"30pvRd","marks":38},{"name":"F","marks":68},{"name":"phigV","marks":72},{"name":"4","marks":21},{"name":"O2YoHkkH","marks":48},{"name":"7Dxw99fRx","marks":43},{"name":"Vd1","marks":99},{"name":"k","marks":18},{"name":"1KvDxAv","marks":14},{"name":"sTx28WMmai","marks":98},{"name":"1fZDIHLe","marks":61},{"name":"autFMX","marks":82},{"name":"5xWB","marks":38},{"name":"SnsgmIHka","marks":36},{"name":"aui5j","marks":84},{"name":"0oA5iiSK","marks":32},{"name":"CObJOOP8","marks":39},{"name":"Xmio5w1J4","marks":98},{"name":"JaH","marks":70},{"name":"z","marks":97},{"name":"Av2uwyy","marks":33},{"name":"oypKh","marks":62},{"name":"eEsNC0","marks":26},{"name":"pA4vBnE3MA","marks":91},{"name":"DNaGo","marks":21},{"name":"7K","marks":51},{"name":"kCTBjw","marks":8},{"name":"ELB2zoq","marks":87},{"name":"OVPfu7k8","marks":46},{"name":"UHLMuZ","marks":76},{"name":"vKrP","marks":39},{"name":"eTK","marks":36},{"name":"TM","marks":16},{"name":"P5","marks":7},{"name":"Y","marks":24},{"name":"Dwy084","marks":37},{"name":"6AX","marks":76},{"name":"kzDpUvNVwW","marks":55},{"name":"IyRUenO","marks":92},{"name":"FaiDFZUFs0","marks":23},{"name":"t","marks":84},{"name":"tFCqUf","marks":28},{"name":"e1LFHc9mTk","marks":51},{"name":"536","marks":45},{"name":"G26inQPAI","marks":91},{"name":"9eX","marks":97},{"name":"UBPh7D","marks":82},{"name":"hUlHN6R8","marks":57},{"name":"txIQlbpJG","marks":7},{"name":"2Ld1rZN","marks":29},{"name":"MjdSYYJ","marks":56},{"name":"u","marks":87},{"name":"uR8c","marks":17},{"name":"lfLzHg","marks":14},{"name":"3jo","marks":91},{"name":"RlToSl8Lat","marks":29},{"name":"jz","marks":92},{"name":"q","marks":79},{"name":"gJmGC","marks":83},{"name":"RFUCfS2m","marks":89},{"name":"AUV","marks":60},{"name":"4JlLLGV","marks":8},{"name":"c7ABJFTwiP","marks":85},{"name":"LgYh0SZz","marks":91},{"name":"L","marks":54},{"name":"8","marks":64},{"name":"P","marks":16},{"name":"6zt4qVGnh","marks":24},{"name":"Uk","marks":46},{"name":"Xy","marks":29},{"name":"0","marks":61},{"name":"UkH","marks":60}]

class MarksRequest(BaseModel):
    names: List[str]

@app.get("/api")
async def get_marks(names: str = None):
    if names:
        names_list = names.split(',')
        marks = [item['marks'] for item in marks_data if item['name'] in names_list]
        return {"marks": marks}
    else:
        return {"error": "No names provided"}
