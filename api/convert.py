from fastapi import FastAPI, File, UploadFile, Form
from fastapi.responses import StreamingResponse, JSONResponse
from converter.pdf_to_docx import convert_pdf_to_docx
from utils.file_ops import stem_with_hash
import io, zipfile

app = FastAPI()

@app.post("/api/convert")
async def convert(files: list[UploadFile] = File(...), strategy: str = Form("auto")):
    results = []
    for f in files:
        pdf_bytes = await f.read()
        try:
            docx_bytes = convert_pdf_to_docx(pdf_bytes, strategy=strategy)
            out_name = stem_with_hash(f.filename, pdf_bytes, ".docx")
            results.append((out_name, docx_bytes))
        except Exception as e:
            return JSONResponse({"error": f"Failed {f.filename}: {e}"}, status_code=400)

    if len(results) == 1:
        name, payload = results[0]
        return StreamingResponse(
            io.BytesIO(payload),
            media_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            headers={"Content-Disposition": f"attachment; filename={name}"}
        )
    else:
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as zf:
            for name, payload in results:
                zf.writestr(name, payload)
        buf.seek(0)
        return StreamingResponse(
            buf,
            media_type="application/zip",
            headers={"Content-Disposition": "attachment; filename=converted.zip"}
        )
