import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from PIL import Image, ImageOps
# from ironpdf import *


def get_image_files_list(image_folder_path):
    return [f for f in os.listdir(image_folder_path)
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]


def break_page(wh, ih, sbi, ds):
    if wh - (ih + sbi + ds) <= 0:
        return True
    return False


def create_pdf(image_folder_path, output_filename):
    canvas_dimensions = A4
    font_size = 8
    margin = 0.1 * inch
    space_between_images = 0.25 * inch
    images_per_line = 4
    space_between_lines = 0.2 * inch
    quality = 50
    description_space = 0.1 * inch

    canvas_heigth = canvas_dimensions[1]
    canvas_width = canvas_dimensions[0]
    workspace_width = canvas_width - 2 * margin
    workspace_height = canvas_heigth - 2 * margin
    each_image_space = (workspace_width - (images_per_line - 1) * space_between_images) / images_per_line
    image_height = each_image_space
    image_width = each_image_space
    y_position = canvas_dimensions[1] - margin - image_height
    x_position = margin

    c = canvas.Canvas(output_filename, pagesize=canvas_dimensions)
    c.setTitle("amostras")
    c.setFont("Helvetica", font_size)

    image_files_list = get_image_files_list(image_folder_path)

    for index, image_file_name in enumerate(image_files_list):
        if index == 0:
            y_position = canvas_dimensions[1] - margin - image_height
        else:
            if index % images_per_line == 0:
                y_position -= image_height + space_between_lines
                x_position = margin
                if y_position < 0 or workspace_height - (y_position + image_height + space_between_images) <= 0:
                    c.showPage()
                    c.setFont("Helvetica", font_size)
                    y_position = canvas_dimensions[1] - margin - image_height
            else:
                x_position += image_width + space_between_images

        img_path = os.path.join(image_folder_path, image_file_name)
        original_image = Image.open(img_path)
        original_image = ImageOps.exif_transpose(original_image)

        original_image.save('./compressed.jpg', quality=quality, )
        img = ImageReader('./compressed.jpg')
        c.drawImage(img, x_position, y_position, width=image_width, height=image_height, preserveAspectRatio=True,
                    anchor='c')

        image_caption = f'{image_file_name}'
        image_caption_width = c.stringWidth(image_caption)
        text_x_position = x_position + ((image_width - image_caption_width) / 2)
        text_y_position = y_position - description_space
        c.drawString(text_x_position, text_y_position, image_caption)
        print(f'OK: {image_file_name}')

    c.save()

#
# def compress_pdf():
#     pdf = PdfDocument("normal.pdf")
#     pdf.CompressImages(50)
#     pdf.SaveAs("normal.pdf")

create_pdf(
    image_folder_path='edit',
    output_filename='edit.pdf'
)

# ou diminuir a qualidade do pdf
# criar tmp e deletar
# reescrever codigo mais estruturado com POO
# mostrar porcentagem gerada no pdf
# mostrar porcentagem de compressao
# botar em thread para ser mais rapido
