import customtkinter 
import customtkinter as ctk
from random import shuffle
import messagebox
from PIL import Image
import os
import platform
import shutil
import posixpath
from pathlib import Path

# Configurações gerais
MAX_TENTATIVAS = 25
NUM_LINHAS = 4
NUM_COLUNAS = 4
CARTAO_SIZE_H = 115
CARTAO_SIZE_W = 115

if platform.system() == "Linux":
    if not os.path.exists(os.path.join(f"{posixpath.expanduser("~")}", ".MemoriaDeElefante")): 
        shutil.copytree("img",f"{os.path.join(f"{posixpath.expanduser("~")}", ".MemoriaDeElefante" ,"img")}")
        print(f"{os.path.join(f"{posixpath.expanduser("~")}", ".MemoriaDeElefante")}")
    else:
        print("A pasta já existe.")
# ============================================================================
# CONFIGURAÇÃO PARA A ABA 'CORES'
# ============================================================================
cor1 = '#dd00ff'
cor2 = '#0080ff'
cor3 = '#00ffff'
cor4 = '#fc6500'
cor5 = '#ffe4c4'
cor6 = '#3cff00'
cor7 = '#ffff00'
cor8 = '#613200'

CARTAO_COLORS = [cor1, cor2, cor3, cor4, cor5, cor6, cor7, cor8]

# ============================================================================
# CONFIGURAÇÃO PARA A ABA 'animais' 
# ============================================================================

# Cores para referência das imagens
img_cor1 = '#dd00ff'
img_cor2 = '#0080ff'
img_cor3 = '#00ffff'
img_cor4 = '#fc6500'
img_cor5 = '#ffe4c4'
img_cor6 = '#3cff00'
img_cor7 = '#ffff00'
img_cor8 = '#ee82dd'

ANIMAIS_COLORS = [img_cor1, img_cor2, img_cor3, img_cor4, img_cor5, img_cor6, img_cor7, img_cor8]

# ============================================================================
# CONFIGURAÇÃO PARA A ABA 'flores' 
# ============================================================================
# Cores para referência das imagens
img_cor1_flor = '#dd00ff'
img_cor2_flor = '#0080ff'
img_cor3_flor = '#00ffff'
img_cor4_flor = '#fc6500'
img_cor5_flor = '#ffe4c4'
img_cor6_flor = '#3cff00'
img_cor7_flor = '#ffff00'
img_cor8_flor = '#ee82dd'

FLORES_COLORS = [img_cor1_flor, img_cor2_flor, img_cor3_flor, img_cor4_flor, img_cor5_flor, img_cor6_flor, img_cor7_flor, img_cor8_flor]


# ============================================================================
# CONFIGURAÇÃO PARA A ABA 'carros' 
# ============================================================================
# Cores para referência das imagens
img_cor1_carros = '#dd00ff'
img_cor2_carros = '#0080ff'
img_cor3_carros = '#00ffff'
img_cor4_carros = '#fc6500'
img_cor5_carros = '#ffe4c4'
img_cor6_carros = '#3cff00'
img_cor7_carros = '#ffff00'
img_cor8_carros = '#ee82dd'

CARROS_COLORS = [img_cor1_carros, img_cor2_carros, img_cor3_carros, img_cor4_carros, img_cor5_carros, img_cor6_carros, img_cor7_carros, img_cor8_carros]

# ============================================================================
# CONFIGURAÇÃO PARA A ABA 'bandeiras' 
# ============================================================================
# Cores para referência das imagens
img_cor1_bandeiras = '#dd00ff'
img_cor2_bandeiras = '#0080ff'
img_cor3_bandeiras = '#00ffff'
img_cor4_bandeiras = '#fc6500'
img_cor5_bandeiras = '#ffe4c4'
img_cor6_bandeiras = '#3cff00'
img_cor7_bandeiras = '#ffff00'
img_cor8_bandeiras = '#ee82dd'

BANDEIRAS_COLORS = [img_cor1_bandeiras, img_cor2_bandeiras, img_cor3_bandeiras, img_cor4_bandeiras, img_cor5_bandeiras, img_cor6_bandeiras, img_cor7_bandeiras, img_cor8_bandeiras]
# Tentar carregar as imagens ou usar cores de fallback
try:
    img1 = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","animais","img1.jpg")),
                                   dark_image=Image.open(os.path.join("img","animais","img1.jpg")),
                                   size=(100, 100))
except:
    img1 = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img1.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img1.jpg")),
                                   size=(100, 100))
    
try:
    img2 = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","animais","img2.jpg")),
                                   dark_image=Image.open(os.path.join("img","animais","img2.jpg")),
                                   size=(100, 100))
except:
    img2 = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img2.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img2.jpg")),
                                   size=(100, 100))
    
try:
    img3 = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","animais","img3.jpg")),
                                   dark_image=Image.open(os.path.join("img","animais","img3.jpg")),
                                   size=(100, 100))
except:
    img3 = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img3.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img3.jpg")),
                                   size=(100, 100))
    
try:
    img4 = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","animais","img4.jpg")),
                                   dark_image=Image.open(os.path.join("img","animais","img4.jpg")),
                                   size=(100, 100))
except:
    img4 = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img4.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img4.jpg")),
                                   size=(100, 100))
    
try:
    img5 = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","animais","img5.jpg")),
                                   dark_image=Image.open(os.path.join("img","animais","img5.jpg")),
                                   size=(100, 100))
except:
    img5 = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img5.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img5.jpg")),
                                   size=(100, 100))
    
try:
    img6 = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","animais","img6.jpg")),
                                   dark_image=Image.open(os.path.join("img","animais","img6.jpg")),
                                   size=(100, 100))
except:
    img6 = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img6.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img6.jpg")),
                                   size=(100, 100))
    
try:
    img7 = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","animais","img7.jpg")),
                                   dark_image=Image.open(os.path.join("img","animais","img7.jpg")),
                                   size=(100, 100))
except:
    img7 = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img7.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img7.jpg")),
                                   size=(100, 100))
    
try:
    img8 = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","animais","img8.jpg")),
                                   dark_image=Image.open(os.path.join("img","animais","img8.jpg")),
                                   size=(100, 100))
except:
    img8 = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img8.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","animais","img8.jpg")),
                                   size=(100, 100))
    
##############################
#     IMAGENS PARA AS FLORES
##############################

# Tentar carregar as imagens ou usar cores de fallback
try:
    img1_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","flores","img1.jpg")),
                                   dark_image=Image.open(os.path.join("img","flores","img1.jpg")),
                                   size=(100, 100))
except:
    img1_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img1.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img1.jpg")),
                                   size=(100, 100))
    
try:
    img2_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","flores","img2.jpg")),
                                   dark_image=Image.open(os.path.join("img","flores","img2.jpg")),
                                   size=(100, 100))
