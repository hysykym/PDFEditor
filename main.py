import PyPDF2

def rotatePDF(path, save_path, rotate_angle):
    with open(path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        writer = PyPDF2.PdfFileWriter()
        for i in range(reader.numPages):
            page = reader.getPage(i)
            page.rotateClockwise(rotate_angle)
            writer.addPage(page)
            with open(save_path, 'wb') as file2:
                writer.write(file2)

if __name__ == '__main__':
    print('-----start-----')

    rotatePDF('twopage.pdf', 'new.pdf', 90)
