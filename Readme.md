## Task 
The aim of this task is to locate car couplings, that is the place where one train car attaches to the other. More specifically, for each image, we want to output the x coordinate (horizontal axis) where the coupling is located.



We have created a sample dataset using labelme, available here: https://drive.google.com/file/d/1qdFB0G6-0tDlgx3kWBIiQ8QWdGrtJ9Em

While the dataset contains a bounding box for each coupling, your final output should only output the x coordinate, estimating center of the coupling. Your solution should take a list of images as input and output the x coordinates, one per line:



./find_couplings image1.jpg image2.jpg

435

456



How and with which tools you approach the problem is up to you. We only ask that the submitted solution contains all the code including training (if there is any), that it can be run on a linux/ubuntu computer easily: either using pip dependencies or a docker image.

If training is involved, it should not take more than an hour on a GTX 1070 comparable GPU (or have a lower accuracy version that does not)



We are interested in a working solution, but do not expect you to spend large amounts of time on it. A few percent of accuracy is not crucial as long as the basic algorithm works and you describe how you would go about pushing it further.



Note that due to the nature of the project, all data we supply and your solution is confidential and must not be shared with a third party.