except:
    img2_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img2.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img2.jpg")),
                                   size=(100, 100))
    
try:
    img3_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","flores","img3.jpg")),
                                   dark_image=Image.open(os.path.join("img","flores","img3.jpg")),
                                   size=(100, 100))
except:
    img3_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img3.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img3.jpg")),
                                   size=(100, 100))
    
try:
    img4_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","flores","img4.jpg")),
                                   dark_image=Image.open(os.path.join("img","flores","img4.jpg")),
                                   size=(100, 100))
except:
    img4_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img4.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img4.jpg")),
                                   size=(100, 100))
    
try:
    img5_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","flores","img5.jpg")),
                                   dark_image=Image.open(os.path.join("img","flores","img5.jpg")),
                                   size=(100, 100))
except:
    img5_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img5.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img5.jpg")),
                                   size=(100, 100))
    
try:
    img6_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","flores","img6.jpg")),
                                   dark_image=Image.open(os.path.join("img","flores","img6.jpg")),
                                   size=(100, 100))
except:
    img6_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img6.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img6.jpg")),
                                   size=(100, 100))
    
try:
    img7_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","flores","img7.jpg")),
                                   dark_image=Image.open(os.path.join("img","flores","img7.jpg")),
                                   size=(100, 100))
except:
    img7_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img7.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img7.jpg")),
                                   size=(100, 100))
    
try:
    img8_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","flores","img8.jpg")),
                                   dark_image=Image.open(os.path.join("img","flores","img8.jpg")),
                                   size=(100, 100))
except:
    img8_flores = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img8.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","flores","img8.jpg")),
                                   size=(100, 100))
    
##############################
#     IMAGENS PARA OS CARROS
##############################

try:
    img1_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","carros","img1.jpg")),
                                   dark_image=Image.open(os.path.join("img","carros","img1.jpg")),
                                   size=(100, 100))
except:
    img1_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img1.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img1.jpg")),
                                   size=(100, 100))
    
try:
    img2_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","carros","img2.jpg")),
                                   dark_image=Image.open(os.path.join("img","carros","img2.jpg")),
                                   size=(100, 100))
except:
    img2_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img2.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img2.jpg")),
                                   size=(100, 100))
    
try:
    img3_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","carros","img3.jpg")),
                                   dark_image=Image.open(os.path.join("img","carros","img3.jpg")),
                                   size=(100, 100))
except:
    img3_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img3.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img3.jpg")),
                                   size=(100, 100))
    
try:
    img4_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","carros","img4.jpg")),
                                   dark_image=Image.open(os.path.join("img","carros","img4.jpg")),
                                   size=(100, 100))
except:
    img4_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img4.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img4.jpg")),
                                   size=(100, 100))
    
try:
    img5_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","carros","img5.jpg")),
                                   dark_image=Image.open(os.path.join("img","carros","img5.jpg")),
                                   size=(100, 100))
except:
    img5_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img5.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img5.jpg")),
                                   size=(100, 100))
    
try:
    img6_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","carros","img6.jpg")),
                                   dark_image=Image.open(os.path.join("img","carros","img6.jpg")),
                                   size=(100, 100))
except:
    img6_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img6.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img6.jpg")),
                                   size=(100, 100))
    
try:
    img7_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","carros","img7.jpg")),
                                   dark_image=Image.open(os.path.join("img","carros","img7.jpg")),
                                   size=(100, 100))
except:
    img7_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img7.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img7.jpg")),
                                   size=(100, 100))
    
try:
    img8_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","carros","img8.jpg")),
                                   dark_image=Image.open(os.path.join("img","carros","img8.jpg")),
                                   size=(100, 100))
except:
    img8_carros = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img8.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","carros","img8.jpg")),
                                   size=(100, 100))
    
##############################
#     IMAGENS PARA AS BANDEIRAS
##############################

try:
    img1_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","bandeiras","img1.jpg")),
                                   dark_image=Image.open(os.path.join("img","bandeiras","img1.jpg")),
                                   size=(100, 100))
except:
    img1_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img1.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img1.jpg")),
                                   size=(100, 100))
    
try:
    img2_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","bandeiras","img2.jpg")),
                                   dark_image=Image.open(os.path.join("img","bandeiras","img2.jpg")),
                                   size=(100, 100))
except:
    img2_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img2.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img2.jpg")),
                                   size=(100, 100))
    
try:
    img3_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","bandeiras","img3.jpg")),
                                   dark_image=Image.open(os.path.join("img","bandeiras","img3.jpg")),
                                   size=(100, 100))
except:
    img3_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img3.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img3.jpg")),
                                   size=(100, 100))
    
try:
    img4_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","bandeiras","img4.jpg")),
                                   dark_image=Image.open(os.path.join("img","bandeiras","img4.jpg")),
                                   size=(100, 100))
except:
    img4_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img4.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img4.jpg")),
                                   size=(100, 100))
    
try:
    img5_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","bandeiras","img5.jpg")),
                                   dark_image=Image.open(os.path.join("img","bandeiras","img5.jpg")),
                                   size=(100, 100))
except:
    img5_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img5.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img5.jpg")),
                                   size=(100, 100))
    
try:
    img6_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","bandeiras","img6.jpg")),
                                   dark_image=Image.open(os.path.join("img","bandeiras","img6.jpg")),
                                   size=(100, 100))
except:
    img6_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img6.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img6.jpg")),
                                   size=(100, 100))
    
try:
    img7_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","bandeiras","img7.jpg")),
                                   dark_image=Image.open(os.path.join("img","bandeiras","img7.jpg")),
                                   size=(100, 100))
except:
    img7_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img7.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img7.jpg")),
                                   size=(100, 100))
    
try:
    img8_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join("img","bandeiras","img8.jpg")),
                                   dark_image=Image.open(os.path.join("img","bandeiras","img8.jpg")),
                                   size=(100, 100))
except:
    img8_bandeiras = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img8.jpg")),
                                   dark_image=Image.open(os.path.join(Path.home(),".MemoriaDeElefante","img","bandeiras","img8.jpg")),
                                   size=(100, 100))
##############################
#    IMAGENS PARA AS FLORES FIM
###############################
# Imagem preta para o verso
try:
    black_image = customtkinter.CTkImage(light_image=Image.open('./img/black.png'),
                                         dark_image=Image.open('./img/black.png'),
                                         size=(100, 100))
except:
    # Criar uma imagem preta simples se não existir
    from PIL import Image, ImageDraw
    img = Image.new('RGB', (100, 100), color='black')
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, 90, 90], outline='white', width=3)
    black_image = customtkinter.CTkImage(light_image=img, dark_image=img, size=(100, 100))

