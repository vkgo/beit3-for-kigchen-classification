from datasets import ImageNetDataset

ImageNetDataset.make_dataset_index(
    train_data_path = "/workspace/share/beit3/data/kitchen/train",
    val_data_path = "/workspace/share/beit3/data/kitchen/val",
    index_path = "/workspace/share/beit3/data/kitchen"
)