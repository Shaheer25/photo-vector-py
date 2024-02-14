import cv2
import io
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

router = FastAPI()


@router.post("/api/v1/photo")
async def convert_photo_to_vector(file: UploadFile = File(...)):
    if not file:
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"api_status": False, "data": None, "message": "Upload a file"},
        )
    else:
        try:
            file_content = await file.read()
            file_path = f"{file.filename}"
            with open(file_path, "wb") as f:
                f.write(file_content)
            final_image_content, status = await image_converter(file_path)
            return JSONResponse(
                status_code=200, content={"status": True, "data": final_image_content}
            )
        except Exception as e:
            return JSONResponse(
                status_code=500,
                content={"api_status": False, "data": None, "message": str(e)},
            )


async def image_converter(path):

    image = cv2.imread(path)

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    inverted = 255 - gray_image

    blur = cv2.GaussianBlur(inverted, (21, 21), 0)

    inverted_blur = 255 - blur

    sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

    status = cv2.imwrite("sketch_image.png", sketch)

    final_image = cv2.imshow("Image", sketch)

    return final_image, status