# Mapeamento de cores para imagens
CARTAO_IMG = {
    img_cor1: img1 if img1 else black_image,
    img_cor2: img2 if img2 else black_image,
    img_cor3: img3 if img3 else black_image,
    img_cor4: img4 if img4 else black_image,
    img_cor5: img5 if img5 else black_image,
    img_cor6: img6 if img6 else black_image,
    img_cor7: img7 if img7 else black_image,
    img_cor8: img8 if img8 else black_image
}
CARTAO_IMG_FLORES = {
    img_cor1: img1_flores if img1_flores else black_image,
    img_cor2: img2_flores if img2_flores else black_image,
    img_cor3: img3_flores if img3_flores else black_image,
    img_cor4: img4_flores if img4_flores else black_image,
    img_cor5: img5_flores if img5_flores else black_image,
    img_cor6: img6_flores if img6_flores else black_image,
    img_cor7: img7_flores if img7_flores else black_image,
    img_cor8: img8_flores if img8_flores else black_image
}
CARTAO_IMG_CARROS = {
    img_cor1: img1_carros if img1_carros else black_image,
    img_cor2: img2_carros if img2_carros else black_image,
    img_cor3: img3_carros if img3_carros else black_image,
    img_cor4: img4_carros if img4_carros else black_image,
    img_cor5: img5_carros if img5_carros else black_image,
    img_cor6: img6_carros if img6_carros else black_image,
    img_cor7: img7_carros if img7_carros else black_image,
    img_cor8: img8_carros if img8_carros else black_image
}
CARTAO_IMG_BANDEIRAS = {
    img_cor1: img1_bandeiras if img1_bandeiras else black_image,
    img_cor2: img2_bandeiras if img2_bandeiras else black_image,
    img_cor3: img3_bandeiras if img3_bandeiras else black_image,
    img_cor4: img4_bandeiras if img4_bandeiras else black_image,
    img_cor5: img5_bandeiras if img5_bandeiras else black_image,
    img_cor6: img6_bandeiras if img6_bandeiras else black_image,
    img_cor7: img7_bandeiras if img7_bandeiras else black_image,
    img_cor8: img8_bandeiras if img8_bandeiras else black_image
}
# ============================================================================
# FUNÇÕES GENÉRICAS
# ============================================================================
def creat_card_grid(cores):
    """Cria um grid de cartões com as cores fornecidas"""
    cores_lista = cores * 2
    shuffle(cores_lista)
    grid = []
    for _ in range(NUM_LINHAS):
        linha = []
        for _ in range(NUM_COLUNAS):
            cor = cores_lista.pop()
            linha.append(cor)
        grid.append(linha)
    return grid

def eliminar_cartao(cartao):
    """Função para eliminar/remover o cartão do tabuleiro"""
    # Criar um efeito visual antes de eliminar
    cartao.configure(fg_color='green', text='✓', text_color='white', 
                    font=('Arial', 40, 'bold'), image=None)
    
    # Após um breve delay, remover completamente o cartão
    cartao.after(300, lambda: cartao.grid_forget() if cartao.winfo_exists() else None)

# ============================================================================
# FUNÇÕES PARA A ABA 'CORES'
# ============================================================================
def reiniciar_jogo_cores():
    global grid_cores, cartoes_cores, cartao_revelado_cores, cartao_correspondente_cores
    global tentativas_cores, cartao_bloqueado_cores, pares_encontrados_cores
    
    # Limpar cartões antigos
    for linha in cartoes_cores:
        for cartao in linha:
            if cartao.winfo_exists():
                cartao.destroy()
    
    # Reiniciar variáveis
    grid_cores = creat_card_grid(CARTAO_COLORS)
    cartoes_cores = []
    cartao_revelado_cores = []
    cartao_correspondente_cores = []
    pares_encontrados_cores = 0
    tentativas_cores = 0
    cartao_bloqueado_cores = False
    
    # Criar novos cartões
    for linha in range(NUM_LINHAS):
        linha_de_cartao = []
        for col in range(NUM_COLUNAS):
            cartao = customtkinter.CTkButton(
                tabview.tab('cores'),
                command=lambda r=linha, c=col: click_cores(r, c),
                text='',
                width=CARTAO_SIZE_W,
                height=CARTAO_SIZE_H,
                fg_color='black',
                bg_color='black',
                hover=False,
                border_color='gray'
            )
            cartao.grid(row=linha, column=col, padx=5, pady=5)
            linha_de_cartao.append(cartao)
        cartoes_cores.append(linha_de_cartao)
    
    label_tentativas_cores.configure(text=f'Tentativas: {tentativas_cores}/{MAX_TENTATIVAS} | Pares: {pares_encontrados_cores}/8')

def click_cores(linha, coluna):
    global cartao_bloqueado_cores, tentativas_cores, pares_encontrados_cores
    
    if cartao_bloqueado_cores:
        return
    
    cartao = cartoes_cores[linha][coluna]
    
    # Se o cartão já foi revelado ou já foi eliminado, não faz nada
    if not cartao.winfo_ismapped():  # Cartão já foi eliminado
        return
    
    cor_atual = cartao.cget('fg_color')
    
    # Se o cartão já está revelado, não faz nada
    if cor_atual != 'black':
        return
    
    # Revelar o cartão (mostrar a cor)
    cartao.configure(fg_color=grid_cores[linha][coluna], 
                    bg_color=grid_cores[linha][coluna])
    cartao_revelado_cores.append((cartao, linha, coluna))
    
    # Se temos 2 cartões revelados, verificar se são iguais
    if len(cartao_revelado_cores) == 2:
        cartao_bloqueado_cores = True
        tentativas_cores += 1
        label_tentativas_cores.configure(text=f'Tentativas: {tentativas_cores}/{MAX_TENTATIVAS} | Pares: {pares_encontrados_cores}/8')
        
        cartao1, linha1, coluna1 = cartao_revelado_cores[0]
        cartao2, linha2, coluna2 = cartao_revelado_cores[1]
        
        cor1 = grid_cores[linha1][coluna1]
        cor2 = grid_cores[linha2][coluna2]
        
        if cor1 == cor2:
            # Cartões iguais - ELIMINAR ambos após um breve delay
            pares_encontrados_cores += 1
            
            # Eliminar primeiro cartão
            app.after(800, lambda: eliminar_cartao(cartao1) if cartao1.winfo_exists() else None)
            # Eliminar segundo cartão
            app.after(800, lambda: eliminar_cartao(cartao2) if cartao2.winfo_exists() else None)
            
            # Limpar lista de revelados após um delay
            cartao_revelado_cores.clear()
            cartao_bloqueado_cores = False
            
            # Verificar se ganhou
            if pares_encontrados_cores == 8:  # 8 pares no total (16 cartões / 2)
                app.after(1200, lambda: mostrar_mensagem_vitoria_cores())
        else:
            # Cartões diferentes - esconder após 1 segundo
            cartao1.after(1000, lambda: cartao1.configure(fg_color='black', bg_color='black') if cartao1.winfo_exists() else None)
            cartao2.after(1000, lambda: cartao2.configure(fg_color='black', bg_color='black') if cartao2.winfo_exists() else None)
            
            # Limpar lista de revelados e desbloquear após 1 segundo
            app.after(1200, desbloquear_jogo_cores)
            
            # Verificar se perdeu
            if tentativas_cores >= MAX_TENTATIVAS:
                app.after(1300, lambda: mostrar_mensagem_derrota_cores())

