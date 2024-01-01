from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch


class PdfGenerator:
    def __init__(
            self,
            canvas_dimensions=A4,
            font_size=8,
            margin=0.2,
            space_between_images=0.2,
            images_per_line=6,
            space_between_lines=0.5,
            quality_compress_image=10,
            description_space=0.2 * inch,
            compress_pdf=True,
            quality_compress_pdf=20


    ):
        self.canvas_dimensions = canvas_dimensions
        self.font_size = font_size
        self.margin = margin * inch
        self.space_between_images = space_between_images * inch
        self.images_per_line = images_per_line
        self.space_between_lines = space_between_lines * inch
        self.quality_compress_image = quality_compress_image
        self.description_space = description_space * inch
        self.compress_pdf = compress_pdf
        self.quality_compress_pdf = quality_compress_pdf

        self.canvas_width = self.canvas_dimensions[0]
        self.canvas_heigth = self.canvas_dimensions[1]
        self.workspace_width = self.canvas_width - 2 * self.margin
        self.workspace_heigth = self.canvas_heigth - 2 * self.margin
        self.image_unit_side_size = (
                self.workspace_width - (self.images_per_line - 1) * self.space_between_images / self.images_per_line
        )
        self.image_width, self.image_height = self.image_unit_side_size

        self.y_position = self.canvas_dimensions[1] - self.margin - self.image_height
        self.x_position = self.margin

    def runner(self):
        # criar pasta tmp

        pass
