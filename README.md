## samosa_classifier
I know it's a bit weird but yes.The idea was to make a real time image classifier ,so I went with this.
### Dataset
I downloaded around 100 images of samosa from the google images, though I knew one cannot make a deep learning model with that sort of data.
Hence to increase the dataset size, I applied augmentation to the images via keras data generator function by augmenting its properties to a 
large extent
#### including cifar-10
I included 5000 images of cifar -10 fr training the model on positive as well as negative examples and 
2500 images for testing set.                           
## Training the Model
I trained the model firstly by using the tensorflow and then keras(scikit of deep learning lol) .
it gave pretty good results by the way
## making it real time
The real task was to make this real time . Initially, I thought to make use of laptop's webcam but it didn't go well (Ps: the camera quality was stupid in 
fact) . Then I decided to use my phone's camera 
### Including Firebase
So a friend of mine made a simple android app which clicks a photo and posts a downloadable link at the firebase and I used that link to
straight away download the file and load the image in the model . I know it's not that much fancy but I had to do this 
#### So this sums up my little adventure