def desbloquear_jogo_cores():
    global cartao_bloqueado_cores
    cartao_revelado_cores.clear()
    cartao_bloqueado_cores = False

def mostrar_mensagem_vitoria_cores():
    resposta = messagebox.askyesno("Parabéns!", 
                                  f"Você encontrou todos os 8 pares em {tentativas_cores} tentativas!\nDeseja jogar novamente?")
    if resposta:
        reiniciar_jogo_cores()
    else:
        tabview.set('cores')

def mostrar_mensagem_derrota_cores():
    resposta = messagebox.askyesno("Fim do jogo", 
                                  f"Você usou todas as {MAX_TENTATIVAS} tentativas!\nEncontrou {pares_encontrados_cores} pares.\nDeseja jogar novamente?")
    if resposta:
        reiniciar_jogo_cores()
    else:
        tabview.set('cores')

# ============================================================================
# FUNÇÕES PARA A ABA 'animais'
# ============================================================================
def reiniciar_jogo_animais():
    global grid_animais, cartoes_animais, cartao_revelado_animais, cartao_correspondente_animais
    global tentativas_animais, cartao_bloqueado_animais, pares_encontrados_animais
    
    # Limpar cartões antigos
    for linha in cartoes_animais:
        for cartao in linha:
            if cartao.winfo_exists():
                cartao.destroy()
    
    # Reiniciar variáveis
    grid_animais = creat_card_grid(ANIMAIS_COLORS )
    cartao_revelado_animais = []
    cartao_correspondente_animais = []
    pares_encontrados_animais = 0
    tentativas_animais = 0
    cartao_bloqueado_animais = False
    
    # Criar novos cartões
    for linha in range(NUM_LINHAS):
        linha_de_cartao = []
        for col in range(NUM_COLUNAS):
            cartao = customtkinter.CTkButton(
                tabview.tab('animais'),
                command=lambda r=linha, c=col: click_animais(r, c),
                text='',
                width=CARTAO_SIZE_W,
                height=CARTAO_SIZE_H,
                fg_color='black',
                bg_color='black',
                hover=False,
                image=black_image
            )
            cartao.grid(row=linha, column=col, padx=5, pady=5)
            linha_de_cartao.append(cartao)
        cartoes_animais.append(linha_de_cartao)
    
    label_tentativas_animais.configure(text=f'Tentativas: {tentativas_animais}/{MAX_TENTATIVAS} | Pares: {pares_encontrados_animais}/8')

def click_animais(linha, coluna):
    global cartao_bloqueado_animais, tentativas_animais, pares_encontrados_animais
    
    if cartao_bloqueado_animais:
        return
    
    cartao = cartoes_animais[linha][coluna]
    
    # Se o cartão já foi revelado ou já foi eliminado, não faz nada
    if not cartao.winfo_ismapped():  # Cartão já foi eliminado
        return
    
    cor_atual = cartao.cget('fg_color')
    
    # Se o cartão já está revelado, não faz nada
    if cor_atual != 'black':
        return
    
    # Revelar o cartão (mostrar a imagem)
    cartao.configure(image=CARTAO_IMG[grid_animais[linha][coluna]], 
                    fg_color=grid_animais[linha][coluna], 
                    bg_color=grid_animais[linha][coluna])
    cartao_revelado_animais.append((cartao, linha, coluna))
    
    # Se temos 2 cartões revelados, verificar se são iguais
    if len(cartao_revelado_animais) == 2:
        cartao_bloqueado_animais = True
        tentativas_animais += 1
        label_tentativas_animais.configure(text=f'Tentativas: {tentativas_animais}/{MAX_TENTATIVAS} | Pares: {pares_encontrados_animais}/8')
        
        cartao1, linha1, coluna1 = cartao_revelado_animais[0]
        cartao2, linha2, coluna2 = cartao_revelado_animais[1]
        
        cor1 = grid_animais[linha1][coluna1]
        cor2 = grid_animais[linha2][coluna2]
        
        if cor1 == cor2:
            # Cartões iguais - ELIMINAR ambos após um breve delay
            pares_encontrados_animais += 1
            
            # Eliminar primeiro cartão
            app.after(800, lambda: eliminar_cartao(cartao1) if cartao1.winfo_exists() else None)
            # Eliminar segundo cartão
            app.after(800, lambda: eliminar_cartao(cartao2) if cartao2.winfo_exists() else None)
            
            # Limpar lista de revelados após um delay
            cartao_revelado_animais.clear()
            cartao_bloqueado_animais = False
            
            # Verificar se ganhou
            if pares_encontrados_animais == 8:  # 8 pares no total (16 cartões / 2)
                app.after(1200, lambda: mostrar_mensagem_vitoria_animais())
        else:
            # Cartões diferentes - esconder após 1 segundo
            cartao1.after(1000, lambda: cartao1.configure(image=black_image, fg_color='black', bg_color='black') if cartao1.winfo_exists() else None)
            cartao2.after(1000, lambda: cartao2.configure(image=black_image, fg_color='black', bg_color='black') if cartao2.winfo_exists() else None)
            
            # Limpar lista de revelados e desbloquear após 1 segundo
            app.after(1200, desbloquear_jogo_animais)
            
            # Verificar se perdeu
            if tentativas_animais >= MAX_TENTATIVAS:
                app.after(1300, lambda: mostrar_mensagem_derrota_animais())

def desbloquear_jogo_animais():
    global cartao_bloqueado_animais
    cartao_revelado_animais.clear()
    cartao_bloqueado_animais = False

def mostrar_mensagem_vitoria_animais():
    resposta = messagebox.askyesno("Parabéns!", 
                                  f"Você encontrou todos os 8 pares em {tentativas_animais} tentativas!\nDeseja jogar novamente?")
    if resposta:
        reiniciar_jogo_animais()
    else:
        tabview.set('animais')

def mostrar_mensagem_derrota_animais():
    resposta = messagebox.askyesno("Fim do jogo", 
                                  f"Você usou todas as {MAX_TENTATIVAS} tentativas!\nEncontrou {pares_encontrados_animais} pares.\nDeseja jogar novamente?")
    if resposta:
        reiniciar_jogo_animais()
    else:
        tabview.set('animais')
