import os
from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles

router = APIRouter()

# Mount static files
static_dir = os.path.join(os.getcwd(),"static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir, exist_ok=True)

@router.get("/pdf/{filename}")
async def get_pdf(filename: str, page: Optional[int] = Query(None, description="Page number to navigate to")):
    """
    Serve PDF file with optional page navigation
    
    Args:
        filename: Name of the PDF file
        page: Page number to navigate to (optional)
    
    Returns:
        PDF file response or redirect with page parameter
    """
    file_path = os.path.join(static_dir, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"File {filename} not found")
    
    if not filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    # If page parameter is provided, return PDF with page navigation
    if page is not None:
        # Return PDF file - most PDF viewers support #page=X parameter
        response = FileResponse(
            file_path,
            media_type="application/pdf",
            headers={
                "Content-Disposition": f"inline; filename={filename}",
                "Cache-Control": "public, max-age=3600"
            }
        )
        # Add page parameter to response headers for client-side navigation
        response.headers["X-PDF-Page"] = str(page)
        return response
    
    # Return PDF file without page specification
    return FileResponse(
        file_path,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"inline; filename={filename}",
            "Cache-Control": "public, max-age=3600"
        }
    )

@router.get("/pdf/{filename}/page/{page_number}")
async def get_pdf_page(filename: str, page_number: int):
    """
    Serve PDF file and navigate to specific page
    
    Args:
        filename: Name of the PDF file
        page_number: Page number to navigate to
    
    Returns:
        PDF file response with page navigation
    """
    file_path = os.path.join(static_dir, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"File {filename} not found")
    
    if not filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    if page_number < 1:
        raise HTTPException(status_code=400, detail="Page number must be greater than 0")
    
    # Return PDF file with page navigation
    response = FileResponse(
        file_path,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"inline; filename={filename}",
            "Cache-Control": "public, max-age=3600",
            "X-PDF-Page": str(page_number)
        }
    )
    return response

@router.get("/pdf/{filename}/info")
async def get_pdf_info(filename: str):
    """
    Get information about PDF file
    
    Args:
        filename: Name of the PDF file
    
    Returns:
        PDF file information
    """
    file_path = os.path.join(static_dir, filename)
    
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail=f"File {filename} not found")
    
    if not filename.lower().endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported")
    
    try:
        import PyPDF2
        with open(file_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            num_pages = len(pdf_reader.pages)
            
            return {
                "filename": filename,
                "total_pages": num_pages,
                "file_size": os.path.getsize(file_path),
                "available_pages": list(range(1, num_pages + 1))
            }
    except ImportError:
        # Fallback if PyPDF2 is not available
        return {
            "filename": filename,
            "file_size": os.path.getsize(file_path),
            "note": "PyPDF2 not available for detailed page information"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading PDF: {str(e)}")
