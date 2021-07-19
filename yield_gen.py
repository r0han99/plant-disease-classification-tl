
# Modules 
from tensorflow.keras.preprocessing.image import ImageDataGenerator




# docs 
def docs():

    docstring = '''

    * functions
        - generator() : arguments gen_type = ( with-aug | with-augmentation ) & host = ( local | colab )

    * usage 
    
        from yield_gen import * 
        train, valid, test = generator(gen_type="with-aug", host="colab") # returns a tf.generator object with data

    * requirements
    
        - local data directory structure
            ./plant-data
                /Train
                    /Train
                        ..samples
                /Test
                    /Test
                        ..samples 
                /Validation
                    /Validation
                        ..samples
        
        - Colab data directory structure 
            ./drive
                ./MyDrive
                    /plant-data
                        /Train
                            /Train
                                ..samples
                        /Test
                            /Test
                                ..samples 
                        /Validation
                            /Validation
                                ..samples

     
    '''

    print(docstring)


def set_paths(host):

    if host == "local":
        print("Local Paths Returned")
        train_dir = './plant-data/Train/Train'
        test_dir = './plant-data/Test/Test'
        valid_dir = './plant-data/Validation/Validation'
        
        return (train_dir, test_dir, valid_dir)

    elif host == "colab":
        print("Colab Paths Returned")
        train_dir = './drive/MyDrive/plant-data/Train/Train'
        test_dir = './drive/MyDrive/plant-data/Test/Test'
        valid_dir = './drive/MyDrive/plant-data/Validation/Validation'
        
        return (train_dir, test_dir, valid_dir)
    
    else:
        print("Invalid Host, returning default")
        set_paths(host="colab")
        



def generator(gen_type, host):

    
    train_dir, test_dir, valid_dir = set_paths(host=host)

    if gen_type == "with-aug" or gen_type == "with-augmentation":

        image_shape = [256,256,3]

        image_gen_with_aug = ImageDataGenerator(rotation_range=20, # rotate the image 20 degrees
                               width_shift_range=0.10, # Shift the pic width by a max of 5%
                               height_shift_range=0.10, # Shift the pic height by a max of 5%
                               rescale=1/255, # Rescale the image by normalzing it.
                               zoom_range=0.1, # Zoom in by 10% max
                              )


        a_train = image_gen_with_aug.flow_from_directory(train_dir,
                                               target_size=image_shape[:2],
                                               color_mode='rgb',
                                               class_mode='categorical')

        a_valid = image_gen_with_aug.flow_from_directory(valid_dir,
                                               target_size=image_shape[:2],
                                               color_mode='rgb',
                                               class_mode='categorical')
    
        
        a_test = image_gen_with_aug.flow_from_directory(test_dir,
                                               target_size=image_shape[:2],
                                               color_mode='rgb',
                                               class_mode='categorical')    


        return (a_train, a_valid, a_test)


    elif gen_type == "without-aug" or gen_type == "without-augmentation":

        image_shape = [256,256,3]

        image_gen_without_aug = ImageDataGenerator(rescale=1/255) # Rescale the image by normalzing it.

        wa_train = image_gen_without_aug.flow_from_directory(train_dir,
                                               target_size=image_shape[:2],
                                               color_mode='rgb',
                                               class_mode='categorical')

        wa_valid = image_gen_without_aug.flow_from_directory(valid_dir,
                                               target_size=image_shape[:2],
                                               color_mode='rgb',
                                               class_mode='categorical')                           


        wa_test = image_gen_without_aug.flow_from_directory(test_dir,
                                               target_size=image_shape[:2],
                                               color_mode='rgb',
                                               class_mode='categorical')   

        
        return (wa_train, wa_valid, wa_test)


    