# ============================================================================
# FUNÇÕES PARA A ABA 'flores'
# ============================================================================
def reiniciar_jogo_flores():
    global grid_flores, cartoes_flores, cartao_revelado_flores, cartao_correspondente_flores
    global tentativas_flores, cartao_bloqueado_flores, pares_encontrados_flores
    
    # Limpar cartões antigos
    for linha in cartoes_flores:
        for cartao in linha:
            if cartao.winfo_exists():
                cartao.destroy()
    
    # Reiniciar variáveis
    grid_flores = creat_card_grid(FLORES_COLORS)
    cartoes_flores = []
    cartao_revelado_flores = []
    cartao_correspondente_flores = []
    pares_encontrados_flores = 0
    tentativas_flores = 0
    cartao_bloqueado_flores = False
    
    # Criar novos cartões
    for linha in range(NUM_LINHAS):
        linha_de_cartao = []
        for col in range(NUM_COLUNAS):
            cartao = customtkinter.CTkButton(
                tabview.tab('flores'),
                command=lambda r=linha, c=col: click_flores(r, c),
                text='',
                width=CARTAO_SIZE_W,
                height=CARTAO_SIZE_H,
                fg_color='black',
                bg_color='black',
                hover=False,
                image=black_image
            )
            cartao.grid(row=linha, column=col, padx=5, pady=5)
            linha_de_cartao.append(cartao)
        cartoes_flores.append(linha_de_cartao)
    
    label_tentativas_flores.configure(text=f'Tentativas: {tentativas_flores}/{MAX_TENTATIVAS} | Pares: {pares_encontrados_flores}/8')

def click_flores(linha, coluna):
    global cartao_bloqueado_flores, tentativas_flores, pares_encontrados_flores
    
    if cartao_bloqueado_flores:
        return
    
    cartao = cartoes_flores[linha][coluna]
    
    # Se o cartão já foi revelado ou já foi eliminado, não faz nada
    if not cartao.winfo_ismapped():  # Cartão já foi eliminado
        return
    
    cor_atual = cartao.cget('fg_color')
    
    # Se o cartão já está revelado, não faz nada
    if cor_atual != 'black':
        return
    
    # Revelar o cartão (mostrar a imagem)
    cartao.configure(image=CARTAO_IMG_FLORES[grid_flores[linha][coluna]], 
                    fg_color=grid_flores[linha][coluna], 
                    bg_color=grid_flores[linha][coluna])
    cartao_revelado_flores.append((cartao, linha, coluna))
    
    # Se temos 2 cartões revelados, verificar se são iguais
    if len(cartao_revelado_flores) == 2:
        cartao_bloqueado_flores = True
        tentativas_flores += 1
        label_tentativas_flores.configure(text=f'Tentativas: {tentativas_flores}/{MAX_TENTATIVAS} | Pares: {pares_encontrados_flores}/8')
        
        cartao1, linha1, coluna1 = cartao_revelado_flores[0]
        cartao2, linha2, coluna2 = cartao_revelado_flores[1]
        
        cor1 = grid_flores[linha1][coluna1]
        cor2 = grid_flores[linha2][coluna2]
        
        if cor1 == cor2:
            # Cartões iguais - ELIMINAR ambos após um breve delay
            pares_encontrados_flores += 1
            
            # Eliminar primeiro cartão
            app.after(800, lambda: eliminar_cartao(cartao1) if cartao1.winfo_exists() else None)
            # Eliminar segundo cartão
            app.after(800, lambda: eliminar_cartao(cartao2) if cartao2.winfo_exists() else None)
            
            # Limpar lista de revelados após um delay
            cartao_revelado_flores.clear()
            cartao_bloqueado_flores = False
            
            # Verificar se ganhou
            if pares_encontrados_flores == 8:  # 8 pares no total (16 cartões / 2)
                app.after(1200, lambda: mostrar_mensagem_vitoria_flores())
        else:
            # Cartões diferentes - esconder após 1 segundo
            cartao1.after(1000, lambda: cartao1.configure(image=black_image, fg_color='black', bg_color='black') if cartao1.winfo_exists() else None)
            cartao2.after(1000, lambda: cartao2.configure(image=black_image, fg_color='black', bg_color='black') if cartao2.winfo_exists() else None)
            
            # Limpar lista de revelados e desbloquear após 1 segundo
            app.after(1200, desbloquear_jogo_flores)
            
            # Verificar se perdeu
            if tentativas_flores >= MAX_TENTATIVAS:
                app.after(1300, lambda: mostrar_mensagem_derrota_flores())

def desbloquear_jogo_flores():
    global cartao_bloqueado_flores
    cartao_revelado_flores.clear()
    cartao_bloqueado_flores = False

def mostrar_mensagem_vitoria_flores():
    resposta = messagebox.askyesno("Parabéns!", 
                                  f"Você encontrou todos os 8 pares em {tentativas_flores} tentativas!\nDeseja jogar novamente?")
    if resposta:
        reiniciar_jogo_flores()
    else:
        tabview.set('flores')

def mostrar_mensagem_derrota_flores():
    resposta = messagebox.askyesno("Fim do jogo", 
                                  f"Você usou todas as {MAX_TENTATIVAS} tentativas!\nEncontrou {pares_encontrados_flores} pares.\nDeseja jogar novamente?")
    if resposta:
        reiniciar_jogo_flores()
    else:
        tabview.set('flores')
#============================================================================
# FUNÇÕES PARA A ABA 'CARROS'
# ============================================================================
def reiniciar_jogo_carros():
    global grid_carros, cartoes_carros, cartao_revelado_carros, cartao_correspondente_carros
    global tentativas_carros, cartao_bloqueado_carros, pares_encontrados_carros
    
    # Limpar cartões antigos
    for linha in cartoes_carros:
        for cartao in linha:
            if cartao.winfo_exists():
                cartao.destroy()
    
    # Reiniciar variáveis
    grid_carros = creat_card_grid(CARROS_COLORS)
    cartoes_carros = []
    cartao_revelado_carros = []
    cartao_correspondente_carros = []
    pares_encontrados_carros = 0
    tentativas_carros = 0
    cartao_bloqueado_carros = False
    
    # Criar novos cartões
    for linha in range(NUM_LINHAS):
        linha_de_cartao = []
        for col in range(NUM_COLUNAS):
            cartao = customtkinter.CTkButton(
                tabview.tab('carros'),
                command=lambda r=linha, c=col: click_carros(r, c),
                text='',
                width=CARTAO_SIZE_W,
                height=CARTAO_SIZE_H,
                fg_color='black',
                bg_color='black',
                hover=False,
                border_color='gray'
            )
            cartao.grid(row=linha, column=col, padx=5, pady=5)
            linha_de_cartao.append(cartao)
        cartoes_carros.append(linha_de_cartao)
    
    label_tentativas_carros.configure(text=f'Tentativas: {tentativas_carros}/{MAX_TENTATIVAS} | Pares: {pares_encontrados_carros}/8')

# ============================================================================
# FUNÇÕES PARA A ABA 'carros'
# ============================================================================

