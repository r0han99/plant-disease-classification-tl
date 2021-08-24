# evaluation pipeline
import tensorflow as tf 
import matplotlib.pyplot as plt 
plt.style.use("classic")
from tensorflow.keras.models import load_model
from zipfile import ZipFile



def evaluate_model(modelname,model, valid, test, history, elapsed):


  # zipobj
  zipobj = ZipFile('./drive/MyDrive/{}.zip'.format(modelname), 'w')

  # evaluating validation
  new_loss, new_acc = model.evaluate_generator(valid)
  print('Validation Accuracy - {:.2f}%'.format(new_acc*100))
  print('validation loss - {:.2f}'.format(new_loss))

  # evaluating test 
  test_loss, test_acc = model.evaluate_generator(test)
  print('Test Accuracy - {:.2f}%'.format(test_acc*100))
  print('Test loss - {:.2f}'.format(test_loss))


  # Plotting - LOSS
  plt.figure(figsize=(10,5))
  plt.plot(history['loss'],label='loss')
  plt.plot(history['val_loss'],ls='--',color='orange',label='validation-loss')
  plt.title('Epochs vs Validation_loss & Train_loss')
  plt.legend()
  plt.savefig("./drive/MyDrive/loss_valloss-{}.png".format(modelname))
  zipobj.write("./drive/MyDrive/loss_valloss-{}.png".format(modelname))

  # Plotting - Accuracy

  plt.figure(figsize=(10,5))
  plt.plot(history['accuracy'],label='Accuracy')
  plt.plot(history['val_accuracy'],ls='--',color='orange',label='validation-Accuracy')
  plt.title('Epochs vs Validation_Accuracy & Train-Accuracy')
  plt.legend(loc='upper left')
  plt.savefig("./drive/MyDrive/acc-valacc-{}.png".format(modelname))
  zipobj.write("./drive/MyDrive/acc-valacc-{}.png".format(modelname))


  history.to_csv("./drive/MyDrive/{}-stats.csv".format(modelname))
  zipobj.write("./drive/MyDrive/{}-stats.csv".format(modelname))

  # writing content

  content = """

Model - {}

* Train Accuracy - {:.2f}%
* Train loss - {:.2f}

* Validation Accuracy - {:.2f}%
* validation loss - {:.2f}

* Test Accuracy - {:.2f}%
* Test loss - {:.2f}

Elapsed - {} Mins

""".format(modelname, history.iloc[-1:,:].values[0][:2][1]*100, history.iloc[-1:,:].values[0][:2][0]*100,(new_acc*100), new_loss, (test_acc*100), test_loss, elapsed//60)


  with open("./drive/MyDrive/{}-summary.txt".format(modelname), "w") as f:
    f.write(content)

  zipobj.write("./drive/MyDrive/{}-summary.txt".format(modelname))

  print("preserving records")
  model.save("./drive/MyDrive/{}.h5".format(modelname))
  zipobj.write("./drive/MyDrive/{}.h5".format(modelname))

  print("{} Records Created".format(modelname))

  

  zipobj.close()
     


