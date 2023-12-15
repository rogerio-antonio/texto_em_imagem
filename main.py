from PIL import Image, ImageDraw, ImageFont

# Texto que será colocado
palavras = ['João', 'Paulo', 'Marcelo']

contador = 1
for palavra in palavras:
    # Abrir a imagem original
    imagem_original = Image.open('step.png')
    
    # Criar uma cópia da imagem original para sobrepor
    imagem = imagem_original.copy()
    
    # Criar objeto de desenho para a cópia
    draw = ImageDraw.Draw(imagem)
    
    # Configurar a fonte
    fonte = ImageFont.truetype('Sarai.ttf', 30)
    
    # Sobrepor texto na imagem
    draw.text((80, 104), palavra, font=fonte)
    
    # Salvar imagem modificada
    imagem.save(f'{palavra}.png')
    #imagem.save(f'imagem{contador}.png')
    contador += 1