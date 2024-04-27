from paddleocr import PaddleOCR


def solve():
    finaltext = ''
    ocr = PaddleOCR(lang='en', use_angle_cls=True)
    img = 'image.png'
    result = ocr.ocr(img)
    for i in range(len(result[0])):
        text = result[0][i][1][0]
        finaltext += ' ' + text
    capcha = finaltext.replace(' ', '')
    print(capcha)
    return capcha
