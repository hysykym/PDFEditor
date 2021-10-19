import PyPDF2
import sys
import os

def check_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)

def rotatePDF(path, save_folder, rotate_angle):
    for filename in os.listdir(path):
        pdf_path = f'{path}/{filename}'
        save_path = f'{save_folder}/{filename}'
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            writer = PyPDF2.PdfFileWriter()
            for i in range(reader.numPages):
                page = reader.getPage(i)
                page.rotateClockwise(rotate_angle)
                writer.addPage(page)
                with open(save_path, 'wb') as file2:
                    writer.write(file2)

def pdf_combiner(pdf_folder, save_folder):
    save_path = f'{save_folder}/merge.pdf'
    merger = PyPDF2.PdfFileMerger()
    for filename in os.listdir(pdf_folder):
        pdf_path = f'{pdf_folder}/{filename}'
        merger.append(pdf_path)
    merger.write(save_path)

def watermarker(pdf_folder, wtr_path, save_folder):
    for filename in os.listdir(pdf_folder):
        pdf_path = f'{pdf_folder}/{filename}'
        save_path = f'{save_folder}/{filename.split()[0]}_w.pdf'

        template = PyPDF2.PdfFileReader(open(pdf_path, 'rb'))
        watermarker_pdf = PyPDF2.PdfFileReader(open(wtr_path, 'rb'))
        writer = PyPDF2.PdfFileWriter()

        for i in range(template.getNumPages()):
            page = template.getPage(i)
            page.mergePage(watermarker_pdf.getPage(0))
            writer.addPage(page)

            with open(save_path, 'wb') as file:
                writer.write(file)

if __name__ == '__main__':
    print('-----start-----')

    # inputs = sys.argv[1:]

    pdf_folder = './pdf'
    save_folder = './new'

    check_folder(pdf_folder)
    check_folder(save_folder)

    rotatePDF(pdf_folder, save_folder, 90)

    pdf_combiner(pdf_folder, save_folder)

    watermarker(pdf_folder, 'wtr.pdf', save_folder)


