from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder
from app.db.database import write_db
from app.models.data import ResponseModel, DataSchema
from time import sleep
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

router = APIRouter()

resource = Resource(attributes={"service.name": "fastapi-otel-api"})
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)
otlp_exporter = OTLPSpanExporter(endpoint="otel-collector:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)

@router.post("/write")
async def add_data(data: DataSchema = Body(...)):
    data = jsonable_encoder(data)
    new_data = write_db(data)
    f1()
    f2()
    return ResponseModel(new_data, f"Data successfully added")

@tracer.start_as_current_span("f1")
def f1():
    sleep(1)
    with tracer.start_as_current_span('f1_child_span') as f1_child_span:
        dojos = 'dojo_otel_hehe'
        for dojo in dojos:
            print(dojo)
        sleep(1)

@tracer.start_as_current_span("f2")
def f2():
    sleep(1)
    return '2 detik'