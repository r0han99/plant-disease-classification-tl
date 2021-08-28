# Comparative Study on Reliability of Transfer Learning to Classify Plant-Based Diseases

***

![tl-banner](https://user-images.githubusercontent.com/45916202/130671624-16e99fe7-ab8f-4ef3-b790-79db1348b3ba.jpg)

***

*Abstract: One of the essential factors contributing to a plant's growth is identifying and preventing diseases in the early stages. Healthy plants are essential for a rich production. Recent advances in Deep learning - a subset of Artificial Intelligence and Machine Learning are playing a pivotal role in solving image classification problems and can be applied to the agricultural sector for crop surveillance and early anomaly identification. For this research, we used an open-source dataset of leaf images divided into three classes, two of which are the most common disease types found on many crops; the graphical characterizations for the three classes are images of leaves with Powdery Residue, images of leaves with Rusty Spots, and images of Healthy leaves. The primary objective of this research is to present a pre-trained ImageNet network architecture that is well suited for dealing with plant-based data, even when sample sizes collected are limited. We used different convolutional neural network-based architectures such as InceptionV3, MobileNetV2, Xception, VGG16, and VGG19 to classify plant leaf images with visually different representations of each disease. Xception, MobileNetV2, and DenseNet had a considerable advantage over all the performance metrics recorded among the other networks trained.*

## Sample Classes


![cls-banner](https://user-images.githubusercontent.com/45916202/130671846-b8fdac38-e460-4907-a56b-0ad490ad12c8.png)


## Metric Evaluation Report 

| Model       | Test Accuracy | F1 Score | Precision | Recall | Total Correct on Test Set/105 |
| ----------- | ------------- | -------- | --------- | ------ | ----------------------------- |
| DenseNet121 | 0.990         | 0.961    | 0.961     | 0.962  | 101                           |
| VGG16       | 0.933         | 0.904    | 0.904     | 0.908  | 95                            |
| InceptionV3 | 0.971         | 0.932    | 0.933     | 0.935  | 98                            |
| MobileNetV2 | 0.971         | 0.962    | 0.961     | 0.965  | 101                           |
| Xception    | 0.942         | 0.942    | 0.942     | 0.943  | 99                            |
| VGG19       | 0.857         | 0.839    | 0.838     | 0.867  | 88                            |
| ConvNet     | 0.760         | 0.656    | 0.657     | 0.660  | 69                            |


***

_Citation: {@article{noauthororeditor,
  abstract = {One of the essential factors contributing to a plant's growth is identifying and preventing diseases in the early stages. Healthy plants are essential for a rich production. Recent advances in Deep learning - a subset of Artificial Intelligence and Machine Learning are playing a pivotal role in solving image classification problems and can be applied to the agricultural sector for crop surveillance and early anomaly identification. For this research, we used an open-source dataset of leaf images divided into three classes, two of which are the most common disease types found on many crops; the graphical characterizations for the three classes are images of leaves with Powdery Residue, images of leaves with Rusty Spots, and images of Healthy leaves. The primary objective of this research is to present a pre-trained ImageNet network architecture that is well suited for dealing with plant-based data, even when sample sizes collected are limited. We used different convolutional neural network-based architectures such as InceptionV3, MobileNetV2, Xception, VGG16, and VGG19 to classify plant leaf images with visually different representations of each disease. Xception, MobileNetV2, and DenseNet had a considerable advantage over all the performance metrics recorded among the other networks trained.},
  added-at = {2021-08-27T13:26:48.000+0200},
  author = {Sai, N Rohan and Rao, T Sudarshan and Kumari, G. L. Aruna},
  biburl = {https://www.bibsonomy.org/bibtex/2de3ddaca08414042a045fdb8b5f8e48c/ijeat_beiesp},
  doi = {10.35940/ijeat.F3080.0810621},
  editor = {Kumar, Dr. Shiv},
  interhash = {55788751bed7d18c45cb40244eceae07},
  intrahash = {de3ddaca08414042a045fdb8b5f8e48c},
  issn = {2249-8958},
  journal = {International Journal of Engineering and Advanced Technology (IJEAT)},
  keywords = {Artificial Intelligence, Deep Learning, Neural
Networks, Transfer Learning},
  language = {En},
  month = {August},
  number = 6,
  pages = {154-160},
  timestamp = {2021-08-27T13:26:48.000+0200},
  title = {Comparative Study on Reliability of Transfer Learning to Classify Plant-Based Diseases},
  url = {https://www.ijeat.org/wp-content/uploads/papers/v10i6/F30800810621.pdf},
  volume = 10,
  year = 2021
}_




