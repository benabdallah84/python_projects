# Get a random list of image paths from test set
import random
def test_pred(num_images_to_plot:int,test_dir,):
  num_images_to_plot = num_images_to_plot
  test_image_path_list = list(Path(test_dir).glob("*/*.jpg")) # get list all image paths from test data 
  test_image_path_sample = random.sample(population=test_image_path_list, # go through all of the test image paths
                                        k=num_images_to_plot) # randomly select 'k' image paths to pred and plot

  # Make predictions on and plot the images
  for image_path in test_image_path_sample:
      pred_and_plot_image(model=model, 
                          image_path=image_path,
                          class_names=class_names,
                          # transform=weights.transforms(), # optionally pass in a specified transform from our pretrained model weights
                          image_size=(224, 224))