def click_carros(linha, coluna):
    global cartao_bloqueado_carros, tentativas_carros, pares_encontrados_carros
    
    if cartao_bloqueado_carros:
        return
    
    cartao = cartoes_carros[linha][coluna]
    
    # Se o cartão já foi revelado ou já foi eliminado, não faz nada
    if not cartao.winfo_ismapped():  # Cartão já foi eliminado
        return
    
    cor_atual = cartao.cget('fg_color')
    
    # Se o cartão já está revelado, não faz nada
    if cor_atual != 'black':
        return
    
    # Revelar o cartão (mostrar a imagem)
    cartao.configure(image=CARTAO_IMG_CARROS[grid_carros[linha][coluna]], 
                    fg_color=grid_carros[linha][coluna], 
                    bg_color=grid_carros[linha][coluna])
    cartao_revelado_carros.append((cartao, linha, coluna))
    
    # Se temos 2 cartões revelados, verificar se são iguais
    if len(cartao_revelado_carros) == 2:
        cartao_bloqueado_carros = True
        tentativas_carros += 1
        label_tentativas_carros.configure(text=f'Tentativas: {tentativas_carros}/{MAX_TENTATIVAS} | Pares: {pares_encontrados_carros}/8')
        
        cartao1, linha1, coluna1 = cartao_revelado_carros[0]
        cartao2, linha2, coluna2 = cartao_revelado_carros[1]
        
        cor1 = grid_carros[linha1][coluna1]
        cor2 = grid_carros[linha2][coluna2]
        
        if cor1 == cor2:
            # Cartões iguais - ELIMINAR ambos após um breve delay
            pares_encontrados_carros += 1
            
            # Eliminar primeiro cartão
            app.after(800, lambda: eliminar_cartao(cartao1) if cartao1.winfo_exists() else None)
            # Eliminar segundo cartão
            app.after(800, lambda: eliminar_cartao(cartao2) if cartao2.winfo_exists() else None)
            
            # Limpar lista de revelados após um delay
            cartao_revelado_carros.clear()
            cartao_bloqueado_carros = False
            
            # Verificar se ganhou
            if pares_encontrados_carros == 8:  # 8 pares no total (16 cartões / 2)
                app.after(1200, lambda: mostrar_mensagem_vitoria_carros())
        else:
            # Cartões diferentes - esconder após 1 segundo
            cartao1.after(1000, lambda: cartao1.configure(image=black_image, fg_color='black', bg_color='black') if cartao1.winfo_exists() else None)
            cartao2.after(1000, lambda: cartao2.configure(image=black_image, fg_color='black', bg_color='black') if cartao2.winfo_exists() else None)
            
            # Limpar lista de revelados e desbloquear após 1 segundo
            app.after(1200, desbloquear_jogo_carros)
            
            # Verificar se perdeu
            if tentativas_carros >= MAX_TENTATIVAS:
                app.after(1300, lambda: mostrar_mensagem_derrota_carros())
def desbloquear_jogo_carros():
    global cartao_bloqueado_carros
    cartao_revelado_carros.clear()
    cartao_bloqueado_carros = False

def mostrar_mensagem_vitoria_carros():
    resposta = messagebox.askyesno("Parabéns!", 
                                  f"Você encontrou todos os 8 pares em {tentativas_carros} tentativas!\nDeseja jogar novamente?")
    if resposta:
        reiniciar_jogo_carros()
    else:
        tabview.set('carros')

def mostrar_mensagem_derrota_carros():
    resposta = messagebox.askyesno("Fim do jogo", 
                                  f"Você usou todas as {MAX_TENTATIVAS} tentativas!\nEncontrou {pares_encontrados_carros} pares.\nDeseja jogar novamente?")
    if resposta:
        reiniciar_jogo_carros()
    else:
        tabview.set('carros')
# ============================================================================
# FUNÇÕES PARA A ABA 'bandeiras'
# ============================================================================
def reiniciar_jogo_bandeiras():
    global grid_bandeiras, cartoes_bandeiras, cartao_revelado_bandeiras, cartao_correspondente_bandeiras
    global tentativas_bandeiras, cartao_bloqueado_bandeiras, pares_encontrados_bandeiras
    
    # Limpar cartões antigos
    for linha in cartoes_bandeiras:
        for cartao in linha:
            if cartao.winfo_exists():
                cartao.destroy()
    
    # Reiniciar variáveis
    grid_bandeiras = creat_card_grid(BANDEIRAS_COLORS)
    cartoes_bandeiras = []
    cartao_revelado_bandeiras = []
    cartao_correspondente_bandeiras = []
    pares_encontrados_bandeiras = 0
    tentativas_bandeiras = 0
    cartao_bloqueado_bandeiras = False
    
    # Criar novos cartões
    for linha in range(NUM_LINHAS):
        linha_de_cartao = []
        for col in range(NUM_COLUNAS):
            cartao = customtkinter.CTkButton(
                tabview.tab('bandeiras'),
                command=lambda r=linha, c=col: click_bandeiras(r, c),
                text='',
                width=CARTAO_SIZE_W,
                height=CARTAO_SIZE_H,
                fg_color='black',
                bg_color='black',
                hover=False,
                image=black_image
            )
            cartao.grid(row=linha, column=col, padx=5, pady=5)
            linha_de_cartao.append(cartao)
        cartoes_bandeiras.append(linha_de_cartao)
    
    label_tentativas_bandeiras.configure(text=f'Tentativas: {tentativas_bandeiras}/{MAX_TENTATIVAS} | Pares: {pares_encontrados_bandeiras}/8')

