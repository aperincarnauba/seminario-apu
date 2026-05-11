from PIL import Image
from collections import Counter
import os

assets_path = 'assets'
images = ['hero.png', '1.png', '2.png', '3.png', '4.png', '5.png', 'lifestyle.png', 'produto.png']

print("=" * 80)
print("ANÁLISE DE CORES DAS IMAGENS - FRIZO")
print("=" * 80)

for img_file in images:
    img_path = os.path.join(assets_path, img_file)
    if os.path.exists(img_path):
        print(f"\n🖼️  {img_file.upper()}")
        print("-" * 80)
        try:
            img = Image.open(img_path).convert('RGB')
            width, height = img.size
            print(f"Dimensões: {width}x{height} pixels")
            
            pixels = img.getdata()
            all_colors = Counter()
            
            # Count color frequencies
            for pixel in pixels:
                hex_color = '#{:02x}{:02x}{:02x}'.format(pixel[0], pixel[1], pixel[2])
                all_colors[hex_color] += 1
            
            # Get top 20 colors
            top_colors = all_colors.most_common(20)
            print(f"\nTop 20 cores mais frequentes:")
            print("Cor HEX        | Frequência (pixels) | % da imagem")
            print("-" * 60)
            
            total_pixels = sum(count for _, count in top_colors)
            for i, (color, count) in enumerate(top_colors, 1):
                percentage = (count / len(pixels)) * 100
                print(f"{color:<14} | {count:>18} | {percentage:>6.2f}%")
        except Exception as e:
            print(f"Erro ao processar {img_file}: {e}")
    else:
        print(f"\n⚠️  {img_file} - NÃO ENCONTRADO")

print("\n" + "=" * 80)
