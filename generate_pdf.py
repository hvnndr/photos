import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from PIL import Image


def get_image_files_list(image_folder_path):
    return [f for f in os.listdir(image_folder_path)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]


def create_pdf(image_folder_path, output_filename):
    canvas_dimensions = A4
    canvas_heigth = canvas_dimensions[1]
    canvas_width = canvas_dimensions[0]
    font_size = 8
    margin = 0.2 * inch
    space_between_images = 0.2 * inch
    workspace_width = canvas_width - 2 * margin
    each_image_space = (workspace_width - 4 * space_between_images) / 5
    image_height = each_image_space
    image_width = each_image_space
    x_position = margin
    y_position = canvas_dimensions[1] - margin - image_height
    space_between_lines = 0.5 * inch


    c = canvas.Canvas(output_filename, pagesize=canvas_dimensions)
    c.setTitle("amostras")
    c.setFont("Helvetica", font_size)

    image_files_list = get_image_files_list(image_folder_path)

    for index, image_file_name in enumerate(image_files_list):
        if index == 0:
            y_position = canvas_dimensions[1] - margin - image_height
        else:
            if index % 5 == 0:
                y_position -= image_height + space_between_lines
                x_position = margin
            else:
                x_position += image_width + space_between_images

        img_path = os.path.join(image_folder_path, image_file_name)
        original_image = Image.open(img_path)
        original_image.save('./compressed.jpg', quality=5)
        img = ImageReader('./compressed.jpg')
        c.drawImage(img, x_position, y_position, width=image_width, height=image_height, preserveAspectRatio=True, anchor='s')

        image_caption = f'{image_file_name}'
        image_caption_width = c.stringWidth(image_caption)
        text_x_position = x_position + ((image_width - image_caption_width) / 2)
        text_y_position = y_position - 0.2 * inch
        c.drawString(text_x_position, text_y_position, image_caption)
        print(f'OK: {image_file_name}')

    c.save()


create_pdf(
    image_folder_path='fotos',
    output_filename='uncompressed.pdf'
)



# determinar quantas fotos por linha
# diminuir a qualidade da imagem
# ou diminuir a qualidade do pdf
#criar tmp e deletar