def click_bandeiras(linha, coluna):
    global cartao_bloqueado_bandeiras, tentativas_bandeiras, pares_encontrados_bandeiras
    
    if cartao_bloqueado_bandeiras:
        return
    
    cartao = cartoes_bandeiras[linha][coluna]
    
    # Se o cartão já foi revelado ou já foi eliminado, não faz nada
    if not cartao.winfo_ismapped():  # Cartão já foi eliminado
        return
    
    cor_atual = cartao.cget('fg_color')
    
    # Se o cartão já está revelado, não faz nada
    if cor_atual != 'black':
        return
    
    # Revelar o cartão (mostrar a imagem)
    cartao.configure(image=CARTAO_IMG_BANDEIRAS[grid_bandeiras[linha][coluna]], 
                    fg_color=grid_bandeiras[linha][coluna], 
                    bg_color=grid_bandeiras[linha][coluna])
    cartao_revelado_bandeiras.append((cartao, linha, coluna))
    
    # Se temos 2 cartões revelados, verificar se são iguais
    if len(cartao_revelado_bandeiras) == 2:
        cartao_bloqueado_bandeiras = True
        tentativas_bandeiras += 1
        label_tentativas_bandeiras.configure(text=f'Tentativas: {tentativas_bandeiras}/{MAX_TENTATIVAS} | Pares: {pares_encontrados_bandeiras}/8')
        
        cartao1, linha1, coluna1 = cartao_revelado_bandeiras[0]
        cartao2, linha2, coluna2 = cartao_revelado_bandeiras[1]
        
        cor1 = grid_bandeiras[linha1][coluna1]
        cor2 = grid_bandeiras[linha2][coluna2]
        
        if cor1 == cor2:
            # Cartões iguais - ELIMINAR ambos após um breve delay
            pares_encontrados_bandeiras += 1
            
            # Eliminar primeiro cartão
            app.after(800, lambda: eliminar_cartao(cartao1) if cartao1.winfo_exists() else None)
            # Eliminar segundo cartão
            app.after(800, lambda: eliminar_cartao(cartao2) if cartao2.winfo_exists() else None)
            
            # Limpar lista de revelados após um delay
            cartao_revelado_bandeiras.clear()
            cartao_bloqueado_bandeiras = False
            
            # Verificar se ganhou
            if pares_encontrados_bandeiras == 8:  # 8 pares no total (16 cartões / 2)
                app.after(1200, lambda: mostrar_mensagem_vitoria_bandeiras())
        else:
            # Cartões diferentes - esconder após 1 segundo
            cartao1.after(1000, lambda: cartao1.configure(image=black_image, fg_color='black', bg_color='black') if cartao1.winfo_exists() else None)
            cartao2.after(1000, lambda: cartao2.configure(image=black_image, fg_color='black', bg_color='black') if cartao2.winfo_exists() else None)
            
            # Limpar lista de revelados e desbloquear após 1 segundo
            app.after(1200, desbloquear_jogo_bandeiras)
            
            # Verificar se perdeu
            if tentativas_bandeiras >= MAX_TENTATIVAS:
                app.after(1300, lambda: mostrar_mensagem_derrota_bandeiras())

def desbloquear_jogo_bandeiras():
    global cartao_bloqueado_bandeiras
    cartao_revelado_bandeiras.clear()
    cartao_bloqueado_bandeiras = False

def mostrar_mensagem_vitoria_bandeiras():
    resposta = messagebox.askyesno("Parabéns!", 
                                  f"Você encontrou todos os 8 pares em {tentativas_bandeiras} tentativas!\nDeseja jogar novamente?")
    if resposta:
        reiniciar_jogo_bandeiras()
    else:
        tabview.set('bandeiras')

def mostrar_mensagem_derrota_bandeiras():
    resposta = messagebox.askyesno("Fim do jogo", 
                                  f"Você usou todas as {MAX_TENTATIVAS} tentativas!\nEncontrou {pares_encontrados_bandeiras} pares.\nDeseja jogar novamente?")
    if resposta:
        reiniciar_jogo_bandeiras()
    else:
        tabview.set('bandeiras')
# ============================================================================
# INTERFACE GRÁFICA
# ============================================================================
app = customtkinter.CTk()
app.geometry('560x680')
app.title("Memória de elefante")
app.resizable(width=False, height=False)
color5 = "#fffafa"
def menuf():
    toplevel = ctk.CTkToplevel(app, width=200 ,height=200)
    toplevel.title("Sobre")
    tabview = ctk.CTkTabview(toplevel, segmented_button_selected_color="#6495ed")
    tabview.pack(padx=10, pady=10)
    tabview.add('Sobre')  # add tab at the end
    tabview.add('Autores')  # add tab at the end
    tabview.set('Sobre')  # set currently visible tab

    label_version = ctk.CTkLabel(tabview.tab("Sobre"), text='versã0 1.0', width=40, height=28, fg_color='transparent' ,font=('Verdana',16,"bold"))
    label_version.pack()
    label_img = ctk.CTkLabel(tabview.tab("Sobre"), text='Memória de elefante \n Venha divertir-se com esse belo jogo de memória \n Memória de elefante é um projecto Jeel Solftwares  ', width=40, height=28, fg_color='transparent' ,font=('Verdana',16,"bold"))
    label_img.pack()
    label_codigo = ctk.CTkLabel(tabview.tab("Autores"), text='CODIGO', width=40, height=28, fg_color='transparent' ,font=('Verdana',16,"bold"))
    label_codigo.pack()
    label_autor = ctk.CTkLabel(tabview.tab("Autores"), text='João Salvador Paulo',text_color=color5, width=40, height=28, fg_color="#444343" ,font=('Verdana',16,"bold"),corner_radius=10)
    label_autor.pack()
    label_design = ctk.CTkLabel(tabview.tab("Autores"), text='DESIGN por', width=40, height=28, fg_color='transparent' ,font=('Verdana',16,"bold"))
    label_design.pack()
    label_autor = ctk.CTkLabel(tabview.tab("Autores"), text='João Salvador Paulo',text_color=color5, width=40, height=28, fg_color="#444343" ,font=('Verdana',16,"bold"),corner_radius=10)
    label_autor.pack()
    label_tel = ctk.CTkLabel(tabview.tab("Autores"), text='Contactos', width=40, height=28, fg_color='transparent' ,font=('Verdana',16,"bold"))
    label_tel.pack()
    label_autor = ctk.CTkLabel(tabview.tab("Autores"), text='+244 949 160 426',text_color=color5, width=40, height=28, fg_color="#444343" ,font=('Verdana',16,"bold"),corner_radius=10)
    label_autor.pack()
    
    
# Configurar aparência
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
frame = customtkinter.CTkFrame(app, width=510, height=30)
frame.pack()
try:
    menu = customtkinter.CTkImage(light_image=Image.open("img/menu.png"),
                                  dark_image=Image.open("img/menu.png"),
                                  size=(28, 28))
except:
    menu = customtkinter.CTkImage(light_image=Image.open(os.path.join(Path.home(), ".MemoriaDeElefante", "img", "menu.png")),
                                  dark_image=Image.open(os.path.join(Path.home(), ".MemoriaDeElefante", "img", "menu.png")),
                                  size=(28, 28))


button = customtkinter.CTkButton(frame, text='',image=menu,hover=False,fg_color="transparent",command=menuf)
button.place(x=420,y=1)
button1 = customtkinter.CTkLabel(frame, text='Memória de elefante', width=140, height=28,font=("Cursive",16,"bold"))
button1.place(x=0,y=0)
# Frame principal com abas
tabview = customtkinter.CTkTabview(app, width=500, height=600)
tabview.pack()

tabview.add('cores')
tabview.add('animais')
tabview.add('flores')
tabview.add('carros')
tabview.add('bandeiras')
tabview.set('cores')

# ============================================================================
# ABA 'CORES' - INTERFACE
# ============================================================================
# Botão de reiniciar para cores
botao_reiniciar_cores = customtkinter.CTkButton(
    tabview.tab('cores'),
    text="🔄 Reiniciar Jogo",
    command=reiniciar_jogo_cores,
    font=('Arial', 14, 'bold'),
    height=40,
    corner_radius=10,
    fg_color='#2E7D32',
    hover_color='#1B5E20'
)
botao_reiniciar_cores.grid(row=NUM_LINHAS, column=0, columnspan=NUM_COLUNAS, padx=10, pady=(10, 5), sticky='ew')

