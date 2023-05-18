def divided_image(image_permuted,img_size,patch_size):
  # Setup code to plot whole image as patches
  img_size = 224
  patch_size = 16
  num_patches = img_size/patch_size 
  assert img_size % patch_size == 0, "Image size must be divisible by patch size"
  print(f"Number of patches per row: {num_patches}\
    \nNumber of patches per column: {num_patches}\
    \nTotal patches: {num_patches*num_patches}\
    \nPatch size: {patch_size} pixels x {patch_size} pixels")

  # Create a series of subplots
  fig, axs = plt.subplots(nrows=img_size // patch_size,
                          ncols=img_size // patch_size,
                          figsize=(num_patches, num_patches),
                          sharex=True,
                          sharey=True)

  # Loop through height and width of image
  for i, patch_height in enumerate(range(0, img_size, patch_size)): # iterate through height
    for j, patch_width in enumerate(range(0, img_size, patch_size)):
      # Plot the permuted image on the different axes 
      axs[i, j].imshow(image_permuted[patch_height:patch_height+patch_size, # iterate through height
                                      patch_width:patch_width+patch_size, # iterate through width
                                      :]) # get all color channels
      # Set up label information for each subplot (patch)
      axs[i, j].set_ylabel(i+1,
                          rotation="horizontal",
                          horizontalalignment="right",
                          verticalalignment="center")
      axs[i, j].set_xlabel(j+1)
      axs[i, j].set_xticks([])
      axs[i, j].set_yticks([])
      axs[i, j].label_outer()

  # Set up a title for the plot
  fig.suptitle(f"{class_names[label]} -> Patchified", fontsize=14)
  plt.show()
