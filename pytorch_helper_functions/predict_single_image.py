# Download custom image
import requests
def predict_single_image(custom_image_path,image_external_path):
  # Setup custom image path
  custom_image_path = custom_image_path

  # Download the image if it doesn't already exist
  if not custom_image_path.is_file():
      with open(custom_image_path, "wb") as f:
          # When downloading from GitHub, need to use the "raw" file link
          request = requests.get(image_external_path)
          print(f"Downloading {custom_image_path}...")
          f.write(request.content)
  else:
      print(f"{custom_image_path} already exists, skipping download.")

  # Predict on custom image
  pred_and_plot_image(model=model,
                      image_path=custom_image_path,
                      class_names=class_names)
