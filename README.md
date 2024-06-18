# DeepBeauty
![GitHub Created At](https://img.shields.io/github/created-at/belluscher/deepbeauty)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/belluscher/deepbeauty)
![Python Badge](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=plastic)
![Static Badge](https://img.shields.io/badge/ULTRALYTICS-orange?style=plastic&logo=ULTRALYTICS)
![Static Badge](https://img.shields.io/badge/YOLOv8x-deeppink?style=plastic&logo=YOLOv8x)
![Static Badge](https://img.shields.io/badge/ROBOFLOW-purple?style=plastic&logo=ROBOFLOW)
![Streamlit Badge](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=fff&style=plastic)

![Eye Shape Recognition Project](https://github.com/belluscher/deepbeauty/blob/main/Deep_Beauty_banner.png)

# DEEP BEAUTY
> Eye Shape recognition with Ultralytics - YoloV8x

Makeup is fun!! And it's also a very relevant industry - the cosmetics industry was worth an estimated 451 billion dollars in 2023. The internet if filled with amazing content on the topic, with beauty staring amongst the 12 biggest categories on Youtube.
<p>
But for those who ever tried to follow a makeup tutorial, the results can be very different from the one of the creator. It's frustrating!
<p>
What the vast majority of people don't know is that the EYE SHAPE plays a huge hole on the sucess of the makeup endeavor. Angelina Jolie's eyes, for instance, are very different from Nicole Kidman's eyes, and every technique has to be addapted to each eye shape.
<p>
But do you know what is your eye shape? It's a hard to get "diagnosys" and the knowledge on it is kept at secret for the beauty professionals. And more: even if you know your eye shape, how to choose between the sea of content avaliable on youtube?
<p>
This is why Deep Beauty uses the power of deep learning to identify the user's eye shape and suggest youtube content from creators with the same eye shape. The project is also usefull for brands that want to tailor content to it's clients, creating a personalized learning experience.
  
## Getting started

To run the model you'll need to install these 2 powerfull libraries.
```
!pip install ultralytics
!pip install roboflow
```

The model was created and runs with Ultralytics, while Roboflow is responsible for creating the dataset with the notations and classes, allowing the object detection - in this case acting like face recognition.

## Datasets

The datasets are avaliable to download. 
<p>
The original dataset - Labeled Faces in the Wild - is a collection from the University of Massachusetts (2007), with 13000 human faces.
<p>
From it we selected the female faces and did eye notations on 676 images, with 1054 notations between the 8 classes. The shapes comprehended on the 8 classes are: ALMOND, UPTURNED, DOWNTURNED, HOODED, DEEP-SET, ROUND, PROTRUDING, MONOLID
<p>
  
- Eye Shape Dataset: https://app.roboflow.com/eyeshapes/eye-shapes/browse
- Original dataset: https://vis-www.cs.umass.edu/lfw/


## Local App

We've biult a local app to demonstrate the power of our model. It runs both uploading a picture and via live camera on a computer.
On terminal you need to type:

```
streamlit run Deep_Beauty.py
```

And streamlit will open a tab in your browser, where you can play and test the model. We're working to deploy it. Don't forget to change the model path on the py file for it to work properly.

### Web App

Ypu can also try it online!!

https://deepbeauty.streamlit.app/

We are working to solve any bugs that might appear. We know that the live camera doesn't pop up, but the model is running backstage, so it's predicting eye shapes and returning the mode of the results, after 7 seconds.

## Features

* Eye Shape Recognition
* Makeup tutorials suggestions based on the users eye shape
* In the future the model will identify the eye shape from the latest youtube makeup tutorials and do the suggestions automatically. Let's collaborate on that!

## Future

We keep improving this project, and our next goals are

* Improving the dataset with higher resolution images
* Improving the Youtube Libraries for each shape
* Write code to automatize the youtube suggestions (video eye shape recognition, webcraping, sellenium)
* Improve the angle reading on the model
* Create a mobile app - frontal camera usage
* Use GAN - Generative adversarial network - to make the tutorials with the user's face.


## Contributing

If you'd like to contribute, please fork the repository and use a feature
branch. Pull requests are warmly welcome.

## Links

Summary of most useful links:

- Project homepage: https://github.com/belluscher/deepbeauty
- Repository: https://github.com/belluscher/deepbeauty
- Issue tracker: https://github.com/belluscher/deepbeauty/issues
  - In case of sensitive bugs like security vulnerabilities, please contact
    belluscher@gmail.com directly instead of using issue tracker. We value your effort
    to improve the security and privacy of this project!
- Web App on Streamlit: https://deepbeauty.streamlit.app/
- Related projects:
  - More of our work on beauty, makeup, education and consulting: https://belluscher.com.br
  - For makeup related topics, please contact bel@belluscher.com.br


## Licensing

The code in this project is licensed under MIT license.



