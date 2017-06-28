
def mod_pixels(img,red_transform,green_transform,blue_transform):

	source_pixels = list(img.getdata())	
	work_pixels = []
	output_image = Image.new(img.mode, img.size)
	for r,g,b in source_pixels:
		new_red = pixel_transform(r, red_transform)
		new_green = pixel_transform(g, green_transform)
		new_blue = pixel_transform(b, blue_transform)
		new_data = (new_red, new_green, new_blue)
		work_pixels.append(new_data)

		output_image.putdata(work_pixels)
		return output_image
		


def pixel_transform(pixel, transformation):

	if transformation = 'null':
		pixel=pixel

	if transformation = 'black':
		pixel=0

	if transformation = 'white':
		pixel=255

	if transform = 'shift':
		pixel = pixel + (int(pixel * .5))

	return pixel

source_image = Image.open("work.jpg")
new_image = mod_pixels(new_image, 'null', 'white', 'shift')
new_image.show()
