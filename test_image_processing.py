from image_processing import load_image, save_image, apply_blur, resize_image

img = load_image('caminho/para/sua/imagem.jpg')
img_blur = apply_blur(img)
img_resized = resize_image(img_blur, 800, 600)
save_image(img_resized, 'caminho/para/imagem_processada.jpg')
