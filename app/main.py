from fastapi import FastAPI, Depends
from app.config import get_settings, Settings
from app.api import read, write
from opentelemetry import trace
from opentelemetry.exporter import jaeger
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

app = FastAPI()

app.include_router(read.router)
app.include_router(write.router)

@app.get("/")
async def root(settings: Settings = Depends(get_settings)):
    return {
        "message": "Hello World",
        "environment": settings.environment
    }

resource = Resource(attributes={"service.name": "fastapi-otel"})
trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)
otlp_exporter = OTLPSpanExporter(endpoint="otel-collector:4317", insecure=True)
span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)
FastAPIInstrumentor.instrument_app(app)