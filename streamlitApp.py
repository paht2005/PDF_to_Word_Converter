import io, zipfile
import streamlit as st
from converter.pdf_to_docx import convert_pdf_to_docx
from utils.file_ops import stem_with_hash, safe_basename, timestamp

st.set_page_config(page_title="PDF → Word Converter", layout="centered")

st.title(" PDF → Word Converter")
st.caption("Upload PDF(s) and download as editable Word (DOCX).")

# --- Settings ---
with st.sidebar:
    st.header(" Settings")
    strategy = st.selectbox(
        "Conversion strategy",
        ["auto", "precise", "text"],
        help=(
            "auto: try layout-precise first, fallback to text\n"
            "precise: pdf2docx only (may fail)\n"
            "text: simple text+images, very robust"
        )
    )
    batch_zip = st.checkbox("Download as .zip if multiple files", value=True)

# --- Upload ---
uploaded_files = st.file_uploader(
    "Upload one or more PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

def convert_one(filename: str, data: bytes):
    """Convert a single PDF to DOCX and return (name, bytes)."""
    out_bytes = convert_pdf_to_docx(data, strategy=strategy)
    out_name = stem_with_hash(filename, data, ".docx")
    return out_name, out_bytes

# --- Processing ---
if uploaded_files:
    results = []
    progress = st.progress(0, text="Converting...")

    for i, uf in enumerate(uploaded_files, 1):
        pdf_bytes = uf.read()
        try:
            name, docx_bytes = convert_one(uf.name, pdf_bytes)
            results.append((name, docx_bytes))
            st.success(f" {name} converted")
        except Exception as e:
            st.error(f" Failed {safe_basename(uf.name)} — {e}")
        progress.progress(i / len(uploaded_files), text=f"Processed {i}/{len(uploaded_files)}")

    if results:
        if len(results) == 1 and not batch_zip:
            name, payload = results[0]
            st.download_button(
                "⬇ Download DOCX",
                data=payload,
                file_name=name,
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
            )
        else:
            buf = io.BytesIO()
            with zipfile.ZipFile(buf, "w") as zf:
                for name, payload in results:
                    zf.writestr(name, payload)
            buf.seek(0)
            st.download_button(
                "⬇ Download all as ZIP",
                data=buf,
                file_name=f"converted-{timestamp()}.zip",
                mime="application/zip"
            )

st.markdown("---")
st.caption("Tip: If 'precise' fails, switch to 'text' mode.")
