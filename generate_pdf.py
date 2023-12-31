import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader


def create_pdf(image_folder_path, output_filename):

    canvas_dimensions = A4
    canvas_heigth = canvas_dimensions[1]
    canvas_width = canvas_dimensions[0]
    c = canvas.Canvas(output_filename, pagesize=canvas_dimensions)
    margin = 0.5 * inch
    space_between_images = 0.8 * inch

    workspace_width = canvas_width - 2 * margin

    each_image_space = (workspace_width - 4 * space_between_images) / 5

    image_files_list = [f for f in os.listdir(image_folder_path)
                   if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for index, image_file_name in enumerate(image_files_list):
        image_height = each_image_space
        image_width = each_image_space

        if index % 5 == 0:
            x_position = margin
            y_position = canvas_dimensions[1] - margin - image_height
        else:
            x_position += image_width + space_between_images
            y_position = canvas_dimensions[1] - margin - image_height

        img_path = os.path.join(image_folder_path, image_file_name)
        img = ImageReader(img_path)

        # c.drawImage(img, x_position, y_position, width=image_width, preserveAspectRatio=True)
        c.drawImage(img, x_position, y_position, width=image_width, height=image_height, preserveAspectRatio=True, anchor='n')

        text_x_position = x_position
        text_y_position = y_position - 0.2 * inch

        c.drawString(text_x_position, text_y_position, f'{image_file_name}')
    c.save()


create_pdf(image_folder_path='./ft', output_filename='teste_451.pdf')