# Label de tentativas para cores
label_tentativas_cores = customtkinter.CTkLabel(
    tabview.tab('cores'),
    text=f'Tentativas: 0/{MAX_TENTATIVAS} | Pares: 0/8',
    font=('Arial', 16, 'bold'),
    text_color='white'
)
label_tentativas_cores.grid(row=NUM_LINHAS+1, column=0, columnspan=NUM_COLUNAS, padx=10, pady=(5, 10))

# ============================================================================
# ABA 'animais' - INTERFACE
# ============================================================================
# Botão de reiniciar para animais
botao_reiniciar_animais = customtkinter.CTkButton(
    tabview.tab('animais'),
    text="🔄 Reiniciar Jogo",
    command=reiniciar_jogo_animais,
    font=('Arial', 14, 'bold'),
    height=40,
    corner_radius=10,
    fg_color='#2E7D32',
    hover_color='#1B5E20'
)
botao_reiniciar_animais.grid(row=NUM_LINHAS, column=0, columnspan=NUM_COLUNAS, padx=10, pady=(10, 5), sticky='ew')

# Label de tentativas para animais
label_tentativas_animais = customtkinter.CTkLabel(
    tabview.tab('animais'),
    text=f'Tentativas: 0/{MAX_TENTATIVAS} | Pares: 0/8',
    font=('Arial', 16, 'bold'),
    text_color='white'
)
label_tentativas_animais.grid(row=NUM_LINHAS+1, column=0, columnspan=NUM_COLUNAS, padx=10, pady=(5, 10))
# ============================================================================
# Botão de reiniciar para flores
botao_reiniciar_flores = customtkinter.CTkButton(
    tabview.tab('flores'),
    text="🔄 Reiniciar Jogo",
    command=reiniciar_jogo_flores,
    font=('Arial', 14, 'bold'),
    height=40,
    corner_radius=10,
    fg_color='#2E7D32',
    hover_color='#1B5E20'
)
botao_reiniciar_flores.grid(row=NUM_LINHAS, column=0, columnspan=NUM_COLUNAS, padx=10, pady=(10, 5), sticky='ew')

# Label de tentativas para flores
label_tentativas_flores = customtkinter.CTkLabel(
    tabview.tab('flores'),
    text=f'Tentativas: 0/{MAX_TENTATIVAS} | Pares: 0/8',
    font=('Arial', 16, 'bold'),
    text_color='white'
)
label_tentativas_flores.grid(row=NUM_LINHAS+1, column=0, columnspan=NUM_COLUNAS, padx=10, pady=(5, 10))
# ============================================================================
# INICIALIZAÇÃO DOS JOGOS
# ============================================================================
# Botão de reiniciar para carros
botao_reiniciar_carros = customtkinter.CTkButton(
    tabview.tab('carros'),
    text="🔄 Reiniciar Jogo",
    command=reiniciar_jogo_carros,
    font=('Arial', 14, 'bold'),
    height=40,
    corner_radius=10,
    fg_color='#2E7D32',
    hover_color='#1B5E20'
)
botao_reiniciar_carros.grid(row=NUM_LINHAS, column=0, columnspan=NUM_COLUNAS, padx=10, pady=(10, 5), sticky='ew')

# Label de tentativas para carros
label_tentativas_carros = customtkinter.CTkLabel(
    tabview.tab('carros'),
    text=f'Tentativas: 0/{MAX_TENTATIVAS} | Pares: 0/8',
    font=('Arial', 16, 'bold'),
    text_color='white'
)
label_tentativas_carros.grid(row=NUM_LINHAS+1, column=0, columnspan=NUM_COLUNAS, padx=10, pady=(5, 10))
# ============================================================================
# ABA 'bandeiras' - INTERFACE
# ============================================================================
# Botão de reiniciar para bandeiras
botao_reiniciar_bandeiras = customtkinter.CTkButton(
    tabview.tab('bandeiras'),
    text="🔄 Reiniciar Jogo",
    command=reiniciar_jogo_bandeiras,
    font=('Arial', 14, 'bold'),
    height=40,
    corner_radius=10,
    fg_color='#2E7D32',
    hover_color='#1B5E20'
)
botao_reiniciar_bandeiras.grid(row=NUM_LINHAS, column=0, columnspan=NUM_COLUNAS, padx=10, pady=(10, 5), sticky='ew')

# Label de tentativas para bandeiras
label_tentativas_bandeiras = customtkinter.CTkLabel(
    tabview.tab('bandeiras'),
    text=f'Tentativas: 0/{MAX_TENTATIVAS} | Pares: 0/8',
    font=('Arial', 16, 'bold'),
    text_color='white'
)
label_tentativas_bandeiras.grid(row=NUM_LINHAS+1, column=0, columnspan=NUM_COLUNAS, padx=10, pady=(5, 10))

# Variáveis globais para o jogo de cores
grid_cores = creat_card_grid(CARTAO_COLORS)
cartoes_cores = []
cartao_revelado_cores = []
cartao_correspondente_cores = []
tentativas_cores = 0
pares_encontrados_cores = 0
cartao_bloqueado_cores = False

# Variáveis globais para o jogo de animais
grid_animais = creat_card_grid(ANIMAIS_COLORS)
cartoes_animais = []
cartao_revelado_animais = []
cartao_correspondente_animais = []
tentativas_animais = 0
pares_encontrados_animais = 0
cartao_bloqueado_animais = False

# Variáveis globais para o jogo de flores
grid_flores = creat_card_grid(FLORES_COLORS)
cartoes_flores = []
cartao_revelado_flores = []
cartao_correspondente_flores = []
tentativas_flores = 0
pares_encontrados_flores = 0
cartao_bloqueado_flores = False


# Variáveis globais para o jogo de carros
grid_carros = creat_card_grid(CARROS_COLORS)
cartoes_carros = []
cartao_revelado_carros = []
cartao_correspondente_carros = []
tentativas_carros = 0
pares_encontrados_carros = 0
cartao_bloqueado_carros = False
# Variáveis globais para o jogo de bandeiras
grid_bandeiras = creat_card_grid(BANDEIRAS_COLORS)
cartoes_bandeiras = []
cartao_revelado_bandeiras = []
cartao_correspondente_bandeiras = []
tentativas_bandeiras = 0
pares_encontrados_bandeiras = 0
cartao_bloqueado_bandeiras = False

# Inicializar ambos os jogos
reiniciar_jogo_cores()
reiniciar_jogo_animais()
reiniciar_jogo_carros()
reiniciar_jogo_flores()
reiniciar_jogo_bandeiras()
app.mainloop()