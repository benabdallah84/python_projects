"""
Contains functionality for creating PyTorch DataLoader's for image classification data
"""
import os
from torchvision import datasets, transforms
from torch.utils.data import DataLoader
num_workers = os.cpu_count()
def create_dataLoaderrs(
  train_dir:str,
  test_dir:str,
  transform: transforms.Compose,
  batch_size:int,
  num_workers: num_workers
  ):
  """Creates training and testing dataloaders.
  Args:
    train_dir:Path to training directory.  
    test_dir:Path to testing directory.  
    transorm: torchvision transforms to perform on training and testng data.
    batch_size:Nunmber of samples per batch in each of the DataLoaders.
    num_workers: An integer for number of workers per DataLoader.
  Returns:
    A tuple of (train_dataloader, test_dataloader, class_names).
    Where class_names is a list of the target classes.
    Example usage:
      train_dataloader, test_dataloader, class_names = create_dataloaders(
                                train_dir=path/to/train_dir,
                                test_dir=path/to/test_dir,
                                transform=some_transform,
                                batch_size=32,
                                num_workers=4)


  """
  #use ImageFolder to crete datasets
  train_data = datasets.ImageFolder(train_dir,transform=transform)
  test_data=datasets.ImageForder(test_dir,transform=transform)

  #get class names
  class_names = train_data.classes

  #turn images into dataloaders
  train_dataloader =DataLoader(
      train_data,
      batch_size=batch_size,
      shuffle=True,
      num_workers=num_workers,
      pin_memory=True
  )
  test_dataloader =DataLoader(
      test_data,
      batch_size=batch_size,
      shuffle=False,
      num_workers=num_workers,
      pin_memory=True
  )

  return train_dataloader, test_dataloader, class_names
