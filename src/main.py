from fastapi import FastAPI, HTTPException
from factories.ingestor_factory import IngestorFactory

app = FastAPI(title="mirror-core", version="0.1.0", description="An API for data classification.")

def print_pdf_content(filepath):
    try:
        ingestor = IngestorFactory.create_ingestor(filepath)
        data = ingestor.ingest()  
        print(data)
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    pdf_name = "foo.pdf"
    pdf_filepath = "/Users/johnchildseddy/Desktop/opensource/mirror-core/tests/test_files/" + pdf_name
    print_pdf_content(pdf_filepath)

@app.get("/")
async def read_root():
    return {"message": "Welcome to the mirror-core API!"}


# To run the server with uvicorn go to root and run: 'uvicorn src.main:app --reload'
