"""Training script for waste classification using MobileNetV2 transfer learning.

Usage:
    python scripts/train.py --data_dir PATH_TO_DATA --output model/model.h5

Expect dataset organized with subfolders per class (ImageDataGenerator flow_from_directory style).
"""
import argparse
import os
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam


def build_model(num_classes, base_trainable=False):
    base = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
    base.trainable = base_trainable
    x = base.output
    x = GlobalAveragePooling2D()(x)
    out = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs=base.input, outputs=out)
    return model


def main(args):
    data_dir = args.data_dir
    out = args.output
    batch = args.batch_size
    epochs = args.epochs

    train_gen = ImageDataGenerator(rescale=1./255, validation_split=0.2,
                                   rotation_range=20, width_shift_range=0.1,
                                   height_shift_range=0.1, horizontal_flip=True)

    train_flow = train_gen.flow_from_directory(data_dir, target_size=(224, 224), batch_size=batch, subset='training')
    val_flow = train_gen.flow_from_directory(data_dir, target_size=(224, 224), batch_size=batch, subset='validation')

    num_classes = train_flow.num_classes
    model = build_model(num_classes, base_trainable=False)
    model.compile(optimizer=Adam(1e-4), loss='categorical_crossentropy', metrics=['accuracy'])

    model.fit(train_flow, validation_data=val_flow, epochs=epochs)

    os.makedirs(os.path.dirname(out), exist_ok=True)
    model.save(out)
    print('Saved model to', out)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', required=True, help='Path to dataset root (folders per class)')
    parser.add_argument('--output', default='model/model.h5')
    parser.add_argument('--batch_size', type=int, default=16)
    parser.add_argument('--epochs', type=int, default=10)
    args = parser.parse_args()
    main(args)
